import logging
import sys
from pathlib import Path

import click
import colorlog

from .comparators import compare_pdfs


def setup_logging(debug, save_log):  # pragma: no cover
    level = logging.DEBUG if debug else logging.INFO

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)-8s%(reset)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)

    if save_log:
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler = logging.FileHandler("log.txt")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


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
@click.option("--debug", is_flag=True, help="Verbose logging")
@click.option("--save-log", is_flag=True, help="Write log output to log.txt")
@click.version_option(package_name="diffpdf")
def cli(reference, actual, threshold, dpi, output_dir, debug, save_log):
    """Compare two PDF files for structural, textual, and visual differences."""
    logger = setup_logging(debug, save_log)

    try:
        compare_pdfs(reference, actual, threshold, dpi, output_dir, logger)
    except Exception as e:  # pragma: no cover
        logger.critical(f"Error: {e}")
        sys.exit(2)
