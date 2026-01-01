import sys
from pathlib import Path

import click

from . import diffpdf
from .logger import setup_logging


@click.command()
@click.argument(
    "reference", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.argument("actual", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--threshold", type=float, default=0.1, help="Pixelmatch threshold (0.0-1.0)"
)
@click.option("--dpi", type=int, default=96, help="Render resolution")
@click.option(
    "--output-dir",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Diff image output directory (if not specified, no diff images are saved)",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Increase verbosity",
)
@click.version_option(package_name="diffpdf")
def cli(
    reference: Path,
    actual: Path,
    threshold: float,
    dpi: int,
    output_dir: Path | None,
    verbose: bool,
) -> None:
    """Compare two PDF files for structural, textual, and visual differences."""
    try:
        if diffpdf(reference, actual, threshold, dpi, output_dir, verbose):
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:  # pragma: no cover
        logger = setup_logging(verbose)
        logger.critical(f"Error: {e}", exc_info=True)
        sys.exit(2)
