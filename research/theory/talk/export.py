#!/usr/bin/env python3
"""
Export mentions.csv to theory-papers.jsonl for the concordance viewer.

One JSON object per paper:
  id, author, year, venue, title, tag, plink_url, mentions[]

Each mention: left, right, match, tag (only if set)

Usage:
    python export.py [-csv mentions.csv] [-o ../../assets/theory-papers.jsonl]
"""

import argparse
import json
import math
import re
from pathlib import Path

import pandas as pd

_PUNCT     = re.compile(r'\s+([.,;:!?)\]])')
_OPEN      = re.compile(r'([\(\["])\s+')
_RQUOTE    = re.compile(r"\s+('')")   # space before closing ''
_LQUOTE    = re.compile(r"(``)\s+")   # space after opening ``

_HTML_ARTIFACTS = re.compile(r'\s*<?\b(br|nbsp|amp|lt|gt)\b>?\s*$', re.IGNORECASE)

def clean_title(s):
    if not isinstance(s, str):
        return s
    s = _HTML_ARTIFACTS.sub('', s).strip()
    return s


def fix_punct(s):
    if not isinstance(s, str):
        return s
    s = _PUNCT.sub(r'\1', s)
    s = _OPEN.sub(r'\1', s)
    s = _RQUOTE.sub(r'\1', s)
    s = _LQUOTE.sub(r'\1', s)
    return s


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-csv", default="mentions.csv")
    parser.add_argument("-o", default="../../assets/theory-papers.jsonl")
    return parser.parse_args()


def clean(val):
    if val is None:
        return None
    if isinstance(val, float) and math.isnan(val):
        return None
    return val


def load_s2_ids(cache_path="cache/s2_ids.jsonl"):
    s2 = {}
    p = Path(cache_path)
    if not p.exists():
        return s2
    with open(p) as f:
        for line in f:
            line = line.strip()
            if line:
                obj = json.loads(line)
                if obj.get("s2_id"):
                    s2[obj["plink_id"]] = obj["s2_id"]
    return s2


def norm_title(t):
    if not isinstance(t, str):
        return ""
    t = t.lower().strip()
    t = re.sub(r'\s*\(\d+\)\s*$', '', t)   # trailing "(1)", "(2)" etc
    t = re.sub(r'\d+\s*$', '', t)           # trailing bare numbers
    return re.sub(r'\W+', '', t)


def dedup_plinks(df):
    """Keep one plink_id per paper (normalized title). Prefer tagged > most mentions."""
    meta = (df.groupby("plink_id")
              .agg(title=("title", "first"),
                   paper_tag=("paper tag", "first"),
                   n_mentions=("match", "count"))
              .reset_index())
    meta["_norm"] = meta["title"].apply(norm_title)
    meta = meta[meta["_norm"] != ""]

    def best(group):
        tagged = group[group["paper_tag"].notna() & (group["paper_tag"] != "")]
        pool = tagged if not tagged.empty else group
        return pool.sort_values("n_mentions", ascending=False).iloc[0]["plink_id"]

    keep = meta.groupby("_norm").apply(best, include_groups=False).values
    return df[df["plink_id"].isin(keep)]


def _build_meta_lookup(base_dir: Path) -> dict:
    """Returns {plink_id: {title, author, year, venue}} from CSV sources."""
    import re as _re
    lookup = {}
    sources = list(base_dir.glob("data/*.csv")) + [base_dir / "filtered_ft50.csv"]

    def normalize_source(s):
        if not isinstance(s, str): return ""
        s = s.strip().upper()
        s = _re.sub(r"\s*\([^)]*\)\s*$", "", s).strip()
        return {"MIS QUARTERLY": "MISQ", "INFORMATION SYSTEMS RESEARCH": "ISR"}.get(s, s)

    for src in sources:
        if not src.exists():
            continue
        try:
            df = pd.read_csv(src)
        except Exception:
            continue
        for _, row in df.iterrows():
            year_match = _re.search(r"((?:19|20)\d{2})", str(row.get("publicationDate", "")))
            meta = {
                "title": clean_title(row.get("title", "")),
                "author": str(row.get("contributors", "")).replace(" ; ", ", "),
                "year": int(year_match.group(1)) if year_match else None,
                "venue": normalize_source(row.get("source", "")),
            }
            for plink in str(row.get("all_plinks", row.get("plink", ""))).split("|"):
                pid = plink.strip().rstrip("/").split("/")[-1]
                if pid and pid not in lookup:
                    lookup[pid] = meta
    return lookup


def _build_title_lookup(base_dir: Path) -> dict:
    return {pid: m["title"] for pid, m in _build_meta_lookup(base_dir).items()}


def validate(df):
    errors = []
    per_paper = df.groupby("plink_id").first().reset_index()
    passing = per_paper[per_paper["paper tag"] == "Theory in passing"]
    bad = passing[passing["dsr_method"].notna() & (passing["dsr_method"] != "")]
    for _, row in bad.iterrows():
        errors.append(f"  dsr_method should be None for '{row['title']}' (paper tag='Theory in passing', got '{row['dsr_method']}')")
    if errors:
        raise ValueError("Validation errors:\n" + "\n".join(errors))


