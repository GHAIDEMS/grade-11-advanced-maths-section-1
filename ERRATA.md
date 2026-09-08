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

## Section 3

| Id | Book p. | Location | Kind | The book prints | Should be / proposal | Handling | Status | Found by |
|---|---|---|---|---|---|---|---|---|
| S3-01 | 96 | Example 3.3 long division (`latex/section03/sections/02-factors-and-zeros.tex:348`) | error | subtracted lines printed as (x² + 2x − 0) and (6x + 12) | −(−x² + 2x − 0) and −(−6x + 12); quotient x² − x − 6 is right | verbatim + note | open | transcription |
| S3-02 | 98 | Example 3.4 statement vs solution (`latex/section03/sections/03-rational-zero-theorem.tex:62`) | error | question (b) x³ + x² − 2x − 5, (c) 3x³ + x² + x − 5; solution works (b) x³ + x² − 2x − 8, (c) 9x³ + x² + x − 10 | one polynomial per part throughout | verbatim + note | open | transcription |
| S3-03 | 98 | Example 3.4 solution (a) From ±2 (`latex/section03/sections/03-rational-zero-theorem.tex:86`) | error | 2/2, −2/2, 2/3, −2/3, 2/6, −2/6 = ±1, ±2/3, ±1/6; no combined list | ±2 by 1, 2, 3, 6 gives ±2, ±1, ±2/3, ±1/3 | verbatim + note | open | transcription |
| S3-04 | 99 | Example 3.4 solution (c) (`latex/section03/sections/03-rational-zero-theorem.tex:132`) | error | line headed From ±4 lists 5/1 … 5/9 | From ±5 | verbatim + note | open | transcription |
| S3-05 | 102-103 | Sketching Step 1 (Figures 3.1 and 3.2) (`latex/section03/sections/04-sketching.tex:24`) | error | "If a < 0" printed above both figures; both show the a > 0 shape | first caption a > 0; second figure should be the reflected (a < 0) shape | verbatim + note | open | transcription |
| S3-06 | 104/107/109 | Examples 3.6-3.8 Step 4 interval lists (`latex/section03/sections/04-sketching.tex:142`) | error | first interval printed as −2 < x (Ex 3.6) and −1 < x (Ex 3.7 and 3.8) | x < −2 and x < −1 | verbatim + note | open | transcription |
| S3-07 | 106 | Example 3.7 long division (`latex/section03/sections/04-sketching.tex:208`) | error | (−7x² − 7x + 12) without minus sign | −(−7x² − 7x + 0) | verbatim + note | open | transcription |
| S3-08 | 107 | Table 3.1 (Example 3.7) (`latex/section03/sections/04-sketching.tex:281`) | error | headings −2 > x, −2 < x < −1, −1 < x < 1.5, x > 1.5 copied from Example 3.6; last column 2(5)³ + 3(5)² − 5(5) − 6 = 294 | x < −1, −1 < x < 3, 3 < x < 4, x > 4; (5)³ − 6(5)² + 5(5) + 12 = 12 (still positive) | verbatim + note | open | transcription |
| S3-09 | 109 | Example 3.8 long division (`latex/section03/sections/04-sketching.tex:322`) | error | −(2x² − 4x − 6) | −(2x² − 4x + 0); remainder 3x − 6 is right | verbatim + note | open | transcription |
| S3-10 | 112 | Example 3.9 Step 1 item 2 (`latex/section03/sections/05-descartes.tex:26`) | error | f(x) = 3x³ − 2x² + 4x + 5 | 3x³ − 2x² + 4x − 5 as in the question | verbatim + note | open | transcription |
| S3-11 | 114 | Example 3.10 (b) Step 1 (`latex/section03/sections/05-descartes.tex:182`) | error | 3 (negative) | 3 (positive); count of 2 changes is right | verbatim + note | open | transcription |
| S3-12 | 116 | Example 3.10 (c) Step 4 (`latex/section03/sections/05-descartes.tex:300`) | error | From −2 to −6 no changes); changes numbered 2 then 3, total 2 | From −12 to −6; changes numbered 1 then 2 | verbatim + note | open | transcription |
| S3-13 | 118 | Example 3.12 solution (`latex/section03/sections/06-fundamental-theorem.tex:78`) | error | 3x[x² − (−25)(x² − 25)] | no factor 3x (carried over from Example 3.11) | verbatim + note | open | transcription |
| S3-14 | 124 | Example 3.16 solution (`latex/section03/sections/07-complex-conjugates.tex:111`) | error | NB: −i² = −1 | −i² = 1 (as in Example 3.15); next line is right | verbatim + note | open | transcription |
| S3-15 | 127 | Example 3.18 solution (`latex/section03/sections/08-linear-quadratic-factors.tex:136`) | error | x = 5/2 i or x = −5/2 i; factors (x + 5/2 i)(x − 5/2 i) | ±√(5/2) i = ±(√10/2) i | verbatim + note | open | transcription |
| S3-16 | 131 | Review Questions Q12 (`latex/section03/sections/09-exercises.tex:94`) | error | y⁴ + 3x² + 2 | y⁴ + 3y² + 2 (answer key treats it as one variable) | verbatim + note | open | transcription |
| S3-17 | 455 | Answer key Section 3 Q4(c) (`latex/section03/answers.tex:34`) | error | (x − 2)(2x − )(2x) | (x − 2)(2x + 3)(2x − 1) | verbatim + note | open | transcription |
| S3-18 | 455 | Answer key Section 3 Q6(b) (`latex/section03/answers.tex:51`) | error | …, −√5, √5 | −i√5, i√5 (2x⁴ + 17x² + 35 = (2x² + 7)(x² + 5)) | verbatim + note | open | transcription |
| S3-19 | 455 | Answer key Section 3 Q8 (`latex/section03/answers.tex:64`) | error | a = 11, b = 6; (2x + 1)(x + 2)(x + 3) | answer does not fit Q(x) = 10x³ + ax² − 10x + b (leading coefficient 2, Q(−½) = 12.5, Q(−1) = 17); as printed the question has no integer solution | verbatim + note | open | transcription |
| S3-20 | 455 | Answer key Section 3 Q9 (`latex/section03/answers.tex:69`) | error | x⁴ − 6x³ + 24x² − 38x + 29 | x⁴ − 6x³ + 24x² − 38x + 39 | verbatim + note | open | transcription |
| S3-21 | 456 | Answer key Section 3 Q11(c) (`latex/section03/answers.tex:84`) | error | x⁴ − 8x² + 16 | x⁴ − 4x³ − 3x² + 16x − 4 (= (x² − 4)(x² − 4x + 1)) | verbatim + note | open | transcription |

