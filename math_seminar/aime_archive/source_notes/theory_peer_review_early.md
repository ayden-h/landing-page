# Independent mathematical review of the three added theory books

Review date: 2026-11-06. Reviewer: the agent responsible for the 1983–1999 archive. This review followed completion of all 255 early-era records, including the 173 newly written solutions and all 577 archived alternative entries for those new records.

## Scope and outcome

I read every statement, proof, worked example, exercise, and exercise solution in the following drafts:

| Book | Sections reviewed | Exercise solutions reviewed |
|---|---|---|
| Geometry | All chapters 1–16, including the archive-derived results and the 2016-I-09 source-discrepancy clinic | All 20 |
| Algebra | All chapters 1–17, including the recurrence, floor-fiber, root-filter, and archive-derived sections | All 24 |
| Number theory | All chapters 1–18, including lifting, numerator feasibility, and the shortened-factorial theorem | All 26 |

No incorrect numerical theorem formula or exercise answer was found. The edits below repair omitted hypotheses, degenerate cases, or wording that could support an invalid extension. They do not change the intended answers. The review checks the proofs themselves; finite computations are supplementary evidence rather than substitutes for the arguments.

## Geometry edits

File: `aime_geometry/theory/Geometry_Theory.md`.

1. **Corollary 5.4, radical center.** Required pairwise distinct centers and a unique intersection of the two axes. Coincident circles and coincident axes do not satisfy the ordinary three-line formulation without further conventions.
2. **Section 8.4, orthogonal projection.** Stated that the direction vector is nonzero and identified the segment as the points with parameter between zero and one. This prevents division by a zero squared length and makes the endpoint test explicit.
3. **Section 13.2, spheres tangent to a plane.** Required the spheres to lie on the same side of the plane. Their vertical center difference is then the difference of their radii, giving horizontal distance squared equal to four times their product. Added the corresponding same-side and external-tangency conditions for the circle version.
4. **Section 13.3, Gram determinants.** Restricted the implication “zero determinant means degeneracy” to realizable data. A nonnegative determinant by itself is not a realizability test: the full Gram matrix must be positive semidefinite, and positive definite for a nondegenerate tetrahedron.

Particular proof checks included Ceva's barycentric weights, the Ptolemy similarity construction, the triple-angle factorization, all archive-derived generalizations in Chapter 14, and all equality/branch restrictions in the worked examples. The intentional 2016-I-09 archive discrepancy was checked and preserved; the historical reported answer was not silently substituted for the result of the stated geometry.

## Algebra edits

File: `aime_algebra/theory/Algebra_Theory.md`.

1. **Proposition 2.4, converse to power-sum elimination.** Made the real-variable assumptions and discriminant condition explicit; algebraic reconstruction over the complex numbers does not by itself give real values.
2. **Theorem 8.1, second-order recurrence.** Fixed the sequence domain and the initial values as the zeroth and first terms. Stated the zeroth-power convention for a zero characteristic root; otherwise the formula can lose an arbitrary initial value.
3. **Theorem 8.4, weighted moments.** Required a positive number of bases, allowed real or complex bases explicitly, and defined the zeroth moment separately as the sum of the weights. This removes an unnecessary undefined-zero-power edge case.
4. **Section 9.3, conjugate powers.** Distinguished nonnegative exponents for integrality from positive exponents for the strict small-conjugate inequality used in the floor argument.
5. **Theorem 12.2, root-of-unity filter.** Required a positive integer modulus and integer exponents/residue indices.
6. **Proposition 15.4, arithmetic-progression arrays.** Specified consecutive integer row and column indices; supplied the one-row/one-column cases, where unused coefficients can be set to zero.
7. **Theorem 15.5, weighted binomial modes.** Required the row index to be a nonnegative integer. The one-mode/two-mode distinction and the boundary indices were verified.
8. **Exercise 20.** Specified real variables, as required by its inequality and equality argument.

Particular proof checks included Newton sums, reciprocal polynomial reduction, recurrence degeneracies, the exact root counts in Section 10.2, the absolute-value defect identity in Section 10.3, and the floor-fiber count. No intentional archive branch discrepancy was overwritten.

## Number theory edits

File: `aime_number_theory/theory/Number_Theory_Theory.md`.

