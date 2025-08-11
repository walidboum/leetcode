#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import time
import html
import unicodedata
from typing import List, Dict, Tuple, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://leetcode.ca"
ALL_URL = "https://leetcode.ca/all/problems.html"

# --------------------------
# HTTP
# --------------------------

def make_session() -> requests.Session:
    s = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "GET"],
    )
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; LeetScraper/1.2; +https://example.com)",
        "Accept-Language": "en-US,en;q=0.9",
    })
    s.mount("https://", HTTPAdapter(max_retries=retries))
    s.mount("http://", HTTPAdapter(max_retries=retries))
    return s

# --------------------------
# Utils
# --------------------------

_slug_re = re.compile(r"[^a-z0-9\-]+")

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip().replace(" ", "-")
    text = _slug_re.sub("", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "untitled"

def ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def clean_text(s: str) -> str:
    s = html.unescape(s).replace("\r\n", "\n").replace("\r", "\n")
    return s.strip()

def md_escape_inline(s: str) -> str:
    return s.replace("|", r"\|")

# --------------------------
# Index page parsing
# --------------------------

def parse_all_links(html_text: str) -> List[str]:
    """
    Extract problem page links from the 'All Problems' page.
    Current canonical format: /all/<num>.html. Keep fallback for older dated URLs.
    """
    soup = BeautifulSoup(html_text, "html.parser")
    links: List[str] = []

    def add(href: str):
        if not href:
            return
        if href.startswith("//"):
            href = "https:" + href
        abs_url = urljoin(BASE, href)
        links.append(abs_url)

    # Primary: /all/<num>.html
    for a in soup.select('a[href^="/all/"], a[href*="/all/"]'):
        href = a.get("href") or ""
        if re.search(r"/all/\d+\.html$", href):
            add(href)

    # Fallback: /yyyy-mm-dd-<num>-<title>
    for a in soup.select("a[href]"):
        href = a.get("href") or ""
        if re.search(r"/\d{4}-\d{2}-\d{2}-\d+-", href):
            add(href)

    # Dedup preserving order
    seen, uniq = set(), []
    for u in links:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq

# --------------------------
# Problem page parsing
# --------------------------

def extract_title_and_number(soup: BeautifulSoup) -> Tuple[Optional[int], str]:
    h1 = soup.find("h1")
    if not h1:
        txt = soup.get_text(" ", strip=True)
        m = re.search(r"\b(\d+)\.\s+(.+?)\s*(?=$)", txt)
        if m:
            return int(m.group(1)), m.group(2).strip()
        return None, ""
    title_text = clean_text(h1.get_text(" ", strip=True))
    m = re.match(r"^\s*(\d+)\.\s*(.+)$", title_text)
    if m:
        return int(m.group(1)), m.group(2).strip()
    return None, title_text

def extract_section_div_by_h3(soup: BeautifulSoup, header_text: str) -> Optional[Tag]:
    want = header_text.lower().rstrip(":")
    for h3 in soup.find_all("h3"):
        if h3.get_text(strip=True).lower().rstrip(":") == want:
            return h3.parent
    return None

def extract_difficulty(soup: BeautifulSoup) -> Optional[str]:
    div = extract_section_div_by_h3(soup, "Difficulty")
    if not div:
        return None
    span = div.find("span")
    if span:
        return clean_text(span.get_text())
    txt = div.get_text(" ", strip=True)
    m = re.search(r"\b(Easy|Medium|Hard)\b", txt, flags=re.I)
    return m.group(0).title() if m else None

def extract_company_tags(soup: BeautifulSoup) -> List[str]:
    div = extract_section_div_by_h3(soup, "Company")
    if not div:
        return []
    tags = []
    for a in div.select("a"):
        t = clean_text(a.get_text())
        if t:
            tags.append(t)
    seen, out = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out

def extract_problem_solution_link(soup: BeautifulSoup) -> Optional[str]:
    div = extract_section_div_by_h3(soup, "Problem Solution")
    if not div:
        return None
    a = div.find("a", href=True)
    return urljoin(BASE, a["href"]) if a else None

def extract_description_and_examples(
    soup: BeautifulSoup
) -> Tuple[str, List[Tuple[str, str, str]]]:
    """
    Return (description_markdown, examples)
    examples = list of (label, example_text, example_raw_html)
    """
    root = soup.select_one(".markdown-body") or soup
    description_parts: List[str] = []
    examples: List[Tuple[str, str, str]] = []

    example_re = re.compile(r"^Example\s*\d*\s*:?", re.I)
    found_example = False

    for node in root.children:
        if isinstance(node, NavigableString) or not isinstance(node, Tag):
            continue

        if node.name == "p":
            strong = node.find("strong")
            if strong:
                stxt = clean_text(strong.get_text())
                if example_re.match(stxt):
                    found_example = True
                    pre = node.find_next_sibling("pre")
                    if pre:
                        ex_text = clean_text(pre.get_text())
                        ex_raw = pre.decode_contents()  # raw HTML inside <pre>
                    else:
                        ex_text, ex_raw = "", ""
                    label = stxt if stxt.endswith(":") else (stxt + ":")
                    examples.append((label, ex_text, ex_raw))
                    continue

        if not found_example and node.name == "p":
            ptxt = clean_text(node.get_text(" ", strip=True))
            if ptxt:
                description_parts.append(ptxt)

    # Fallback if no structured examples were found
    if not examples:
        for t in root.find_all(string=re.compile(r"^Example", re.I)):
            label = clean_text(t)
            container = t.parent if isinstance(t, NavigableString) else t
            pre = container.find_next("pre") if isinstance(container, Tag) else None
            if pre:
                ex_text = clean_text(pre.get_text())
                ex_raw = pre.decode_contents()
            else:
                ex_text, ex_raw = "", ""
            examples.append((label if label.endswith(":") else label + ":", ex_text, ex_raw))

    return "\n\n".join(description_parts), examples

# --------------------------
# Markdown
# --------------------------

def render_markdown(meta: Dict) -> str:
    """
    meta keys:
      - number: Optional[int]
      - title: str
      - difficulty: Optional[str]
      - companies: List[str]
      - url: str
      - description: str
      - examples: List[Tuple[label, text, raw_html]]
      - solution_link: Optional[str]
    """
    number = meta.get("number")
    title = meta.get("title") or "Untitled"
    difficulty = meta.get("difficulty") or "Unknown"
    companies = meta.get("companies") or []
    url = meta.get("url") or ""
    solution_link = meta.get("solution_link")

    header_title = f"{number}. {title}" if number is not None else title

    fm = [
        "---",
        f'problem_number: {number if number is not None else "null"}',
        f'title: "{md_escape_inline(title)}"',
        f'difficulty: "{difficulty}"',
        "companies: [" + ", ".join(f'"{md_escape_inline(c)}"' for c in companies) + "]",
        f'source: "{url}"',
        f'solution_link: "{solution_link or ""}"',
        "---",
        "",
        f"# {header_title}",
        "",
    ]

    desc = (meta.get("description") or "").strip()
    if desc:
        fm += ["## Description", "", desc, ""]

    if solution_link:
        fm += [
            "## Problem Solution",
            "",
            f"[Open solution]({solution_link})",
            "",
        ]

    examples = meta.get("examples") or []
    if examples:
        fm += ["## Examples", ""]
        for i, (label, ex_text, ex_raw) in enumerate(examples, 1):
            fm += [f"### {label}", "", "```", ex_text or "", "```", ""]
            # include raw html for fidelity
            if ex_raw:
                fm += [f"#### {label} (raw HTML)", "", "```html", ex_raw, "```", ""]

    fm.append("> _This Markdown was generated for personal study from leetcode.ca_")
    return "\n".join(fm).strip() + "\n"

# --------------------------
# Orchestration
# --------------------------

def fetch_and_parse_problem(session: requests.Session, url: str) -> Optional[Dict]:
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"[WARN] Failed to GET {url}: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    number, title = extract_title_and_number(soup)
    difficulty = extract_difficulty(soup)
    companies = extract_company_tags(soup)
    description, examples = extract_description_and_examples(soup)
    solution_link = extract_problem_solution_link(soup)

    return {
        "number": number,
        "title": title,
        "difficulty": difficulty,
        "companies": companies,
        "url": url,
        "description": description,
        "examples": examples,
        "solution_link": solution_link,
    }

def output_filename(meta: Dict, out_dir: str) -> str:
    number = meta.get("number")
    title = meta.get("title") or "untitled"
    slug = slugify(title)
    if number is not None:
        name = f"{number:04d}-{slug}.md"
    else:
        name = f"{slug}.md"
    return os.path.join(out_dir, name)

def scrape_all(out_dir: str, max_workers: int = 8, polite_delay: float = 0.4, limit: Optional[int] = None):
    ensure_dir(out_dir)
    session = make_session()

    print(f"[INFO] Fetching problem index: {ALL_URL}")
    try:
        res = session.get(ALL_URL, timeout=30)
        res.raise_for_status()
    except Exception as e:
        print(f"[ERROR] Could not fetch index: {e}")
        return

    problem_links = parse_all_links(res.text)
    if limit:
        problem_links = problem_links[:limit]
    print(f"[INFO] Found {len(problem_links)} candidate problem links.")

    created = skipped = 0

    def worker(url: str) -> Tuple[str, Optional[str]]:
        meta = fetch_and_parse_problem(session, url)
        if not meta:
            return (url, None)
        fname = output_filename(meta, out_dir)
        if os.path.exists(fname):
            return (url, "skipped")
        md = render_markdown(meta)
        with open(fname, "w", encoding="utf-8") as f:
            f.write(md)
        time.sleep(polite_delay)
        return (url, fname)

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(worker, u) for u in problem_links]
        for fut in as_completed(futures):
            url, result = fut.result()
            if result is None:
                print(f"[WARN] Failed: {url}")
            elif result == "skipped":
                skipped += 1
            else:
                created += 1
                print(f"[OK]  {result}")

    print(f"[DONE] Created: {created}, Skipped (exists): {skipped}, Total links: {len(problem_links)}")

# --------------------------
# CLI
# --------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="./leetcode_problems", help="Output folder for Markdown files")
    ap.add_argument("--max-workers", type=int, default=8, help="Parallel workers")
    ap.add_argument("--polite-delay", type=float, default=0.4, help="Delay (seconds) after each problem page")
    ap.add_argument("--limit", type=int, default=None, help="Limit number of problems (debug)")
    args = ap.parse_args()

    scrape_all(args.out, max_workers=args.max_workers, polite_delay=args.polite_delay, limit=args.limit)

if __name__ == "__main__":
    main()
