import difflib
import re
import sys
from pathlib import Path
from typing import Iterable

import fitz


def extract_text(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()


def generate_diff(
    ref_text: str, ref: Path, actual_text: str, actual: Path
) -> Iterable[str]:
    ref_lines = ref_text.splitlines(keepends=True)
    actual_lines = actual_text.splitlines(keepends=True)

    diff = difflib.unified_diff(
        ref_lines,
        actual_lines,
        fromfile=ref.name,
        tofile=actual.name,
        lineterm="",
    )

    return diff


def check_text_content(ref: Path, actual: Path, logger) -> None:
    logger.info("[3/4] Checking text content...")

    # Extract text and remove whitespace
    ref_text = re.sub(r"\s+", " ", extract_text(ref)).strip()
    actual_text = re.sub(r"\s+", " ", extract_text(actual)).strip()

    if ref_text != actual_text:
        diff = generate_diff(ref_text, ref, actual_text, actual)
        diff_text = "\n".join(diff)
        logger.error(f"Text content mismatch:\n {diff_text}")
        sys.exit(1)

    logger.info("Text content matches")
