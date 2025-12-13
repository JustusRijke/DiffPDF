import sys
from pathlib import Path

import fitz


def get_page_count(pdf_path: Path) -> int:
    doc = fitz.open(pdf_path)
    count = len(doc)
    doc.close()
    return count


def check_page_counts(ref: Path, actual: Path, logger) -> None:
    logger.info("[2/4] Checking page counts...")

    ref_count = get_page_count(ref)
    actual_count = get_page_count(actual)

    if ref_count != actual_count:
        logger.error(f"Page count mismatch: expected {ref_count}, got {actual_count}")
        sys.exit(1)

    logger.info(f"Page counts match ({ref_count} pages)")
