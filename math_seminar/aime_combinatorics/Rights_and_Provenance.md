# Rights, sources, and provenance

The contest problems are credited to the Mathematical Association of America, American Mathematics Competitions. This collection contains independently worded mathematical restatements, newly written solution exposition, and an original organization of classical and archive-derived methods. It is not an official MAA publication. New exposition means written after consulting sources, not solved without access to published answers or methods.

## What was retrieved and what is included

The research used the [1983–2026 transcription](https://huggingface.co/datasets/bhushansshah/AIME-1983-to-2026), checked against the [Pandores 1983–2025 archive](https://huggingface.co/datasets/Pandores/aime-1983-2025) and the [math-ai 2026 archive](https://huggingface.co/datasets/math-ai/aime26). These transcriptions point to the [AoPS AIME archive](https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions). The retrieved main CSV has SHA-256 `c28491d5f462d5f5685cbb9f70b954d0527e40095c0b0e2f49f77a2f28b14e39`. Research date: 6 November 2026.

Raw statements and community solutions were downloaded to a temporary research cache and read there. They are **not redistributed in this repository**. A dataset uploader's license label does not establish permission to republish all underlying contest and contributor material. The [source directory](Published_Solution_Sources.md) supplies a per-problem link; the [source-review data](data/source_review.json) records the inspected entries and specific defects. An entry can be a continuation, a comment, or a media link, so the count of entries is not a count of independent complete proofs. A link-only entry was inspected as a link; its video was not thereby reviewed.

AoPS contributors retain their own source attribution. The [AoPS terms](https://artofproblemsolving.com/company/tos) do not provide a blanket public redistribution license for all such solutions. The [Xue archive](https://www.xuemath.org/aime-resources), for example, describes permission for its own posting; that permission is not assumed to transfer to this project. Source links give access to published solutions alongside the new worked solutions without reproducing the source anthology.

## Coverage and transcription decisions

The working universe comprises 17 annual papers from 1983–1999 and 54 I/II papers from 2000–2026: 71 papers and 1,065 standard year/form/problem slots. The 2020 second paper is also called AOIME and is not counted twice. All slots have a recorded combinatorics inclusion or exclusion decision. This is complete coverage of that defined archive universe, not certification that every regional wording or alternate administration has been collected.

The 1,035 pre-2026 answer records were cross-checked wherever nonempty; no disagreements between the two transcriptions were found. Both can descend from the same source, so agreement is not independent mathematical verification. The main transcription has blank answer fields for 1987-A-07, 1998-A-02, 1998-A-09, and 1998-A-13; their authored solutions establish 070, 480, 087, and 368 respectively. Source scraping sometimes loses equations, spaces, or diagrams. Restatements were repaired by mathematical reconstruction and alternate transcriptions; the linked original remains the reference for official wording.

The 2026 materials include distinct versions, as discussed by the [MathArena maintainer](https://huggingface.co/datasets/MathArena/aime_2026/discussions/2). In 2026-II-01, asking for the tenth versus eleventh term produces 178 versus 196. In 2026-II-10, asking for the sum versus the maximum of possible lengths produces 850 versus 340. They are recorded as wording variants, not silently declared erroneous answer keys. The shared archive metadata retains the main transcription's version; subject volumes must specify the target they solve.

For 2022-II-08, uniqueness among all positive integers gives 080; restricting the comparison domain to integers at most 600 adds the endpoint 600 and gives 081. Archived community notes report acceptance of both answers. A primary MAA acceptance notice was not retrieved, so the mathematical distinction is documented without claiming primary confirmation of that administrative history. The [licensed LIVE archive](https://live.poshenloh.com/past-contests/aime/2022II/problem/8) uses the clarified all-positive-integers wording.

## What review establishes

Every included problem has a full newly written solution. All stored solution-text entries for included problems have been inspected, with missing material and link-only entries identified where relevant. Review does not certify every source proof: several sources have correct final answers supported by incomplete or incorrect arguments. Those defects are part of the source notes, not adopted as proof.

Exact check scripts and their result files distinguish a final-answer comparison from an independent enumeration or alternate derivation. The theory book supplies general proofs; finite checks support those proofs but do not replace them. No claim is made that all the classical theorems are new. “Derived” identifies a formulation distilled during this project; it does not assert priority in the mathematical literature.
