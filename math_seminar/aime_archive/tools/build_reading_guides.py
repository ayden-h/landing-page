"""Build coverage, provenance, errata, and reading guides from the final audit."""
from pathlib import Path
from collections import Counter
import json,re
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
SUBJECTS=('combinatorics','geometry','algebra','number_theory')
NAMES={s:s.replace('_',' ').title() for s in SUBJECTS}
BOOKS={s:'_'.join(w.title() for w in s.split('_'))+'_Theory' for s in SUBJECTS}
PLANS={
'geometry':[
('1–2','Similarity, area ratios, cevians; Chapters 1–3','Normalize a length, translate side ratios into affine weights, and prove the metric formula you use.'),
('3–4','Tangency, circles, and centers; Chapters 4–7','Record powers with signs, distinguish arcs, and compare coordinate and synthetic proofs.'),
('5–6','Vectors, complex coordinates, inversion; Chapters 8–10','Choose an origin that eliminates a constraint; check transformed domains and incidence.'),
('7–8','Trigonometry, reflection, solids; Chapters 11–13','Write the equality construction and verify that feet and intersections lie on the required segments.'),
('9–12','Archive-derived shortcuts and mixed practice; Chapter 14 onward','Attempt six to ten historical problems per week and rewrite each decisive argument without referring to the source.')],
'algebra':[
('1–2','Domains, symmetric coordinates, polynomials; Chapters 1–4','Track which transformations are equivalences and compute the target invariant before individual unknowns.'),
('3–4','Symmetry, composition, recurrences; Chapters 5–8','State every initial value and excluded denominator; prove the iterate formula.'),
('5–6','Radicals, floors, inequalities; Chapters 9–11','Keep endpoint signs and equality conditions beside each formula.'),
('7–8','Complex numbers, trigonometry, logarithms; Chapters 12–14','Separate magnitude from argument and use monotonicity to prove uniqueness.'),
('9–12','Finite differences and mixed practice; Chapter 15 onward','Compare a direct expansion with a shorter invariant proof, then solve chronological sets.')],
'number_theory':[
('1–2','Gcd, valuations, divisor functions; Chapters 1–3','Translate conditions into prime-exponent constraints and prove both directions.'),
('3–4','Congruences, prime powers, orders; Chapters 4–6','Check coprimality before division or exponent reduction.'),
('5–6','Factorials, lifting, digits; Chapters 7–9','Keep the prime-two exception and reduced-denominator conditions explicit.'),
('7–8','Diophantine equations, factorization, descent; Chapters 10–12','Prove that a parameterization is exhaustive and that every candidate is feasible.'),
('9–12','Floor sums, extrema, mixed practice; Chapter 13 onward','Bound a search before running it, then produce a concise proof independent of numerical reconnaissance.')]
}

