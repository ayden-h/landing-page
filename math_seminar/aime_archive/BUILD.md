# Rebuilding the collection

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
