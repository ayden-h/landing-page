# Rebuilding and checking the collection

The editable originals are `solutions/early.json`, `solutions/middle.json`, `solutions/recent.json`, and `theory/Combinatorics_Theory.md`. The individual problem files, solution files, combined reading files, indices, and coverage summaries are generated from them.

From this directory, use Python 3:

```sh
python3 tools/build_collection.py
python3 checks/early_exact_checks.py
python3 tools/verify_middle.py
python3 checks/recent_independent.py
python3 checks/recent_loops.py
python3 tools/verify_theory.py
```

The PDF build also needs Pandoc and Tectonic. Paths can be supplied explicitly:

```sh
python3 tools/build_pdfs.py --pandoc pandoc --tectonic tectonic
```

Read `Coverage_Report.md` before interpreting a check count. Some checks compare a formula to exhaustive enumeration; others are exact evaluations of a mathematical reduction. They are not a formal proof-verification system. The source-review sidecars are research records; their reconciled notes are already incorporated into the solution JSON originals.

The raw copyrighted source cache is deliberately not a build dependency and is not included. Rebuilding uses the new exposition and bibliographic metadata only.