def main():
    args = parse_args()
    df_raw = pd.read_csv(args.csv)
    str_cols = df_raw.select_dtypes(include="object").columns
    df_raw[str_cols] = df_raw[str_cols].apply(lambda c: c.str.strip())
    df = dedup_plinks(df_raw)
    validate(df_raw)
    s2_ids = load_s2_ids()

    out_path = Path(args.o)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    EXCLUDE_TAGS = {"Out of scope"}

    papers = []
    for plink_id, group in df.groupby("plink_id", sort=False):
        row0 = group.iloc[0]

        explicit_tag = clean(row0.get("paper tag"))
        if explicit_tag in EXCLUDE_TAGS:
            continue
        has_mentions = len(group) > 0 and any(clean(m["match"]) for _, m in group.iterrows())
        paper_tag = explicit_tag if explicit_tag else ("No theory" if not has_mentions else "Untagged")

        mentions = []
        for idx, (_, m) in enumerate(group.iterrows()):
            mention = {
                "mid": idx,
                "sec": clean(m.get("section_name")) or "",
                "left": fix_punct(clean(m["context_left"]) or "").rstrip(),
                "match": clean(m["match"]) or "theory",
                "right": fix_punct(clean(m["context_right"]) or "").lstrip(),
            }
            mtag = clean(m.get("mention tag"))
            if mtag:
                mention["tag"] = mtag
            mentions.append(mention)

        # format author: last name of first author
        author = (clean(row0.get("author")) or "").replace(" ; ", ", ")

        s2_id = s2_ids.get(plink_id)
        s2_url = f"https://www.semanticscholar.org/paper/{s2_id}" if s2_id else None

        papers.append({
            "id": plink_id,
            "author": author,
            "year": int(row0["year"]) if pd.notna(row0["year"]) else None,
            "venue": clean(row0.get("venue")) or "",
            "title": clean_title(clean(row0.get("title")) or ""),
            "tag": paper_tag,
            "dsr_method": [m.strip() for m in (clean(row0.get("dsr_method")) or "").split(";") if m.strip() and m.strip().lower() != "x"],
            "approach": clean(row0.get("approach")) or ("No theory" if paper_tag == "No theory" else None),
            "orientation": clean(row0.get("orientation")),
            "plink_url": f"https://research.ebsco.com/plink/{plink_id}",
            "s2_url": s2_url,
            "mentions": mentions,
        })

    # add papers from no_theory_papers.csv (explicit no-theory registry)
    no_theory_path = Path(args.csv).parent / "no_theory_papers.csv"
    if no_theory_path.exists():
        in_csv = set(df_raw["plink_id"])
        nt_df = pd.read_csv(no_theory_path)
        for _, row in nt_df.iterrows():
            pid = str(row["id"]).strip()
            if pid in in_csv:
                continue
            papers.append({
                "id": pid,
                "author": str(row.get("author", "") or ""),
                "year": int(row["year"]) if pd.notna(row.get("year")) else None,
                "venue": str(row.get("venue", "") or ""),
                "title": clean_title(str(row.get("title", "") or "")),
                "tag": "No theory",
                "dsr_method": [],
                "approach": "No theory",
                "orientation": None,
                "plink_url": str(row.get("plink_url", "") or f"https://research.ebsco.com/plink/{pid}"),
                "s2_url": str(row["s2_url"]) if pd.notna(row.get("s2_url")) and row.get("s2_url") else None,
                "mentions": [],
            })

    # sort by year then author
    papers.sort(key=lambda p: (p["year"] or 0, p["author"]))

    def sorted_vals(col):
        return sorted({p[col] for p in papers if p[col]})

    def sorted_vals_list(col):
        vals = set()
        for p in papers:
            for v in (p[col] if isinstance(p[col], list) else []):
                if v:
                    vals.add(v)
        return sorted(vals)

    meta = {
        "_meta": True,
        "methods": sorted_vals_list("dsr_method"),
        "approaches": sorted_vals("approach"),
        "orientations": sorted_vals("orientation"),
    }

    all_lines = [meta] + papers

    with open(out_path, "w") as f:
        for obj in all_lines:
            f.write(json.dumps(obj) + "\n")

    print(f"Wrote {len(papers)} papers -> {out_path}")

    # embed data into theory-concordance.html
    html_path = out_path.parent / "theory-concordance.html"
    if html_path.exists():
        html = html_path.read_text()
        embedded = "window.__EMBEDDED_DATA__ = " + json.dumps(all_lines) + ";"
        start_marker = "// __EMBEDDED_DATA_START__"
        end_marker   = "// __EMBEDDED_DATA_END__"
        start_idx = html.index(start_marker)
        end_idx   = html.index(end_marker) + len(end_marker)
        html = html[:start_idx] + start_marker + "\n" + embedded + "\n" + end_marker + html[end_idx:]
        html_path.write_text(html)
        print(f"Embedded data -> {html_path}")

    tag_counts = {}
    for p in papers:
        tag_counts[p["tag"]] = tag_counts.get(p["tag"], 0) + 1
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {count:>4}  {tag}")

    untagged = [p for p in papers if p["tag"] == "Untagged"]
    if untagged:
        print(f"\nUntagged ({len(untagged)}):")
        for p in sorted(untagged, key=lambda p: len(p["mentions"])):
            print(f"  ({len(p['mentions'])})  {p['title']}")



if __name__ == "__main__":
    main()
