import re
import time
import pathlib
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ALL_PAGE = "https://leetcode.ca/all/problems.html"
PER_PROBLEM_BASE = "https://leetcode.ca/all/{id}.html"

# --- helpers -----------------------------------------------------------------
def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"`|’|‘|“|”", "", s)             # remove odd quotes
    s = re.sub(r"[^a-z0-9]+", "-", s)           # non-alnum -> hyphen
    s = re.sub(r"-{2,}", "-", s).strip("-")     # collapse hyphens
    return s or "untitled"

def leetcode_dot_com_url(slug: str) -> str:
    # best-effort guess; most titles map 1:1
    return f"https://leetcode.com/problems/{slug}/"

def fetch(url: str, tries: int = 5, sleep_s: float = 1.2) -> str:
    last_err = None
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/124.0 Safari/537.36"),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://leetcode.ca/",
    }
    for i in range(tries):
        try:
            r = requests.get(url, headers=headers, timeout=30)
            if r.status_code == 200:
                return r.text
            last_err = f"HTTP {r.status_code}"
        except Exception as e:
            last_err = str(e)
        time.sleep(sleep_s * (i + 1))
    raise RuntimeError(f"Failed to GET {url}: {last_err}")

# --- scrape table -------------------------------------------------------------
def parse_all_table(html: str):
    soup = BeautifulSoup(html, "html.parser")
    tbody = soup.find("tbody")
    if not tbody:
        raise RuntimeError("Could not find problems table <tbody>.")

    problems = []
    for tr in tbody.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 4:
            continue
        id_text = tds[0].get_text(strip=True)
        title_a = tds[1].find("a")
        title = (title_a.get_text(strip=True) if title_a else tds[1].get_text(strip=True))
        href = title_a["href"] if title_a and title_a.has_attr("href") else None
        diff = tds[2].get_text(strip=True)
        lock = tds[4 - 1].get_text(strip=True)  # last column is "Lock"
        # some rows include stray words like "Image" next to titles; clean them
        title = re.sub(r"\bImage\b", "", title).strip()

        try:
            pid = int(re.sub(r"[^\d]", "", id_text))
        except ValueError:
            continue

        problems.append({
            "id": pid,
            "title": title,
            "href": href,          # like "21.html"
            "difficulty": diff,
            "lock": lock,
        })
    return problems

# --- file writing -------------------------------------------------------------
MD_TEMPLATE = """--- 
id: {id}
title: "{title}"
slug: {slug}
difficulty: {difficulty}
lock: {lock}
source: leetcode.ca
leetcode_ca_url: {leetcode_ca_url}
leetcode_url: {leetcode_url}
---

# {id}. {title}

**Links:** [{title} @ leetcode.ca]({leetcode_ca_url}) · [{title} @ leetcode.com]({leetcode_url})

## Notes
- TODO: Approach
- TODO: Time / Space Complexity
"""

def main():
    repo_root = Path(r"C:\Users\wboum\source\leetcode").resolve()
    out_dir = repo_root / "problems"
    out_dir.mkdir(parents=True, exist_ok=True)

    html = fetch(ALL_PAGE)
    problems = parse_all_table(html)
    problems.sort(key=lambda p: p["id"])

    count_new = 0
    for p in problems:
        slug = slugify(p["title"])
        fname = f"{p['id']:04d}-{slug}.md"
        path = out_dir / fname

        if path.exists():
            continue

        leet_ca_url = (PER_PROBLEM_BASE.format(id=p["id"])
                       if not (p["href"] and p["href"].startswith("http"))
                       else p["href"])
        leet_com_url = leetcode_dot_com_url(slug)

        md = MD_TEMPLATE.format(
            id=p["id"],
            title=p["title"].replace('"', '\\"'),
            slug=slug,
            difficulty=p["difficulty"],
            lock=p["lock"],
            leetcode_ca_url=leet_ca_url,
            leetcode_url=leet_com_url,
        )
        path.write_text(md, encoding="utf-8")
        count_new += 1

    print(f"Wrote {count_new} new files into {out_dir}")
    print("Done.")

if __name__ == "__main__":
    main()
