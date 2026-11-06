# Reproduction notes

`verify_examples.py` is self-contained and requires only Python’s standard library. Run it to regenerate the finite checks. These checks do not replace the proofs.

The build scripts document the compilation workflow; they expect the original workspace layout and raw retrieval inputs and are not a turnkey installer. The source ledger supplies the retrieved URLs and bibliographic metadata. PDF typesetting uses Pandoc, XeLaTeX and the supplied header; figures use Matplotlib.

All four PDFs were rendered and representative pages visually inspected. Text bounding boxes were checked on every page for physical-page clipping; missing-glyph build warnings and replacement characters were checked. This is layout QA, not a full independent mathematical or historical audit.
