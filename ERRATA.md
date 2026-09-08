# Errata and proposed changes to the printed book

Generated from `errata.csv` by `latex/tools/errata.py`; edit the CSV, not this file.
Ids `SN-kk` are errors kept verbatim in the LaTeX with a `\booknote[id]`; `SN-Skk` are
suggestions (no change made in the text).

## Section 1

| Id | Book p. | Location | Kind | The book prints | Should be / proposal | Handling | Status | Found by |
|---|---|---|---|---|---|---|---|---|
| S1-01 | 11 | Example 1.1 solution part 2 (`latex/section01/sections/02-demorgans.tex:105`) | error | R' and M' listed with b and h; R' ∩ M' = (R ∪ M)' = {b, x, v, q, w, j, k} | R' = {j,k,n,q,v,w,x}, M' = {d,j,k,m,q,s,v,w,x}; R' ∩ M' = (R ∪ M)' = {j,k,q,v,w,x} | verbatim + note | open | transcription (Santiago) |
| S1-02 | 11 | Example 1.1 solution part 3 (`latex/section01/sections/02-demorgans.tex:129`) | error | Q' = {b,c,g,h,i,j,k,m,p,r,t,y}; final line does not follow from the printed complements | Q' = {b,d,g,h,i,j,k,l,m,p,r,s,t,y}; (R ∩ M ∩ Q)' = {b,d,g,h,i,j,k,l,m,n,p,q,r,s,t,v,w,x,y} | verbatim + note | open | transcription (Santiago) |
| S1-03 | 22 | Example 1.8 Venn diagram (region formulas) (`latex/section01/sections/03-applying-demorgans.tex:359`) | error | Gold-only region labelled −18+x | x−21 | corrected in text + note | open | transcription (Santiago) |
| S1-04 | 22 | Example 1.8 completed diagram (`latex/section01/sections/03-applying-demorgans.tex:390`) | error | region values from x=25 (17, 25, 2, 13, 25, 5); inconsistent with part (f) = 34 | values from the solved x=28: 20, 22, 5, 10, 2, 7 (triple 28); 2+22+10 = 34 | verbatim + note | open | transcription (Santiago) |
| S1-05 | 43 | Review Questions Part A Q10(b) (`latex/section01/sections/05-exercises.tex:75`) | error | A' ∪ (Y ∩ Z') | A' ∪ (B ∩ C') | verbatim + note | open | STACK authoring |
| S1-06 | 48 | Review Questions Part B Q9 (`latex/section01/sections/05-exercises.tex:261`) | error | part (a) expands (1+py)^9 in y; part (b) gives the terms as 1 and 36x and qx^2 | one variable throughout | verbatim + note | open | STACK authoring |

## Section 2

| Id | Book p. | Location | Kind | The book prints | Should be / proposal | Handling | Status | Found by |
|---|---|---|---|---|---|---|---|---|
| S2-01 | 53 | Activity 2.2 steps 5 (`latex/section02/sections/03-arithmetic-and-geometric.tex:30`) | error | [a + 2d(n − 2)] in line (2); third bracket of 2Sn is [2a + (n − 1)] | [a + (n − 2)d] and [2a + (n − 1)d] | verbatim + note | open | transcription |
| S2-02 | 56 | Example 2.4 solution (`latex/section02/sections/03-arithmetic-and-geometric.tex:138`) | error | 2 × 16 382 / 3 | 2 × 16 383 / 3 (4^7 − 1 = 16383); final answer 10922 is correct | verbatim + note | open | transcription |
| S2-03 | 57 | Example 2.5 solution (`latex/section02/sections/03-arithmetic-and-geometric.tex:154`) | error | S10 = ½(1 − 1/1024) followed by S10 = (1024 − 1)/1024 | dividing by (1 − ½) cancels the ½; the intermediate line is wrong though the result is right | verbatim + note | open | transcription |
| S2-04 | 58 | Example 2.6 statement (`latex/preamble.tex:69`) | error | series printed as 5, −1 + 1/5, … | 5, −1, 1/5, … | verbatim + note | open | transcription |
| S2-05 | 60 | Example 2.7 solution (c) (`latex/section02/sections/05-recursive.tex:92`) | error | 0.41(0.1)^2 + 0.41(0.1)^3 | 0.41(0.01)^2 + 0.41(0.01)^3 | verbatim + note | open | transcription |
| S2-06 | 60 | Example 2.8 solution (`latex/section02/sections/05-recursive.tex:108`) | error | 0.9 / (1 − 0.1) = 0.9 / 0.1 = 1 | 0.9 / 0.9 = 1 | verbatim + note | open | transcription |
| S2-07 | 61 | Example 2.9 solution (`latex/section02/sections/05-recursive.tex:132`) | error | r = 6/100 ÷ 6/1000 = 1/10 | r = 6/1000 ÷ 6/100 = 1/10 | verbatim + note | open | transcription |
| S2-08 | 68 | Example 2.15 solution step 3 (`latex/section02/sections/07-max-min.tex:188`) | error | last three substitutions written m = …; point written (5.5, 2,5) | w = …; (5.5, 2.5) | verbatim + note | open | transcription |
| S2-09 | 80 | Example 2.20 solution step 3 (`latex/section02/sections/10-systems-quadratic.tex:61`) | error | y ≥ 3 3/49; second substitution headed At x = 0 | y ≥ 3 9/49 (= 156/49); At x = −12/7 | verbatim + note | open | transcription |
| S2-10 | 83 | Example 2.21 solution (`latex/section02/sections/11-real-life-quadratic.tex:69`) | error | Step 4 is followed by Step 6 | renumber or add the missing Step 5 | verbatim + note | open | transcription |
