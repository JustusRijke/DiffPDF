import sys
from pathlib import Path

import click

from .comparators import compare_pdfs
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
    default="./",
    help="Diff image output directory",
)
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Increase verbosity (-v for INFO, -vv for DEBUG)",
)
@click.option("--save-log", is_flag=True, help="Write log output to log.txt")
@click.version_option(package_name="diffpdf")
def cli(reference, actual, threshold, dpi, output_dir, verbosity, save_log):
    """Compare two PDF files for structural, textual, and visual differences."""
    logger = setup_logging(verbosity, save_log)
    logger.debug("Debug logging enabled")

    try:
        compare_pdfs(reference, actual, threshold, dpi, output_dir, logger)
    except Exception as e:  # pragma: no cover
        logger.critical(f"Error: {e}", exc_info=True)
        sys.exit(2)