## Section 4

| Id | Book p. | Location | Kind | The book prints | Should be / proposal | Handling | Status | Found by |
|---|---|---|---|---|---|---|---|---|
| S4-01 | 138 | Example 4.1 solution (`latex/section04/sections/01-intro.tex:128`) | error | working of part (c) lettered d. to j. | one part c.; the question has parts a-c only | verbatim + note | open | transcription |
| S4-02 | 138 | Example 4.1 solution (c) (`latex/section04/sections/01-intro.tex:130`) | error | (-5—15)^2 | (-5 - (-15))^2 = 10^2 | verbatim + note | open | transcription |
| S4-03 | 142 | Example 4.2 solution (`latex/section04/sections/02-deriving-equation.tex:130`) | error | solution lettered a. to i. for four parts | (b) = b-e, (c) = f-h, (d) = i | verbatim + note | open | transcription |
| S4-04 | 145-146 | Example 4.4 solution (`latex/section04/sections/02-deriving-equation.tex:237`) | error | b. labels the centre and equation (part of (a)); the answers 57km and 23 km both sit under c. | b. 57km; c. 23 km | verbatim + note | open | transcription |
| S4-05 | 149 | Example 4.6 (a) Method 2 (`latex/section04/sections/02-deriving-equation.tex:394`) | error | Centre = (-4 _ -2, -2 _ -2) | (-4 ÷ -2, -2 ÷ -2) | verbatim + note | open | transcription |
| S4-06 | 150 | Example 4.6 (d) Method 1 (`latex/section04/sections/02-deriving-equation.tex:454`) | error | two equations on one line; (x - 1)^2 + (y + 0)^2 = 1 _ 4 | = 1/4 | verbatim + note | open | transcription |
| S4-07 | 152 | Example 4.7 Method 1 (`latex/section04/sections/03-from-given-points.tex:70`) | error | four lines of working numbered 1. to 4. | unnumbered working | verbatim + note | open | transcription |
| S4-08 | 152 | Method 2 text after Figure 4.15 (`latex/section04/sections/03-from-given-points.tex:38`) | error | is AOB = 90° | APB = 90° (O is the centre) | verbatim + note | open | transcription |
| S4-09 | 153 | Example 4.7 Method 2 (`latex/section04/sections/03-from-given-points.tex:101`) | error | gradient connecting (-2, 2) and (x, y) = -2/(x - (-2)) | (y - 2)/(x - (-2)) | verbatim + note | open | transcription |
| S4-10 | 160 | Example 4.9 solution (`latex/section04/sections/04-tangents-normals.tex:72`) | error | m = -(12 - 0)/(5 - 0) = -1 2/5; gradient of tangent -1/m = -(1/12)/5 = 1 × 5/12 | m = -12/5 = -2 2/5; -1/m = -1/(-12/5) = 5/12 | verbatim + note | open | transcription |
| S4-11 | 163-164 | Example 4.12 (question and Figure 4.25 caption) (`latex/section04/sections/04-tangents-normals.tex:206`) | error | circle x² + y² - 2x + 12y - 3 = 0 | solution works x² + y² - 6x + 4y - 3 = 0 (centre (3, -2), r = 4); for the printed circle L = √61 | verbatim + note | open | transcription |
| S4-12 | 165 | Example 4.13 (a) (`latex/section04/sections/04-tangents-normals.tex:275`) | error | (x - (-5)^2 + (y - (-2))^2 = 3^2 | (x - (-5))^2 + … | verbatim + note | open | transcription |
| S4-13 | 165 | Example 4.13 (b) (`latex/section04/sections/04-tangents-normals.tex:290`) | error | √(6² - 3²) = √(36 - 6) = √30 | √(36 - 9) = √27 = 3√3 | verbatim + note | open | transcription |
| S4-14 | 166 | Example 4.14 solution (`latex/section04/sections/05-loci.tex:40`) | error | Using the general equation of the circle | the standard equation (x - h)² + (y - k)² = r² is used | verbatim + note | open | transcription |
| S4-15 | 172-175 | Review Questions numbering (`latex/section04/sections/06-exercises.tex:3`) | error | questions numbered 1-25; single problems split over 1/2, 6/7, 10/11, 12/13, 14/15, 24/25; 1 g is the end of 1 f | 19 problems, as in the answer key | verbatim + note | open | transcription |
| S4-16 | 175 | Review Questions Q21 (`latex/section04/sections/06-exercises.tex:141`) | error | lines 3y - x = 0 and x - 3y = 0 | the two lines coincide; the question needs two different lines | verbatim + note | open | transcription |
| S4-17 | 456 | Answer key Section 4 Q3(d) (`latex/section04/answers.tex:27`) | error | 10 + 4√5 | 10 + 2√5 (\|AB\| = √20, \|BC\| = \|AC\| = 5) | verbatim + note | open | transcription |
| S4-18 | 457 | Answer key Section 4 Q5(a) (`latex/section04/answers.tex:39`) | error | (x + 5)² + (y + 12)² = 30² | (x - 5)² + (y - 12)² = 30² (post office is 5 km east, 12 km north of the house) | verbatim + note | open | transcription |
| S4-19 | 457 | Answer key Section 4 Q9(b) (`latex/section04/answers.tex:71`) | error | x² + y² + 4x - 12 = 0 | x² + y² - 4x - 12 = 0 (centre (2, 0)) | verbatim + note | open | transcription |
| S4-20 | 458 | Answer key Section 4 Q16 (`latex/section04/answers.tex:104`) | error | y - x = 0 | does not follow: the two lines in the question are the same line (S4-16) | verbatim + note | open | transcription |
