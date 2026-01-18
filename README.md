# DiffPDF

[![Build](https://github.com/JustusRijke/DiffPDF/actions/workflows/build.yml/badge.svg)](https://github.com/JustusRijke/DiffPDF/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/JustusRijke/DiffPDF/graph/badge.svg?token=O3ZJFG6X7A)](https://codecov.io/gh/JustusRijke/DiffPDF)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/DiffPDF)](https://pypi.org/project/DiffPDF/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/DiffPDF)](https://pypi.org/project/DiffPDF/)

CLI tool for detecting structural, textual, and visual differences between PDF files, for use in automatic regression tests.

## How It Works

DiffPDF uses a fail-fast sequential pipeline to compare PDFs:

1. **Hash Check** - SHA-256 comparison. If identical, exit immediately with pass.
2. **Page Count** - Verify both PDFs have the same number of pages.
3. **Text Content** - Extract and compare text from all pages (ignoring whitespace).
4. **Visual Check** - Render pages to images and compare using [pixelmatch-fast](https://pypi.org/project/pixelmatch-fast/).

Each stage only runs if all previous stages pass.

## Installation

Install Python (v3.10 or higher) and install the package:

```bash
pip install diffpdf
```

## CLI Usage

```bash
Usage: diffpdf [OPTIONS] REFERENCE ACTUAL

  Compare two PDF files for structural, textual, and visual differences.

Options:
  --threshold FLOAT       Pixelmatch threshold (0.0-1.0)
  --dpi INTEGER           Render resolution
  --output-dir DIRECTORY  Diff output directory (saves text diffs and visual diff images on failure)
  -v, --verbose           Increase verbosity
  --version               Show the version and exit.
  --help                  Show this message and exit.
```

### Exit Codes

- `0` — Pass (PDFs are equivalent)
- `1` — Fail (differences detected)
- `2` — Error (invalid input or processing error)

## Library Usage

```python
from diffpdf import diffpdf

# Basic usage (no diff output saved)
diffpdf("reference.pdf", "actual.pdf")

# With options (save text diffs and visual diff images to ./output directory)
diffpdf("reference.pdf", "actual.pdf", output_dir="./output", dpi=300)
```

## Development

Install [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). Then, install dependencies & activate the automatically generated virtual environment:

```bash
uv sync --locked
source .venv/bin/activate
```

Skip `--locked` to use the newest dependencies (this might modify `uv.lock`)

### Testing

Run tests:

```bash
pytest
```

### Quality Assurance (QA)

Automatically run code quality checks before every commit using [pre-commit](https://pre-commit.com/):

```bash
pre-commit install
```

This installs git hooks that run ruff, type checks, and other checks before each commit. You can run manually at any time with:

```bash
pre-commit run --all-files
```

## Acknowledgements

Built with [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing and [pixelmatch-fast](https://pypi.org/project/pixelmatch-fast/) (Python port of [pixelmatch](https://github.com/mapbox/pixelmatch)) for visual comparison.
