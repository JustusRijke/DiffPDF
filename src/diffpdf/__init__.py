from importlib.metadata import version
from pathlib import Path

from .hash_check import check_hash
from .logger import setup_logging
from .page_check import check_page_counts
from .text_check import check_text_content
from .visual_check import check_visual_content

__version__ = version("diffpdf")


def diffpdf(
    reference: str | Path,
    actual: str | Path,
    threshold: float = 0.1,
    dpi: int = 96,
    output_dir: str | Path | None = None,
    verbose: bool = False,
) -> bool:
    ref_path = Path(reference) if isinstance(reference, str) else reference
    actual_path = Path(actual) if isinstance(actual, str) else actual
    out_path = Path(output_dir) if isinstance(output_dir, str) else output_dir

    logger = setup_logging(verbose)

    logger.info("[1/4] Checking file hashes...")
    if check_hash(ref_path, actual_path):
        logger.info("Files are identical (hash match)")
        return True
    logger.info("Hashes differ, continuing checks")

    logger.info("[2/4] Checking page counts...")
    if not check_page_counts(ref_path, actual_path):
        return False

    logger.info("[3/4] Checking text content...")
    if not check_text_content(ref_path, actual_path, out_path):
        return False

    logger.info("[4/4] Checking visual content...")
    if not check_visual_content(ref_path, actual_path, threshold, dpi, out_path):
        return False

    logger.info("PDFs are equivalent")
    return True


__all__ = ["diffpdf", "__version__"]
