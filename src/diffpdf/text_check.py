import difflib
import sys
from pathlib import Path

import fitz


def extract_text(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()


def generate_diff(ref_text: str, actual_text: str) -> str:
    ref_lines = ref_text.splitlines(keepends=True)
    actual_lines = actual_text.splitlines(keepends=True)

    diff = difflib.unified_diff(
        ref_lines,
        actual_lines,
        fromfile="reference.pdf",
        tofile="actual.pdf",
        lineterm="",
    )

    return "".join(diff)


def check_text_content(ref: Path, actual: Path, logger) -> None:
    logger.info("[3/4] Checking text content...")

    ref_text = extract_text(ref)
    actual_text = extract_text(actual)

    if ref_text != actual_text:
        diff = generate_diff(ref_text, actual_text)
        logger.error("Text content mismatch")
        for line in diff.splitlines():
            logger.error(line)
        sys.exit(1)

    logger.info("Text content matches")