1. **Lemma 2.2.** Specified nonzero rational summands and a nonzero sum, consistent with the book's finite-valuation convention.
2. **Section 2.1 and Proposition 2.3.** Required a positive power and positive integer exponents; handled the zero rational separately in the rational-integrality argument.
3. **Proposition 3.4.** Specified that the fixed sum is an integer.
4. **Proposition 6.4.** Replaced “odd consecutive numbers” by “consecutive odd integers”; their difference is two, and their oddness is what makes their gcd one.
5. **Theorem 7.1, Corollary 7.2, and Theorem 7.3.** Made the factorial/binomial index domains and the primality assumption explicit. Lucas's statement permits nonnegative indices, using the standard zero value when the lower index exceeds the upper one.
6. **Theorem 8.2.** Required a positive integer exponent; exponent zero would produce the excluded valuation of zero.
7. **Section 9.1.** Required an integer base at least two and stated that leading zeros are ignored for uniqueness.
8. **Theorem 9.2.** Specified the ordinary decimal expansion that is not eventually all nines, together with integer numerator and denominator. This removes the second decimal representation of terminating rationals.
9. **Theorem 9.3.** Specified that the denominator and enumerated numerators are positive integers.

The proofs of both lifting theorems, the prime-two square-root count, the exponential-gcd criterion, reduced-numerator feasibility, the Frobenius boundary, primitive Pythagorean parametrization, descent, and the factorial-block maximum were checked in full. The factorial-block result correctly excludes parameter one: for that parameter every positive-length block from two through the endpoint works, so there is no finite maximum.

## Verification after edits

Ran `aime_archive/checks/theory_checks.py` successfully after the edits. All **6,584 exact parameter cases passed**: geometry 587, algebra 1,825, and number theory 4,172. These are counts of parameter instances, not counts of separately proved theorems.

This log records mathematical review of the Markdown drafts. It does not certify the subsequent PDF layout, completeness of every regional examination variant, or the correctness of the entire historical archive beyond the assigned early era.

## Supplemental results and targeted PDF review

After completing the 2026 supplemental archive, I added and proved the following results. They are archive-driven formulations of standard methods, with no claim of mathematical novelty.

- **Geometry, Section 13.5, Theorem 13.3:** positive sphere radii above a fixed contact plane admit a distinct common tangent plane on one common side exactly when they are affine functions of the planar contact points. The proof includes the converse plane construction, its normal length, positivity of all signed center distances, and the distinct-plane condition. Three noncollinear contact points give unique interpolation. The worked application is 2026-I-12.
- **Geometry, Section 14.8, Proposition 14.11:** for a convex equiangular pentagon, perimeter squared equals the square root of five times twice the diagonal-square sum minus three times the side-square sum. The proof derives both cyclic-product equations from diagonal lengths and vector closure. The worked application is 2026-I-14.
- **Number theory, Section 9.4, Lemma 9.4 and Proposition 9.5:** a nonnegative coefficient series has its ending integer block fixed when the full scaled tail is below one. An explicit geometric bound handles a known finite tail prefix and a later linear coefficient majorant. The divisor-generating expansion is proved by regrouping nonnegative geometric-series terms. The 2026-II-09 application supplies the missing full carry bound, 361/810.

The agent responsible for the middle-era archive independently checked the hypotheses and algebra of all three additions and found no remaining concern. Exact supplemental checks in `checks/late_theory_additions.py` passed **1,169 parameter cases**: 75 positive equiangular pentagons with exact cyclotomic vector closure, 625 affine sphere-radius instances including parallel tangent planes, and 469 carry certificates checked against rational truncations of the original infinite series with rigorous remainder bounds. The existing 6,584 theory cases and the 16 supplemental 2026 problem checks also passed again.

Rebuilt `aime_geometry/output/Geometry_Theory.pdf` (**40 pages**) and `aime_number_theory/output/Number_Theory_Theory.pdf` (**31 pages**) with the archive's prescribed Pandoc/Tectonic builder. Added section page breaks to keep each new exposition together, and shortened the pre-existing number-theory Section 9.3 heading to fit the text width. Final rendered-page inspection covered geometry physical pages 31 and 37 and number theory physical pages 18 and 19. The displayed formulas, proofs, headings, margins, and running page numbers are legible, with no clipping or overlap on those pages.

Neither build emitted overfull-box, underfull-box, or missing-glyph warnings. Geometry emitted five reproducibility warnings about Pandoc's temporary absolute image paths for its existing figures; number theory emitted no warnings. This targeted inspection covers the changed material and adjacent heading, not every page of either book or the later combined archive volumes.


## Final geometry and number theory PDF inspection, 2026-11-06

Rebuilt all six PDFs after the shared radical-baseline and literal-caret reader fixes. Geometry has 40/63/237 pages (theory/problems/worked solutions); number theory has 31/46/175. Inspected 36 rendered sample pages, including first/middle/last and mathematical pages in each volume. All 592 pages passed extracted-character page and body-margin bounds checks. No missing-glyph or overfull warnings remain; nonfatal underfull spacing notices and temporary-image path warnings are recorded in the QA ledgers. Both theory title pages visibly credit Ayden Bi, matching PDF Author metadata. The ledgers record source Markdown, PDF, and shared build-input SHA-256 hashes. This is sampled visual inspection, not a claim to have visually inspected every page.
