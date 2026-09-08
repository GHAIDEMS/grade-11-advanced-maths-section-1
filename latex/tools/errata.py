#!/usr/bin/env python3
"""
errata.py -- keep errata.csv and the LaTeX markers in step, and render ERRATA.md.

    python latex/tools/errata.py          # check + regenerate ERRATA.md (run from repo root)
    python latex/tools/errata.py --check  # check only, exit 1 on any mismatch

Markers in the LaTeX:
    \\booknote[S2-04]{...}        a defect kept verbatim in the text (kind = error)
    % SUGGEST S2-S01: ...         a proposed change, comment only      (kind = suggestion)

Every error row must have a \\booknote marker and every marker a row; suggestion rows need
no marker (a SUGGEST comment is optional but is reported if its id is unknown).
"""
import csv, re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV = os.path.join(ROOT, "errata.csv")
MD = os.path.join(ROOT, "ERRATA.md")
COLS = ["id", "section", "book_page", "location", "kind", "book_prints", "should_be",
        "handling", "status", "found_by", "date", "notes"]

NOTE_RE = re.compile(r"\\booknote\[([A-Z0-9-]+)\]")
SUGG_RE = re.compile(r"%\s*SUGGEST\s+([A-Z0-9-]+)\s*:")

def markers():
    found = {}
    for path in glob.glob(os.path.join(ROOT, "latex", "**", "*.tex"), recursive=True):
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        text = open(path, encoding="utf-8").read()
        for kind, rx in (("error", NOTE_RE), ("suggestion", SUGG_RE)):
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                found.setdefault(m.group(1), []).append((kind, f"{rel}:{line}"))
    return found

def rows():
    with open(CSV, encoding="utf-8", newline="") as f:
        r = list(csv.DictReader(f))
    missing = [c for c in COLS if r and c not in r[0]]
    if missing:
        sys.exit(f"errata.csv lacks columns: {missing}")
    return r

def check(rs, ms):
    problems = []
    ids = [r["id"] for r in rs]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        problems.append(f"duplicate ids in errata.csv: {sorted(dup)}")
    for r in rs:
        if r["kind"] not in ("error", "suggestion"):
            problems.append(f"{r['id']}: kind must be error or suggestion, not {r['kind']!r}")
        if r["kind"] == "error" and r["id"] not in ms:
            problems.append(f"{r['id']}: error row has no \\booknote[{r['id']}] marker in the LaTeX")
    for i, where in ms.items():
        if i not in ids:
            problems.append(f"{i}: marker at {where[0][1]} has no row in errata.csv")
    return problems

def render(rs, ms):
    out = ["# Errata and proposed changes to the printed book", "",
           "Generated from `errata.csv` by `latex/tools/errata.py`; edit the CSV, not this file.",
           "Ids `SN-kk` are errors kept verbatim in the LaTeX with a `\\booknote[id]`; `SN-Skk` are",
           "suggestions (no change made in the text).", ""]
    by_sec = {}
    for r in rs:
        by_sec.setdefault(r["section"], []).append(r)
    for sec in sorted(by_sec, key=lambda s: int(s)):
        out += [f"## Section {sec}", "",
                "| Id | Book p. | Location | Kind | The book prints | Should be / proposal | Handling | Status | Found by |",
                "|---|---|---|---|---|---|---|---|---|"]
        for r in by_sec[sec]:
            cell = lambda k: r[k].replace("|", "\\|").replace("\n", " ")
            where = ms.get(r["id"], [("", "")])[0][1]
            loc = cell("location") + (f" (`{where}`)" if where else "")
            out.append(f"| {r['id']} | {cell('book_page')} | {loc} | {cell('kind')} | {cell('book_prints')} | "
                       f"{cell('should_be')} | {cell('handling')} | {cell('status')} | {cell('found_by')} |")
        out.append("")
    return "\n".join(out)

def main():
    rs, ms = rows(), markers()
    problems = check(rs, ms)
    for p in problems:
        print("ERROR:", p)
    if "--check" not in sys.argv:
        with open(MD, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(rs, ms))
        print(f"ERRATA.md: {len(rs)} rows, {len(ms)} markers")
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
