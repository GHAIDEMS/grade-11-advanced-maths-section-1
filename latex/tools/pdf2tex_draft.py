#!/usr/bin/env python3
"""
pdf2tex_draft.py -- turn a page range of Additional-Maths-book-2.pdf into a *draft*
LaTeX transcript, using the PDF's font information as a guide.

The book is an InDesign export: prose is STIX Regular, variables are STIX Italic,
headings are Source Sans Pro Bold, and equations were set with the InMath plug-in
(which leaves private-use control glyphs behind and flattens fractions into three
lines: numerator / "__" / denominator).  The draft therefore gets the prose right
and marks the maths for hand re-typesetting from the rendered page.

Usage:  python pdf2tex_draft.py BOOK.pdf FIRST LAST > draft.tex   (1-based PDF pages)
"""
import sys, re, fitz

SYM = {
    "\u222a": r"\cup ", "\u2229": r"\cap ", "\u2032": "'", "\u2033": "''",
    "\u2212": "-", "\u00d7": r"\times ", "\u00f7": r"\div ", "\u2264": r"\le ", "\u2265": r"\ge ",
    "\u2260": r"\ne ", "\u221a": r"\sqrt", "\u03c0": r"\pi ", "\u221e": r"\infty ",
    "\u2192": r"\to ", "\u21d2": r"\Rightarrow ", "\u21d4": r"\Leftrightarrow ", "\u2211": r"\sum ",
    "\u222b": r"\int ", "\u2208": r"\in ", "\u2209": r"\notin ", "\u2282": r"\subset ", "\u2286": r"\subseteq ",
    "\u2205": r"\varnothing ", "\u00b1": r"\pm ", "\u2213": r"\mp ", "\u00b0": r"^{\circ}",
    "\u03b1": r"\alpha ", "\u03b2": r"\beta ", "\u03b8": r"\theta ", "\u03bc": r"\mu ", "\u03b5": r"\varepsilon ",
    "\u03bb": r"\lambda ", "\u03c3": r"\sigma ", "\u03a3": r"\Sigma ", "\u0394": r"\Delta ", "\u03b4": r"\delta ",
    "\u03c6": r"\phi ", "\u03c9": r"\omega ", "\u03b3": r"\gamma ", "\u2234": r"\therefore ", "\u2026": r"\ldots ",
    "\u2019": "'", "\u2018": "`", "\u201c": "``", "\u201d": "''", "\u2013": "--", "\u2014": "---",
    "\u00a0": " ", "\u2007": " ", "\u202f": " ", "\u200a": " ", "\u200b": "", "\u2009": " ", "\t": " ",
    "\u2248": r"\approx ", "\u2261": r"\equiv ", "\u2200": r"\forall ", "\u2203": r"\exists ",
    "\u00b2": "^{2}", "\u00b3": "^{3}", "\u00bd": r"\tfrac12 ", "\u00bc": r"\tfrac14 ", "\u00be": r"\tfrac34 ",
    "\u2225": r"\parallel ", "\u22a5": r"\perp ", "\u2220": r"\angle ", "\u25b3": r"\triangle ",
    "\u2044": "/", "\u2022": r"\item ", "\uf0b7": r"\item ",
}
TEX_ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde ", "^": r"\^{}"}

def clean(s, math=False):
    out = []
    for ch in s:
        o = ord(ch)
        if 0xE000 <= o <= 0xF8FF:          # InMath control glyphs
            continue
        if ch in SYM:
            out.append(SYM[ch]); continue
        if not math and ch in TEX_ESC:
            out.append(TEX_ESC[ch]); continue
        out.append(ch)
    return "".join(out)

def font_kind(name):
    n = name.split("+")[-1]
    if "SourceSansPro" in n:
        return "head" if ("Bold" in n or "Semibold" in n) else "sans"
    if "Italic" in n or "BoldItalic" in n:
        return "ital"
    if "Bold" in n:
        return "bold"
    return "roman"

def render_line(line, base_size):
    """Join the spans of one text line into a draft LaTeX string."""
    parts = []
    base_y = None
    for sp in line["spans"]:
        if base_y is None and font_kind(sp["font"]) in ("roman", "ital", "bold"):
            base_y = sp["origin"][1]
    for sp in line["spans"]:
        txt = sp["text"]
        if not txt.strip():
            parts.append(" "); continue
        kind = font_kind(sp["font"])
        size = sp["size"]
        y = sp["origin"][1]
        small = size < base_size * 0.8
        raised = base_y is not None and (base_y - y) > size * 0.25
        lowered = base_y is not None and (y - base_y) > size * 0.15
        if kind == "ital":
            body = clean(txt, math=True).strip()
            s = f"${body}$"
        elif kind == "bold":
            s = r"\textbf{" + clean(txt).strip() + "}"
        elif kind == "head":
            s = clean(txt)
        else:
            s = clean(txt)
        if small and raised:
            s = "^{" + s.strip() + "}"
        elif small and lowered:
            s = "_{" + s.strip() + "}"
        parts.append(s)
    return re.sub(r"[ ]{2,}", " ", "".join(parts)).strip()

def page_lines(page):
    W, H = page.rect.width, page.rect.height
    d = page.get_text("dict")
    lines = []
    for b in d["blocks"]:
        if b["type"] != 0:
            lines.append({"y": b["bbox"][1], "x": b["bbox"][0], "kind": "image", "text": f"%% [IMAGE {b['bbox']}]", "size": 0})
            continue
        for l in b["lines"]:
            y0 = l["bbox"][1]
            if y0 < 48 or y0 > H - 45:        # running header / footer
                continue
            spans = [s for s in l["spans"] if s["text"].strip()]
            if not spans:
                continue
            kinds = [font_kind(s["font"]) for s in spans]
            sizes = [s["size"] for s in spans]
            base = max(set(sizes), key=sizes.count)
            kind = "head" if all(k == "head" for k in kinds) else "text"
            lines.append({"y": y0, "x": l["bbox"][0], "kind": kind, "size": base,
                          "text": render_line(l, base)})
    lines.sort(key=lambda r: (round(r["y"] / 3), r["x"]))
    return lines

HEAD_RE = re.compile(r"^(Example \d+\.\d+|Solution|Activity \d+\.\d+.*|Key Ideas|KEY IDEAS|Review Questions|REVIEW QUESTIONS|Extended Reading|EXTENDED READING|Part [A-Z]|Part \d)\b", re.I)

def emit_page(page, pno):
    out = [f"%% ================= PDF p.{pno} =================="]
    prev_kind = None
    for r in page_lines(page):
        t = r["text"]
        if r["kind"] == "image":
            out.append(t); prev_kind = "image"; continue
        if r["kind"] == "head":
            m = HEAD_RE.match(t)
            tag = "ENV" if m else "HEADING"
            out.append(f"\n%% {tag} ({r['size']:.0f}pt): {t}")
            prev_kind = "head"; continue
        if t == "__" or t.startswith("__"):
            out.append("%% [fraction bar]"); continue
        out.append(t)
        prev_kind = "text"
    return "\n".join(out)

def main():
    book, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    doc = fitz.open(book)
    chunks = [emit_page(doc[p - 1], p) for p in range(first, last + 1)]
    sys.stdout.write("\n\n".join(chunks) + "\n")

if __name__ == "__main__":
    main()
