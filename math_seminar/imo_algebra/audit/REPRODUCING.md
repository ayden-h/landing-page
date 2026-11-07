# Rebuilding and verification

The editable Markdown and figure PDFs in this package are the final PDF inputs. With Python 3, Pandoc, XeLaTeX, Latin Modern and DejaVu fonts installed, run:

```sh
python audit/rebuild_pdfs.py
```

Run the finite diagnostics with Python 3 and NumPy:

```sh
python audit/verify_subjects.py
```

The second command covers the three authored subject cores and writes Verification_Results.json beside the script. These computations are diagnostics, not formal proof verification.

The other scripts preserve the original multi-subject production workflow. They expect its output/ and research/ directory layout and retrieved MathNet JSON cache, which is not included in this package. They are provenance records, not standalone downloaders. The original raw statements are preserved in problems/ and Collected_Source_Problems.md; logged compatibility changes affect the printable collection only. Re-fetching the source URLs may produce a different or unavailable snapshot.

SHA256SUMS.txt checksums all package files except itself. It records the released files; rebuilding a PDF may change its binary checksum because of tool versions and creation timestamps. Verify the release from the package root using sha256sum -c SHA256SUMS.txt on systems that provide it.
