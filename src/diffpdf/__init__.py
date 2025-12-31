from importlib.metadata import version
from pathlib import Path

from .comparators import compare_pdfs
from .logger import setup_logging

__version__ = version("diffpdf")


def diffpdf(
    reference: str | Path,
    actual: str | Path,
    threshold: float = 0.1,
    dpi: int = 96,
    output_dir: str | Path | None = None,
    verbosity: int = 0,
    save_log: bool = False,
) -> bool:
    ref_path = Path(reference) if isinstance(reference, str) else reference
    actual_path = Path(actual) if isinstance(actual, str) else actual
    out_path = Path(output_dir) if isinstance(output_dir, str) else output_dir

    logger = setup_logging(verbosity, save_log)
    return compare_pdfs(ref_path, actual_path, threshold, dpi, out_path, logger)


__all__ = ["diffpdf", "__version__"]
