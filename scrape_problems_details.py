import os
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

PROBLEMS_DIR = "problems"
DETAILS_DIR = "problems_details"
os.makedirs(DETAILS_DIR, exist_ok=True)

def get_leetcode_ca_url(md_path):
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("leetcode_ca_url:"):
                return line.split(":", 1)[1].strip()
    return None

def parse_problem_page(url):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"
    # Description and Examples
    root = soup.select_one(".markdown-body") or soup
    description_parts = []
    examples = []
    found_example = False
    example_lines = []
    for node in root.stripped_strings:
        if not found_example:
            if "Example:" in node:
                found_example = True
                example_lines.append(node)
            else:
                description_parts.append(node)
        else:
            # Stop if a new section starts (e.g., "Difficulty:", "Company:", etc.)
            if node.startswith("Difficulty:") or node.startswith("Company:") or node.startswith("Lock:"):
                break
            example_lines.append(node)
    if example_lines:
        # Join all example lines as one block
        examples.append(("Example", "\n".join(example_lines)))
    description_md = "\n\n".join(description_parts)
    # Company tags
    companies = []
    for div in soup.find_all("div"):
        h3 = div.find("h3")
        if h3 and h3.get_text(strip=True).lower().startswith("company"):
            for a in div.select("a"):
                txt = a.get_text(strip=True)
                if txt:
                    companies.append(txt)
    return title, description_md.strip(), examples, companies

def write_details_md(filename, title, desc, examples, companies, url):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Source:** [{url}]({url})\n\n")
        if companies:
            f.write("**Companies:** " + ", ".join(companies) + "\n\n")
        f.write("## Description\n\n")
        f.write(desc + "\n\n")
        if examples:
            f.write("## Examples\n\n")
            for ex_title, ex_code in examples:
                f.write(f"### {ex_title}\n\n")
                f.write("```\n" + ex_code + "\n```\n\n")

def process_file(fname):
    md_path = os.path.join(PROBLEMS_DIR, fname)
    url = get_leetcode_ca_url(md_path)
    if not url:
        return f"URL not found in {fname}"
    try:
        title, desc, examples, companies = parse_problem_page(url)
        out_path = os.path.join(DETAILS_DIR, fname)
        write_details_md(out_path, title, desc, examples, companies, url)
        return f"Processed: {fname}"
    except Exception as e:
        return f"Error processing {fname}: {e}"

if __name__ == "__main__":
    files = [f for f in os.listdir(PROBLEMS_DIR) if f.endswith(".md")]
    max_workers = 6  # You can adjust this number
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_file, fname): fname for fname in files}
        for future in as_completed(futures):
            print(future.result())