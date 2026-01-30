import difflib
import logging
import re
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


def check_text_content(ref: Path, actual: Path, output_dir: Path | None) -> bool:
    logger = logging.getLogger()
    # Extract text and remove whitespace
    ref_text = re.sub(r"\s+", " ", extract_text(ref)).strip()
    actual_text = re.sub(r"\s+", " ", extract_text(actual)).strip()

    if ref_text != actual_text:
        diff = generate_diff(ref_text, ref, actual_text, actual)
        diff_text = "\n".join(diff)

        if output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            diff_file = output_dir / f"{ref.stem}_vs_{actual.stem}_text_diff.txt"
            diff_file.write_text(diff_text, encoding="utf-8")

        logger.error(f"Text content mismatch:\n {diff_text}")
        return False

    logger.info("Text content identical")
    return True
