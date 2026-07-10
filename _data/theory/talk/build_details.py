#!/usr/bin/env python3
"""
Build details.jsonl.gz: expanded context (±N words) for each mention.

For each mention in mentions.csv, finds the matching position in the GROBID
section text and extracts a wider window of words around it.

Output: one JSON object per mention:
  { "id": "<plink_id>:<mid>", "ctx": "<expanded context>" }

Usage:
    python build_details.py [-csv mentions.csv] [-json json/] [-o ../../assets/theory-details.jsonl.gz] [-window 100]
"""

import argparse
import gzip
import json
import re
from pathlib import Path

import pandas as pd

PATTERN = re.compile(r'^theor', re.IGNORECASE)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-csv",    default="mentions.csv")
    p.add_argument("-json",   default="json/")
    p.add_argument("-o",      default="../../../assets/theory-details.jsonl.gz")
    p.add_argument("-window", type=int, default=100)
    return p.parse_args()


def load_sections(json_dir: Path) -> dict:
    """Returns {plink_id: [(section_name, words[])]}"""
    sections = {}
    for path in sorted(json_dir.glob("*.jsonl")):
        pid = path.stem
        secs = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                text = re.sub(r'\s+', ' ', obj.get("section_text", "")).strip()
                words = text.split()
                secs.append((obj.get("section_name", ""), words))
        sections[pid] = secs
    return sections


def find_mention(sections, plink_id: str, section_name: str, left: str, match: str, right: str) -> tuple[list, int] | None:
    """Find the word index of `match` in the section, guided by surrounding context."""
    secs = sections.get(plink_id, [])
    left_tail = left.split()[-3:] if left else []
    right_head = right.split()[:3] if right else []

    for sname, words in secs:
        if section_name and sname != section_name:
            continue
        for i, w in enumerate(words):
            if not PATTERN.match(w):
                continue
            if w.lower() != match.lower():
                continue
            # check left context
            if left_tail:
                pre = [ww.lower().strip('.,;:()[]"\'') for ww in words[max(0, i - len(left_tail)):i]]
                if not any(lt.lower().strip('.,;:()[]"\'') in pre for lt in left_tail):
                    continue
            return words, i
    return None


def main():
    args = parse_args()
    W = args.window
    json_dir = Path(args.json)
    out_path = Path(args.o)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.csv)
    sections = load_sections(json_dir)

    records = []
    hits = misses = 0

    for plink_id, group in df.groupby("plink_id", sort=False):
        for mid, (_, row) in enumerate(group.iterrows()):
            left  = str(row.get("context_left")  or "")
            match = str(row.get("match")          or "theory")
            right = str(row.get("context_right")  or "")
            sname = str(row.get("section_name")   or "")

            result = find_mention(sections, plink_id, sname, left, match, right)
            if result is None:
                misses += 1
                continue

            words, pos = result
            window_words = words[max(0, pos - W): pos + W + 1]
            # bold the match word with simple marker
            rel = pos - max(0, pos - W)
            window_words[rel] = f"**{window_words[rel]}**"
            ctx = " ".join(window_words)

            records.append({"id": f"{plink_id}:{mid}", "ctx": ctx})
            hits += 1

    with gzip.open(out_path, "wt", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

    print(f"Wrote {len(records)} detail records -> {out_path}")
    print(f"  hits={hits}  misses={misses}")


if __name__ == "__main__":
    main()
