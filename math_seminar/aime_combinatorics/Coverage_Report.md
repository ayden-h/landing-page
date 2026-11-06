# Coverage and verification report

Research edition: 6 November 2026.

## Archive scope

The standard archive contains **71 examinations and 1,065 numbered problem slots**: one 15-problem AIME in each year 1983–1999, followed by AIME I and AIME II in each year 2000–2026. Every slot was retrieved and assigned an inclusion decision. The identifier audit found no missing, duplicate, or unexpected slots in that standard inventory.

| Period | Problem slots classified | Included problems | Excluded problems | Newly written solutions |
|---|---:|---:|---:|---:|
| 1983–1999 | 255 | 82 | 173 | 82 |
| 2000–2013 | 420 | 131 | 289 | 131 |
| 2014–2026 | 390 | 144 | 246 | 144 |
| **Total** | **1,065** | **357** | **708** | **357** |

All 357 included entries currently have a completed solution and no entry is marked unresolved. The [classification ledger](data/classification.json) records every slot's decision and reason; the [coverage data](data/coverage.json) gives the annual counts. The [archive audit](data/archive_audit.json) records the source inventory and cross-checks.

“All” here refers to that standard archive and the stated subject rule. It does **not** certify exhaustive coverage of regional variants, alternate final questions, replacement examinations, or every version of a community page.

## Inclusion rule

Included problems require a substantive combinatorial idea: finite counting or probability; selections and arrangements; occupancy and partitions; combinatorial identities; paths, graphs, cycles, or symmetry; discrete optimization and invariants; or a geometric, algebraic, or number-theoretic setting whose main work is counting configurations. Continuous probability is included because its sample-space methods belong naturally with the discrete probability chapters.

A problem is excluded when its integer or finite answer alone is the only reason to call it combinatorics, and its essential work is algebra, geometry, or number theory. Hybrid classification is therefore an editorial decision, made explicit rather than concealed behind a claim that the subject boundary is canonical. The present volume does not replace the planned separate volumes in those subjects.

## Source provenance and review

The primary retrieved transcription was [AIME 1983–2026](https://huggingface.co/datasets/bhushansshah/AIME-1983-to-2026). A second [1983–2025 transcription](https://huggingface.co/datasets/Pandores/aime-1983-2025) supplied a cross-check over 1,035 slots; its nonempty answers agreed with the primary archive. The 2026 material was also compared with [aime26](https://huggingface.co/datasets/math-ai/aime26). Per-problem links lead to the corresponding Art of Problem Solving published problem and solution pages. The examinations are credited to the MAA American Mathematics Competitions.

For the included problems, the retrieved snapshot contains **1,136 archived solution entries**: 234 for 1983–1999, 362 for 2000–2013, and 540 for 2014–2026. **All 1,136 entries were inspected and their available mathematical text reviewed.** The [source-review ledger](data/source_review.json) and [published-source directory](Published_Solution_Sources.md) preserve each entry count and the zero-based indices reviewed.

An archived entry can contain a full proof, a fragment, a comment, a diagram-only hint, or an external link. Reviewing an entry means reading the mathematical text and formulas present in that snapshot and recording defects or limitations where found. It does not imply endorsing every argument. **No solution videos were reviewed.** A link-only entry or an image pointer was inspected as such; its linked content is not represented as read unless the item's notes expressly say so. Diagram-program source was not a substitute for a mathematical proof review.

The written solutions are new expositions after source consultation, not claims of blind independent discovery. Their review notes distinguish a sound borrowed method from a missing justification, a corrected formula, or a different proof. The collection contains short original restatements and source links rather than a bulk reproduction of downloaded copyrighted statements or community solution text. Raw transcriptions were used in a temporary research cache outside the deliverable; a dataset's license label was not treated as permission to republish underlying contest or contributor works.

The primary transcription has blank answer fields for 1987-A-07, 1998-A-02, 1998-A-09, and 1998-A-13. The solution records fill these through the mathematical proofs rather than treating a missing archive field as an answer. Further details appear in [rights and provenance](Rights_and_Provenance.md).

## Known wording variants

Two 2026 variants are explicitly recorded. In 2026-II-01, different requested sequence terms produce answers 196 and 178. In 2026-II-10, the greatest possible value of the requested length is 340, while the sum of all possible values is 850. These are different requests, not discrepancies to erase by forcing one answer into both statements. The archive audit records the [dataset-maintainer discussion](https://huggingface.co/datasets/MathArena/aime_2026/discussions/2) that prompted the comparison.

Readers should use the linked published wording and diagrams when working from a particular examination version. A compressed restatement is a study aid and can omit incidental narrative; it is not an official facsimile.

## Mathematical verification

The solutions were checked against the recorded answers and reviewed for their mathematical arguments. Additional exact checks use explicit enumeration, integer or rational arithmetic, finite-state counts, or a second formula suited to the problem.

| Additional verification | Recorded checks |
|---|---:|
| [1983–1999 exact problem checks](checks/early_exact_check_results.json) | 39 |
| [2000–2013 exact problem checks](data/middle_verification.json) | 116 |
| [2014–2026 exact problem checks](checks/recent_independent_results.json) | 21 |
| **Problem-check total** | **176** |
| [Theory small-case checks](data/theory_verification.json) | 1,317 |

The rectangular-loop calculation is additional: an exact-cover enumeration checks the square-board values through the 10 by 10 board and several taller rectangles. Its tall-rectangle results are recorded [separately](checks/catalan_rectangles_results.json). The general Catalan theorem also has a structural proof: the equality case of two diagonal bounds forces the corner loop to span the board, yielding a recursive decomposition. Finite agreement is not the proof of that theorem.

The book underwent an independent mathematical review of the generalized propositions, reflection hypotheses, gap arguments, probability assumptions, and exercise solutions. This led to explicit integer and endpoint restrictions and to the requirement that every finite block sequence be admissible in the free-sequence generating-function theorem. The recent Catalan-loop proof was separately reviewed for its corner-loop lemma and recurrence.

The count of checks is not a claim that all 357 solutions have been independently enumerated, that all checks use unrelated methods, or that every theorem has been formally verified. The individual records state what was actually checked.

## Representative corrections found in published alternatives

The critical review records are useful study material in their own right. Examples include:

- **2015-I-05:** one source alternative has an incorrect conditional factor in the sock-pair case analysis; its final answer does not follow from its displayed sum.
- **2015-I-14:** the principal archived parity discussion reverses the required parity in odd square-root blocks. The new solution uses an exact parity identity and handles endpoints separately.
- **2016-II-04:** necessary color totals alone do not prove a box can be colored. The new solution supplies an explicit arrangement attaining the volume bound.
- **2016-II-11:** one source undercounts both a residue class and its intersection by one; cancellation hides the error in the final answer.
- **2017-II-11:** the source/sink criterion for a tournament on five vertices needs proof and fails for six vertices. The new solution uses strongly connected components.
- **2026-I-15:** archived alternatives contain unsupported structural assertions or incorrect base cases. The diagonal argument and Catalan recurrence provide a complete replacement proof.

For specific defects and qualifications, consult the per-item source notes rather than treating answer agreement as proof validation.

## Files for study

The three printable volumes are [theory](output/Combinatorics_Theory.pdf), [problems](output/Combinatorics_Problems.pdf), and [worked solutions](output/Combinatorics_Worked_Solutions.pdf). Editable texts and a twelve-week study plan are linked from the [README](README.md). The consolidated records retain problem identifiers, answers, tags, source provenance, source-review indices, and verification notes so that future corrections can be attached to the precise entry.
