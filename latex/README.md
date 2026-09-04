# LaTeX transcription of *Additional Mathematics for Senior High Schools, Year 2*

Source: the book PDF (Ministry of Education / Mathematics Association of Ghana, 2025;
InDesign export, 481 pp.), which is **not** in this repository — the book's front matter says
*all rights reserved, no reproduction without written permission*, so only the transcription
is committed, never the PDF or page scans.

## Status

| Book section | Folder | Pages (book) | State |
|---|---|---|---|
| 1 Sets and Binomial Expansions | `section01/` | 7–48 | Santiago's transcription (upload of 2026-08-27, moved here from `section1-latex/` on 2026-09-04); `answers.tex` added 2026-09-04 |
| 2 Sequences and Inequalities | `section02/` | 49–87 | transcribed 2026-09-04, with answers (book pp. 452–453) |
| 3–14 | — | 88–447 | not started |

`book.tex` builds the whole book (one `report` chapter per book Section, answers as an
unnumbered chapter at the end).  Each `sectionNN/main.tex` builds that Section on its own.

Section 1's `answers.tex` is the book's answer key for Section 1 (pp. 448–452), which the
original transcription lacked, with its five Venn diagrams cropped from the PDF into
`section01/figures/ans-*.png`.  `book.tex` includes the answers; `section01/main.tex` does
not, so `section01/main.pdf` (the compiled Section 1 committed with the original upload)
is still an exact build of it.  Section 1 also keeps its own `section01/preamble.tex`, so it
compiles standalone exactly as before; `book.tex` and `section02/main.tex` use the shared
`preamble.tex`.

## Building

A TeX distribution is needed (tested with MiKTeX 25.12, packages auto-install).  No
`latexmk` yet.

```
cd latex && pdflatex book && pdflatex book          # whole book
cd latex/section02 && pdflatex main && pdflatex main # one section
```

Build products (`*.pdf`, `*.aux`, …) are git-ignored; `section01/main.pdf` is the one
committed exception, kept from the original upload.

## Conventions (inherited from the Section 1 files)

- `preamble.tex` is shared and is a superset of Section 1's own `section01/preamble.tex`:
  the same `keyideas`, `activity{title}` and `example{title}` tcolorbox environments and the
  same Venn-diagram macros, so the Section 1 files compile unchanged under either.  Added in
  the shared one: `\solution`, `\figcaption{n.m}{text}`, `\booknote{...}`, `\cedi`, pgfplots,
  booktabs.
- **Verbatim transcription.**  The book's wording, numbering, typos and arithmetic slips are
  kept; a slip that would mislead a reader gets a `\booknote{}` (italic, in parentheses)
  saying what the book prints and what was meant — the Section 1 practice.  Section 2 carries
  10 such notes.
- Headings: the book's red capitals (strand topics) are `\section`, the pink sub-heads
  `\subsection`; the strand/sub-strand line at the top of a Section is `\section*`/`\subsection*`.
- Review Questions are `\section*{Review Questions}` + one `\item` per book question, with
  the book's own numbering (Section 2's Q13/14 and Q16–18 are single problems the book
  splits).  Answers sit in `sectionNN/answers.tex` with the answer key's own numbering.
- Figures: screenshots (GeoGebra graphs, Excel) are cropped from the PDF at 200 dpi with
  `tools/crop_figures.py` into `sectionNN/figures/` (JPEG when the PNG is over ~0.5 MB);
  simple diagrams — number lines, parabolas, the necklace curves — are redrawn in TikZ/pgfplots.
  Use `\linewidth`, not `\textwidth`, for widths (the boxes are narrower than the page).
- One file per book topic under `sectionNN/sections/`, each headed by a comment giving the
  book and PDF page range it covers.

## Workflow that produced Section 2 (per section, ~40 book pages)

1. `python tools/pdf2tex_draft.py BOOK.pdf FIRST LAST > draft.tex` —
   uses the PDF's fonts (STIX Italic = variable, Source Sans Bold = heading, InMath control
   glyphs = equation) to give a draft with the prose right and the maths flattened.
2. Render the pages (`fitz`, 130 dpi) and re-typeset every equation from the image; the draft
   is only a reading aid for the prose.
3. `python tools/crop_figures.py BOOK.pdf list PAGE` / `crop ...` for the figures.
4. Compile after every few pages; the first compile of Section 2 caught a systematic
   corruption (every `\\` lost by the shell), so compile early.

Section 2 came to 1 650 lines of LaTeX, 7 cropped figures, 5 TikZ/pgfplots figures and
3 tables, and typesets to 31 pages against the book's 39.

## Tools

- `tools/pdf2tex_draft.py` — page range → draft LaTeX (see above).
- `tools/crop_figures.py` — list the figure rectangles on a page, or crop one to PNG.

Both need PyMuPDF (`fitz`).
