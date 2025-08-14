#!/usr/bin/env python3
"""
merge_md.py — Concatenate Markdown files into a single .md file.

Usage examples:
  # Recursively merge all .md files under a folder, sorted by name
  python merge_md.py "C:\\Users\\you\\path\\to\\folder" -r -o combined.md

  # Non-recursive, sorted by modification time, add H2 headers for each file
  python merge_md.py ./notes --sort mtime --header-level 2 -o all.md
"""

from __future__ import annotations
import argparse
from pathlib import Path
import fnmatch
import sys
from datetime import datetime

def gather_files(root: Path, pattern: str, recursive: bool, exclude: list[str], output: Path) -> list[Path]:
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Input directory not found or not a directory: {root}")

    candidates = root.rglob(pattern) if recursive else root.glob(pattern)
    files = []
    for p in candidates:
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        # Exclude patterns (match against both relative path and name)
        skip = any(
            fnmatch.fnmatch(str(rel).replace("\\", "/"), ex) or fnmatch.fnmatch(p.name, ex)
            for ex in exclude
        )
        if skip:
            continue
        # Never include the output file itself if it sits inside the tree
        try:
            if p.resolve() == output.resolve():
                continue
        except Exception:
            pass
        files.append(p)
    return files

def sort_files(files: list[Path], root: Path, mode: str) -> list[Path]:
    if mode == "none":
        return files
    if mode == "name":
        return sorted(files, key=lambda p: str(p.relative_to(root)).lower())
    if mode == "mtime":
        return sorted(files, key=lambda p: p.stat().st_mtime)
    return files

def main():
    ap = argparse.ArgumentParser(description="Concatenate Markdown files into one .md file.")
    ap.add_argument("input_dir", help="Folder containing .md files")
    ap.add_argument("-o", "--output", default="combined.md", help="Output markdown file")
    ap.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories")
    ap.add_argument("--pattern", default="*.md", help="Glob pattern to include (default: *.md)")
    ap.add_argument("--exclude", action="append", default=[], help="Glob pattern to exclude (can repeat)")
    ap.add_argument("--sort", choices=["name", "mtime", "none"], default="name", help="Sort order")
    ap.add_argument("--header-level", type=int, choices=[0,1,2,3,4,5,6], default=2,
                    help="Add a markdown header with file name before each file; 0 = no header (default: 2)")
    ap.add_argument("--no-hr", action="store_true", help="Do not insert --- between files")
    ap.add_argument("--encoding", default="utf-8", help="Text encoding for output (default: utf-8)")
    args = ap.parse_args()

    root = Path(args.input_dir).expanduser()
    out_path = Path(args.output).expanduser()

    files = gather_files(root, args.pattern, args.recursive, args.exclude, out_path)
    if not files:
        print("No markdown files found with the given options.", file=sys.stderr)
        sys.exit(1)

    files = sort_files(files, root, args.sort)

    # Write output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding=args.encoding, newline="\n") as out:
        out.write(f"<!-- Generated {datetime.now().isoformat()} by merge_md.py -->\n\n")
        for idx, p in enumerate(files):
            rel = p.relative_to(root)
            if args.header_level > 0:
                out.write(f"{'#' * args.header_level} {rel.as_posix()}\n\n")
            # Read using utf-8-sig to gracefully handle BOM if present
            text = p.read_text(encoding="utf-8-sig")
            # Ensure a single trailing newline
            if not text.endswith("\n"):
                text += "\n"
            out.write(text)
            # Separate files with a horizontal rule unless disabled or last file
            if not args.no_hr and idx != len(files) - 1:
                out.write("\n---\n\n")

    print(f"Combined {len(files)} files into: {out_path}")

if __name__ == "__main__":
    main()
