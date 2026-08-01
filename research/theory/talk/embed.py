#!/usr/bin/env python3
"""
Embed theory-papers.jsonl into the __EMBEDDED_DATA__ block of theory-concordance.html.

Usage:
    python embed.py [-jsonl PATH] [-html PATH]
"""
import argparse
import json
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-jsonl", default="assets/theory-papers.jsonl")
    parser.add_argument("-html",  default="assets/theory-concordance.html")
    return parser.parse_args()


def main():
    args = parse_args()
    jsonl_path = Path(args.jsonl)
    html_path  = Path(args.html)

    lines = [json.loads(l) for l in jsonl_path.read_text().strip().split("\n") if l.strip()]

    html = html_path.read_text()
    blob = "window.__EMBEDDED_DATA__ = " + json.dumps(lines) + ";"
    start_marker = "// __EMBEDDED_DATA_START__"
    end_marker   = "// __EMBEDDED_DATA_END__"
    si = html.index(start_marker)
    ei = html.index(end_marker) + len(end_marker)
    html_path.write_text(html[:si] + start_marker + "\n" + blob + "\n" + end_marker + html[ei:])
    print(f"Embedded {len(lines)} records into {html_path}")


if __name__ == "__main__":
    main()
