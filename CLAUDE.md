# Working rules for this repository

This repo holds the LaTeX transcription (`latex/`) and the PreTeXt conversion (`pretext/`) of
*Additional Mathematics for Senior High Schools, Year 2* (Ministry of Education / Mathematics
Association of Ghana, 2025). The repo name says "section-1" for historical reasons; it holds
the whole book.

## The book PDF

- Local path on Michele's machine: `C:\Users\ACER\Ghana Text Books\Additional-Maths-book-2.pdf`
  (481 pages, InDesign export, text and equations are real text, not scans).
- **Never commit the PDF, page scans or page renders.** The book is all rights reserved and
  permission is still being negotiated. Only the transcription goes in git.
- Book page = PDF page − 1 throughout the body.

| Section | Title | PDF pages | Book pages |
|---|---|---|---|
| 1 | Sets and Binomial Expansions | 8–49 | 7–48 |
| 2 | Sequences and Inequalities | 50–88 | 49–87 |
| 3 | Polynomial Functions | 89–133 | 88–132 |
| 4 | Circles and Loci | 134–176 | 133–175 |
| 5 | Vectors | 177–197 | 176–196 |
| 6 | Matrices | 198–228 | 197–227 |
| 7 | Correlation | 229–269 | 228–268 |
| 8 | Indices and Logarithms | 270–305 | 269–304 |
| 9 | Trigonometric Identities | 306–332 | 305–331 |
| 10 | Differentiation | 333–365 | 332–364 |
| 11 | Integration | 366–389 | 365–388 |
| 12 | Applications of Differentiation | 390–420 | 389–419 |
| 13 | Probability | 421–434 | 420–433 |
| 14 | Combinations and Permutations | 435–448 | 434–447 |
| — | Answers to Review Questions | 449–473 | 448–472 |
| — | References, Glossary | 474–481 | 473–480 |

Each Section's answer key starts under the heading "Review Questions for Section N" in the
answers appendix; find it with a text search over PDF pages 449–473.

## Transcribing a Section (the loop that produced Section 2)

Read `latex/README.md` first; it has the conventions and the tool usage. In short:

1. Branch `latex/section-NN` in your own git worktree. Create `latex/sectionNN/` with
   `main.tex` (copy Section 2's and change the titles), `sections/`, `figures/`, `answers.tex`.
2. `python latex/tools/pdf2tex_draft.py <PDF> FIRST LAST > draft.tex` gives the prose. Render
   each page (PyMuPDF, 130 dpi, into a scratch folder outside the repo) and re-typeset every
   equation from the image. The draft flattens fractions and drops superscripts; never trust it
   for maths.
3. One file per book topic under `sections/`, headed by a comment with the book and PDF page
   range. Headings: red capitals → `\section`, pink sub-heads → `\subsection`, the strand line
   at the top → `\section*`/`\subsection*`. Use the `keyideas`, `activity{...}`, `example{...}`
   environments and `\solution`, `\figcaption{n.m}{...}` from `latex/preamble.tex`. Do not edit
   the preamble without agreeing it with George (the PreTeXt conversion depends on it).
4. **Verbatim.** Keep the book's wording, numbering, typos and arithmetic slips. Where a slip
   would mislead a reader, add `\booknote[SN-kk]{...}` right after it saying what the book
   prints and what was meant, and add the matching row to `errata.csv` (see below). Do not
   silently correct the text.
5. Figures: screenshots (GeoGebra, Excel, photos) are cropped from the PDF with
   `latex/tools/crop_figures.py` at 200 dpi into `figures/` (JPEG if the PNG exceeds ~0.5 MB);
   simple diagrams (number lines, single curves, Venn diagrams) are redrawn in TikZ/pgfplots.
   Always `width=...\linewidth`, never `\textwidth` (boxes are narrower than the page).
6. Review Questions: `\section*{Review Questions}`, one `\item` per book question with the
   book's own numbering. Answers go in `answers.tex` with the answer key's own numbering.
7. Compile `sectionNN/main.tex` after every few pages, and `latex/book.tex` once at the end,
   after adding the Section's `\chapter` block and its answers to `book.tex`. Fix every
   overfull box. Run `python latex/tools/errata.py` (it fails on unmatched ids).
8. Update the status table in `latex/README.md`, commit, push, open a PR titled
   `Section NN: <title>`. The PR body lists the errata ids added and anything left undone.

## Tooling notes (this machine)

- MiKTeX 25.12 is installed per-user and is not on PATH:
  `C:\Users\ACER\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex`. Packages auto-install.
- Python has PyMuPDF (`fitz`), PIL, openpyxl. No `latexmk`, no `pdftoppm`.
- **Write `.tex` files with the Write/Edit tools, not shell heredocs.** The Bash tool on this
  machine collapses `\\` to `\`, which silently destroys every row separator in `align`,
  `tabular` and `cases`. Also keep single shell commands under ~8 KB; longer ones are truncated.
- Scratch renders go under the session scratchpad or `%TEMP%`, never in the repo.

## Errata

`errata.csv` (repo root) is the record of everything wrong in the printed book and everything
we may want to change. One row per item; `tools/errata.py` checks every `\booknote[id]` in the
LaTeX has a row and every row of kind `error` has a marker, and regenerates `ERRATA.md`.
Suggestions (kind `suggestion`) have no marker in the text; put a LaTeX comment
`% SUGGEST SN-Skk: ...` at the spot instead.