def main():
 records=json.loads((ROOT/'data/all_problems_and_solutions.json').read_text())
 meta=json.loads((ROOT/'data/archive_metadata.json').read_text())
 assert len(records)==len(meta)==1065
 total_entries=sum(r['available_source_solutions'] for r in meta)
 counts={s:sum(s in r['subjects'] for r in records) for s in SUBJECTS}
 corrections=[r for r in records if r.get('source_correction') or r.get('variant_note') or r.get('source_discrepancy') or r['id']=='2022-II-08']
 source_text=f'''# Rights, sources, and provenance

Contest credit belongs to the Mathematical Association of America, American Mathematics Competitions. This is an unofficial research and study edition. It contains newly worded mathematical restatements, newly written solution exposition after source consultation, review notes, and an original organization of classical methods. It does not claim blind independent solving, official endorsement, or priority for classical mathematics.

## Research sources and redistribution

The main source was the [1983–2026 transcription](https://huggingface.co/datasets/bhushansshah/AIME-1983-to-2026), checked against the [Pandores 1983–2025 archive](https://huggingface.co/datasets/Pandores/aime-1983-2025) and the [math-ai 2026 archive](https://huggingface.co/datasets/math-ai/aime26). The per-problem links point to the [AoPS AIME archive](https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions). The retrieved main CSV has SHA-256 `c28491d5f462d5f5685cbb9f70b954d0527e40095c0b0e2f49f77a2f28b14e39`. The research edition is dated November 2026.

Raw problem and community-solution transcriptions were downloaded into a temporary research cache and read there. They are not bulk-republished in this repository. A dataset uploader's license label is not treated as permission to redistribute all underlying contest and contributor text. The published-source directories supply access to original wording, diagrams, and alternative solutions alongside the new work. AoPS contributors retain their source attribution; see the [AoPS terms](https://artofproblemsolving.com/company/tos).

All **{total_entries:,} stored source entries** across the **1,065 standard problem slots** were inspected. This is an entry count, not a count of independent full proofs: entries include continuations, comments, attribution lines, diagram code, and media links. Inspecting a link does not imply watching its video or reviewing its target. Missing source material and source defects are documented in the problem files. Source comparison is critical review, not blanket certification of the published alternatives.

## Archive universe and variants

The universe is 17 annual AIME papers from 1983–1999 and 54 AIME I/II papers from 2000–2026: 71 papers and 1,065 numbered slots. The second 2020 paper, also called AOIME, is counted once. Coverage is complete for this defined universe; it does not certify discovery of every regional wording or alternate administration. Subject labels overlap when a solution uses substantive methods from more than one field, and each classification has a problem-specific reason.

The main transcription has blank answers for 1987-A-07, 1998-A-02, 1998-A-09, and 1998-A-13. The authored proofs establish 070, 480, 087, and 368. Transcription agreement is not independent mathematical proof, especially when datasets share source ancestry.

The [MathArena maintainer's 2026 discussion](https://huggingface.co/datasets/MathArena/aime_2026/discussions/2) documents version differences. In 2026-II-01, the tenth-term and eleventh-term requests yield 178 and 196. In 2026-II-10, the sum and maximum of possible lengths yield 850 and 340. The main archive version and the alternate targets are identified explicitly, not silently conflated.

For 2022-II-08, uniqueness among all positive integers gives 080; comparison only within integers at most 600 gives 081. Archived notes report acceptance of both, but a primary MAA acceptance notice was not retrieved. The [licensed LIVE archive](https://live.poshenloh.com/past-contests/aime/2022II/problem/8) uses the all-positive comparison. Other statement conventions and diagnosed inconsistencies are collected in [Errata and conventions](Errata_and_Conventions.md).

## Verification and limits

Every slot has a new worked solution or, where the reviewed wording is inconsistent, a worked diagnosis explaining the reported and literal outcomes. Exact computation supplements the written proofs. The check reports distinguish enumeration, alternate derivation, arithmetic substitution, source-answer agreement, and finite theorem samples. None of these is represented as formal proof verification of the entire collection.

The three added theory books received a separate full proof-and-exercise review; see [the peer-review log](source_notes/theory_peer_review_early.md). Their 6,584 finite parameter checks support rather than replace their general proofs. Additional material written after that review identifies its own verification in its source notes. “Derived” means formulated during this audit, not a claim of mathematical novelty.
'''
 (ROOT/'Rights_and_Provenance.md').write_text(source_text)
 errata=['# Errata, wording variants, and conventions\n',
 'These notes distinguish defects in the reviewed transcriptions from differences in mathematical interpretation. A reported answer is preserved when needed, but the worked proof explains what the stated conditions actually imply. A defect in a licensed or community archive is not automatically a verified defect in the original MAA paper.\n']
 for r in corrections:
  subject=next((s for s in ('geometry','algebra','number_theory','combinatorics') if s in r['subjects']))
  errata.append(f"## [{r['id']}: {r['title']}](../aime_{subject}/worked_solutions/{r['id']}.md)\n")
  for key in ('source_correction','variant_note','source_discrepancy'):
   value=r.get(key)
   if not value:continue
   if isinstance(value,dict):
    for k,v in value.items():
     if isinstance(v,str) and v.startswith('https://') and not any(c.isspace() for c in v):v='[Verified source]('+v+')'
     errata.append(f"- **{k.replace('_',' ').capitalize()}:** {v}")
   else:errata.append(str(value))
  if r.get('variants'):
   for v in r['variants']:errata.append(f"- {v['description']}: **{int(v['answer']):03d}**.")
  if r['id']=='2022-II-08':
   errata.append('Uniqueness among all positive integers gives **080**. Restricting the possible comparison integers to at most 600 adds the boundary value 600 and gives **081**. Archived notes report acceptance of both; a primary MAA acceptance notice was not retrieved. The restatement specifies the all-positive comparison explicitly.')
  errata.append('')
 errata += ['## Other source-proof defects\n','The individual source-comparison paragraphs record further errors that do not change the intended problem: unjustified equality cases, missed parameter bounds, erroneous congruence cancellation, incorrect prime claims, and transcription mistakes. They remain beside the relevant proof rather than being treated as defects of every source or of the original examination.\n']
 (ROOT/'Errata_and_Conventions.md').write_text('\n'.join(errata))
 for subject in ('geometry','algebra','number_theory'):
  root=WORK/('aime_'+subject);name=NAMES[subject];book=BOOKS[subject];prefix=book.removesuffix('_Theory')
  cov=json.loads((root/'data/coverage.json').read_text());n=cov['included_problems'];entries=cov['stored_source_entries']
  intro=f'''# AIME {name}: historical problems and a preparation book

This research edition contains **{n} {name.lower()} problems and substantive hybrids from the standard 1983–2026 AIME archive**, with original mathematical restatements, new worked exposition, answers, method tags, published-source links, and critical comparison notes. The accompanying book develops the recurring methods into definitions, lemmas, theorems, proofs, worked examples, and original exercises.

## Read or print

| Volume | Use |
|---|---|
| [Theory book](output/{book}.pdf) | Learn the structures and hypotheses behind short solutions. |
| [Problem collection](output/{prefix}_Problems.pdf) | Attempt the historical problems before consulting a proof. |
| [Worked solutions](output/{prefix}_Worked_Solutions.pdf) | Study the complete reasoning, source comparison, and checks. |

Editable files: [theory](theory/{book}.md), [problems](Problems.md), [worked solutions](Worked_Solutions.md), [method index](Method_Index.md), [published-source directory](Published_Solution_Sources.md), and [structured data](data/problems_and_solutions.json).

## Scope and evidence

All **1,065 slots in 71 standard examinations** were classified individually. This volume includes {n} of them; subjects overlap, so the four volume counts are not intended to sum to 1,065. Every included slot has a worked mathematical account. Where source wording requires a convention or has a diagnosed inconsistency, the account states that qualification rather than forcing the reported integer answer.

All **{entries:,} stored source entries** for this volume were inspected. The solutions are newly written after source consultation, not claimed as blind independent discoveries. Raw downloaded copyrighted statements and community solutions are not bulk-republished here; their published pages are linked. Counts include comments and link-only entries, and do not imply that videos or missing diagrams were reviewed.

The [coverage report](Coverage_Report.md), [shared provenance report](../aime_archive/Rights_and_Provenance.md), and [errata and conventions](../aime_archive/Errata_and_Conventions.md) specify these boundaries. General proofs and exact checks play different roles: a finite experiment can reject an error or confirm a small case, but it cannot replace a universal proof.

## A twelve-week study plan

Use one session to prove a method, one for related AIME problems, and one for mixed practice and written error analysis. Close the worked solution and reproduce it the next day. Keep the domain, multiplicities, and equality conditions next to the central calculation.

| Weeks | Focus | Written practice |
|---|---|---|
'''
  intro+='\n'.join('| '+' | '.join(row)+' |' for row in PLANS[subject])
  intro+='\n\nAfter the first pass, revisit the remaining problems in chronological mixed sets. Seek a shorter proof only when its hypotheses and converse are still explicit. The method index gives a second route through the same archive.\n\n'
  intro+='Other volumes: '+', '.join(f'[{NAMES[s]}](../aime_{s}/)' for s in SUBJECTS if s!=subject)+'. The [shared archive hub](../aime_archive/) contains the full classification, audit notes, and check reports.\n'
  (root/'README.md').write_text(intro)
  coverage=f'''# AIME {name} coverage report

- Standard universe: **1983–2026**, **71 papers**, **1,065 numbered slots**.
- Included here: **{n} problems**, all with a worked mathematical account.
- Source entries available and inspected: **{entries:,} / {entries:,}**.
- Classification: [all-slot decisions](data/classification.json), including reasons and other substantive subjects.
- Per-entry source review: [review ledger](data/source_review.json).

The archive is complete within the standard year/form/number universe. It does not certify coverage of every regional wording. A source-entry count includes comments, partial arguments, and link-only material, and is not a count of independent full solutions. Explicit conventions, alternate requests, and diagnosed inconsistencies appear in the [shared errata](../aime_archive/Errata_and_Conventions.md).

## Included problems by year

| Year | Problems |
|---|---:|
'''
  coverage+='\n'.join(f'| {y} | {c} |' for y,c in cov['by_year'].items())+'\n\n'
  coverage+='## Verification\n\nThe [shared checks directory](../aime_archive/checks/) contains finite enumerations and exact substitutions for selected historical solutions. The [theory check ledger](../aime_archive/data/theory_check_results.json) records 6,584 parameter cases across the three books. The [proof review](../aime_archive/source_notes/theory_peer_review_early.md) records a full review of the original theory drafts and exercise solutions. Later additions and PDF layout have separate records. None is described as machine verification of all mathematical proofs.\n'
  (root/'Coverage_Report.md').write_text(coverage)
  (root/'Rights_and_Provenance.md').write_text('# Rights and provenance\n\nSee the [shared provenance report](../aime_archive/Rights_and_Provenance.md) for contest credit, source archives, research scope, version differences, and redistribution boundaries. This volume includes new exposition and source links; raw downloaded source text remains outside the repository.\n')
 hub=f'''# AIME: four historical collections and theory books

This project classifies and supplies a worked mathematical account for all **1,065 numbered problems in the 71 standard AIME papers from 1983 through 2026**. Each subject collection includes a printable theory book, a problem volume, and a worked-solution volume. The theory organizes classical tools and archive-derived shortcuts with proofs and exercises.

| Collection | Included problems | Read |
|---|---:|---|
'''
 hub+='\n'.join(f'| {NAMES[s]} | {counts[s]} | [Open volume](../aime_{s}/) |' for s in SUBJECTS)
 hub+=f'''\n
Subject counts overlap. Classification is a documented mathematical judgment, not an official MAA taxonomy. Each entry has a reason, and counting hybrids can appear in several volumes.

The audit inspected **{total_entries:,} stored source entries**. Raw source transcriptions were downloaded for research, but copyrighted source anthologies are not republished. The deliverables provide new restatements, source-consulted solution exposition, critical notes, and per-problem links to published material. Known alternative versions and wording conventions are explicit.

## Audit and study resources

- [All 1,065 classifications](data/classification.json)
- [All worked records](data/all_problems_and_solutions.json)
- [Coverage data](data/coverage.json)
- [Rights and provenance](Rights_and_Provenance.md)
- [Errata, variants, and conventions](Errata_and_Conventions.md)
- [Theory proof review](source_notes/theory_peer_review_early.md)
- [Finite and exact checks](checks/)
- [Archive-derived theory findings](source_notes/)
- [Rebuilding the reading files and PDFs](BUILD.md)

Read a theory chapter, attempt a related set from the method index, then compare the proof and source review. For problems with an extremum or a parameterization, finish by proving attainment or the converse. Those often explain the difference between a short valid solution and a convincing-looking incomplete one.
'''
 (ROOT/'README.md').write_text(hub)
 (ROOT/'BUILD.md').write_text('''# Rebuilding the collection

Run the following from the parent directory containing the four subject folders and `aime_archive`. Python 3.9 or later is sufficient for the data builders and standard-library checks. The drawing generator additionally uses Matplotlib. PDF builds require Pandoc and Tectonic (or adapting the script to an installed LaTeX engine).

```sh
python3 aime_archive/tools/build_subjects.py
python3 aime_archive/tools/build_reading_guides.py
python3 aime_archive/checks/theory_checks.py
python3 aime_archive/tools/build_pdfs.py geometry
python3 aime_archive/tools/build_pdfs.py algebra
python3 aime_archive/tools/build_pdfs.py number_theory
python3 aime_archive/tools/validate_release.py
```

The subject builder requires exactly 1,065 unique records and classifications and verifies complete zero-based source-entry coverage. It reads the audited era records; it does not download copyrighted source text. The combinatorics collection has its own builder and check scripts under its `tools` directory. The shared classification is reconciled with that collection before publication. The optional `validate_pdfs.py` check uses pypdf to compare the twelve final PDFs against their visual-inspection ledgers, verify their source hashes, and check that all four theory title pages and PDF author fields credit Ayden Bi.

To supply nonstandard executable locations, use `--pandoc PATH --tectonic PATH`. The optional `--theory-only` flag rebuilds just the theory volume. Every published PDF is rendered and inspected separately; successful compilation alone is not treated as layout verification.
''')
 print(json.dumps({'subject_counts':counts,'source_entries':total_entries,'explicit_corrections':len(corrections)},indent=2))

if __name__=='__main__':main()
