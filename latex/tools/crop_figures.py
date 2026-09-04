#!/usr/bin/env python3
"""
crop_figures.py -- list or crop the figures of a page of the book PDF.

  python crop_figures.py BOOK.pdf list PAGE
      prints the candidate figure rectangles (PDF points) found on PAGE
  python crop_figures.py BOOK.pdf crop PAGE x0 y0 x1 y1 OUT.png [DPI]
      renders that rectangle of PAGE to OUT.png (default 300 dpi)
"""
import sys, fitz

def candidates(page):
    H = page.rect.height
    boxes = []
    for d in page.get_drawings():
        r = d["rect"]
        if r.width < 15 or r.height < 15: continue
        if r.y0 < 60 or r.y1 > H - 40: continue
        boxes.append(fitz.Rect(r))
    for img in page.get_image_info():
        boxes.append(fitz.Rect(img["bbox"]))
    changed = True
    while changed:
        changed = False
        merged = []
        for r in boxes:
            for m in merged:
                if m.intersects(r) or (abs(m.x0 - r.x0) < 30 and abs(m.y1 - r.y0) < 30):
                    m |= r; changed = True; break
            else:
                merged.append(fitz.Rect(r))
        boxes = merged
    return [m for m in boxes if m.width > 40 and m.height > 40]

def main():
    book, cmd, page_no = sys.argv[1], sys.argv[2], int(sys.argv[3])
    doc = fitz.open(book)
    page = doc[page_no - 1]
    if cmd == "list":
        for r in candidates(page):
            print(f"{r.x0:7.1f} {r.y0:7.1f} {r.x1:7.1f} {r.y1:7.1f}   ({r.width:.0f} x {r.height:.0f} pt)")
    elif cmd == "crop":
        x0, y0, x1, y1 = map(float, sys.argv[4:8])
        out = sys.argv[8]
        dpi = int(sys.argv[9]) if len(sys.argv) > 9 else 300
        page.get_pixmap(dpi=dpi, clip=fitz.Rect(x0, y0, x1, y1)).save(out)
        print("wrote", out)

if __name__ == "__main__":
    main()
