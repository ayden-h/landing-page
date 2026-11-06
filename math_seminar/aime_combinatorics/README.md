# AIME Combinatorics: a historical collection and preparation book

This research edition contains **357 combinatorics and probability problems from the standard AIME archive, 1983–2026**, each with a short mathematical restatement, a newly written solution, an answer, method tags, and a link to published solutions. The accompanying theory book develops the recurring structures into definitions, theorems, proofs, worked examples, and exercises.

## Start here

| Read or print | Purpose |
|---|---|
| [Theory book](output/Combinatorics_Theory.pdf) | Learn the methods and their hypotheses; work the original exercises. |
| [Problem collection](output/Combinatorics_Problems.pdf) | Attempt the historical problems without seeing their solutions. |
| [Worked solutions](output/Combinatorics_Worked_Solutions.pdf) | Compare proofs, identify the decisive encoding, and check answers. |

Editable reading files: [theory](theory/Combinatorics_Theory.md), [problems](Problems.md), [solutions](Worked_Solutions.md), [method index](Method_Index.md), and [published-source directory](Published_Solution_Sources.md). The [coverage report](Coverage_Report.md) specifies the inclusion rule, source-review scope, checks, and known statement variants.

## What the collection contains

The audit classified every one of the **1,065 numbered problem slots in 71 standard examinations**. It includes discrete counting, probability, combinatorial identities, arrangements, graph arguments, and substantive geometric, algebraic, or number-theoretic counting. It excludes problems whose finite search is incidental to an essentially algebraic or number-theoretic solution. Each inclusion or exclusion has a recorded reason. This is coverage of the standard year/form/number archive, not certification that every regional or alternate wording has been found.

The solutions were written after consulting archived published approaches. They are new expositions and sometimes include repaired arguments or a shorter structural proof; they are **not presented as blind independent rediscoveries**. Classical results remain classical. The theory book's organizing framework and derived propositions are intended to make these particular families easier to recognize and solve, without claiming that every observation is a new research theorem.

The deliverables contain source links, original restatements, new solution prose, and critical review notes. **They do not contain a bulk copy of downloaded copyrighted problem and solution text.** Raw transcriptions used during research were kept outside this collection in a temporary cache. Use the published-source directory for the original wording, diagrams, and alternative expositions.

All **1,136 archived solution entries** for the selected problems were inspected, with their available mathematical text reviewed. Link-only entries and media pointers are distinguished from complete proofs; no solution videos were reviewed. See [rights and provenance](Rights_and_Provenance.md) for the source and redistribution boundaries.

## A practical study plan

Use three sessions per week: one to learn and prove a method, one for six to ten related historical problems, and one for mixed problems and a written error review. Attempt a problem before opening its solution; after reading a solution, close it and reproduce the proof the following day.

| Weeks | Focus | What to write in your notebook |
|---|---|---|
| 1–2 | Bijections, fibers, gaps, runs; Chapters 1–3 | The object being counted, the inverse map, and every multiplicity factor. |
| 3–4 | Occupancy, inclusion-exclusion, cycles, symmetry; Chapters 4–5 | A disjoint case split or event definition; the reason a division by a factorial is valid. |
| 5–6 | Recurrences, generating functions, paths; Chapters 6–8 | The smallest sufficient state, complete initial conditions, and the exact coefficient or boundary condition. |
| 7–8 | Discrete and continuous probability; Chapters 9–10 | The sample space, its weights, the conditioning event, and any zero-probability boundaries. |
| 9–10 | Residues, graphs, geometric counting; Chapters 11–13 | An invariant, an extremal construction, or a proof that all geometric cases are represented. |
| 11–12 | Combining methods, verification, original exercises; Chapters 14–17 | A shorter second proof and an explicit account of why the attempted first method was longer. |

Continue through the remaining problems using the method index, then revisit them in mixed chronological sets. A useful target is a one-paragraph proof whose brevity comes from a justified encoding. Retain a longer proof when a hidden hypothesis would otherwise disappear.

## Read the source notes critically

Several published alternatives reach the right answer through incomplete or incorrect intermediate claims. The review notes identify specific cases. For example, an archived solution of 2015-I-14 reverses the required parity in the odd square-root blocks; its endpoint errors happen to cancel. Some 2017-II-11 arguments fail to justify the special five-vertex tournament criterion. The rectangular-loop count in 2026-I-15 needed a structural proof; the new solution derives it from two diagonals and a Catalan recurrence.

The following distinctions matter throughout this collection:

- Circular positions may be labeled. Dividing by the number of rotations without proving equal orbit sizes changes the problem.
- A selected pair or distinguished feature may occur more than once in a single configuration. Counting those features is not automatically counting configurations.
- A recurrence needs an inverse decomposition, a sufficient state, and correct bases. Matching its first few terms is evidence, not a proof.
- An extremal bound needs a construction attaining it. Small exact enumerations check formulas but do not establish their general validity.
- A different final request can change an answer even when the setup is identical. The documented 2026-II-01 and 2026-II-10 variants are retained in the coverage notes.

## Evidence and navigation

There are **176 additional exact problem checks** in the current ledgers: 39 for 1983–1999, 116 for 2000–2013, and 21 for 2014–2026. The rectangular-loop enumerator supplies further independent finite checks. The theory verification ledger records **1,317 small-case checks**. These checks accompany mathematical proofs; they do not certify every line of every proof by computation.

Problem identifiers are stable: `1983-A-07` is Problem 7 of the single 1983 AIME; `2026-II-15` is Problem 15 of AIME II in 2026. Individual files are in the `problems` and `worked_solutions` directories. The consolidated [data file](data/problems_and_solutions.json) preserves the restatements, solutions, tags, source notes, and verification records for further study.

This volume covers combinatorics and its hybrids. Separate algebra, geometry, and number-theory volumes are outside the completed scope of this edition.
