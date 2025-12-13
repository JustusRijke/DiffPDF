import sys
from pathlib import Path

from .hash_check import check_hash
from .page_check import check_page_counts
from .text_check import check_text_content
from .visual_check import check_visual_content


def compare_pdfs(
    ref: Path, actual: Path, threshold: float, dpi: int, output_dir: Path, logger
) -> None:
    check_hash(ref, actual, logger)

    check_page_counts(ref, actual, logger)

    check_text_content(ref, actual, logger)

    check_visual_content(ref, actual, threshold, dpi, output_dir, logger)

    logger.info("PDFs are equivalent")
    sys.exit(0)
