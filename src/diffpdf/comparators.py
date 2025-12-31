from pathlib import Path

from .hash_check import check_hash
from .page_check import check_page_counts
from .text_check import check_text_content
from .visual_check import check_visual_content


def compare_pdfs(
    ref: Path, actual: Path, threshold: float, dpi: int, output_dir: Path | None, logger
) -> bool:
    logger.info("[1/4] Checking file hashes...")
    if check_hash(ref, actual):
        logger.info("Files are identical (hash match)")
        return True
    logger.info("Hashes differ, continuing checks")

    logger.info("[2/4] Checking page counts...")
    if not check_page_counts(ref, actual, logger):
        return False

    logger.info("[3/4] Checking text content...")
    if not check_text_content(ref, actual, logger):
        return False

    logger.info("[4/4] Checking visual content...")
    if not check_visual_content(ref, actual, threshold, dpi, output_dir, logger):
        return False

    logger.info("PDFs are equivalent")
    return True
