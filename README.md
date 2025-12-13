# DiffPDF

[![CI](https://github.com/JustusRijke/DiffPDF/actions/workflows/ci.yml/badge.svg)](https://github.com/JustusRijke/DiffPDF/actions/workflows/ci.yml)

CLI tool for detecting structural, textual, and visual differences between PDF files, for use in automatic regression tests.

## Installation

```bash
pip install diffpdf
```

## Usage

```bash
diffpdf <baseline.pdf> <actual.pdf> [OPTIONS]
```

## How It Works

DiffPDF uses a fail-fast sequential pipeline to compare PDFs:

1. **Hash Check** — SHA-256 comparison. If identical, exit immediately with pass.
2. **Page Count** — Verify both PDFs have the same number of pages.
3. **Text Content** — Extract and compare text from all pages.
4. **Visual Check** — Render pages to images and compare using pixelmatch.

Each stage only runs if all previous stages pass.

**⚠️ Performance Warning:** The Python port of pixelmatch is extremely slow.

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--threshold` | 0.1 | Pixelmatch threshold (0.0-1.0) |
| `--dpi` | 96 | Render resolution |
| `--output-dir` | ./ | Directory for diff images |
| `--debug` | - | Verbose logging |
| `--save-log` | - | Write log to log.txt |

## Exit Codes

- `0` — Pass (PDFs are equivalent)
- `1` — Fail (differences detected)
- `2` — Error (invalid input or processing error)

## Development

```bash
pip install -e .[dev]
pytest tests/ -v
ruff check .
```

## Acknowledgements

Built with [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing and [pixelmatch-py](https://github.com/whtsky/pixelmatch-py) (Python port of [pixelmatch](https://github.com/mapbox/pixelmatch)) for visual comparison.
