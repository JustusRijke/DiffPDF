# DiffPDF

[![Build](https://github.com/JustusRijke/DiffPDF/actions/workflows/build.yml/badge.svg)](https://github.com/JustusRijke/DiffPDF/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/JustusRijke/DiffPDF/graph/badge.svg?token=O3ZJFG6X7A)](https://codecov.io/gh/JustusRijke/DiffPDF)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CLI tool for detecting structural, textual, and visual differences between PDF files, for use in automatic regression tests.

## How It Works

DiffPDF uses a fail-fast sequential pipeline to compare PDFs:

1. **Hash Check** - SHA-256 comparison. If identical, exit immediately with pass.
2. **Page Count** - Verify both PDFs have the same number of pages.
3. **Text Content** - Extract and compare text from all pages (ignoring whitespace).
4. **Visual Check** - Render pages to images and compare using pixelmatch.

Each stage only runs if all previous stages pass.

**⚠️ Performance Warning:** The Python port of pixelmatch is extremely slow.

## Installation

```bash
pip install diffpdf
```

## CLI Usage
```
Usage: diffpdf [OPTIONS] REFERENCE ACTUAL

  Compare two PDF files for structural, textual, and visual differences.

Options:
  --threshold FLOAT       Pixelmatch threshold (0.0-1.0)
  --dpi INTEGER           Render resolution
  --output-dir DIRECTORY  Diff image output directory
  -v, --verbose           Increase verbosity (-v for INFO, -vv for DEBUG)
  --save-log              Write log output to log.txt
  --version               Show the version and exit.
  --help                  Show this message and exit.
```

**Exit Codes**

- `0` — Pass (PDFs are equivalent)
- `1` — Fail (differences detected)
- `2` — Error (invalid input or processing error)

## Library Usage

Call the CLI from Python:
```python
from diffpdf import main
main(["-vv","foo.pdf", "bar.pdf"])
```

## Development

```bash
pip install -e .[dev]
pytest tests/ -v
ruff check .
```

## Acknowledgements

Built with [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing and [pixelmatch-py](https://github.com/whtsky/pixelmatch-py) (Python port of [pixelmatch](https://github.com/mapbox/pixelmatch)) for visual comparison.
