import logging

import click
import colorlog


def setup_logging(debug, save_log):
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
@click.option("--foobar", type=str, help="Example argument; prints value to stdout")
@click.option("--debug", is_flag=True, help="Set log level to DEBUG")
@click.option("--save-log", is_flag=True, help="Write log output to log.txt")
@click.version_option(package_name="DiffPDF")
def cli(foobar, debug, save_log):
    logger = setup_logging(debug, save_log)

    if foobar:
        print(foobar)

    logger.info("DiffPDF started")
    logger.debug("Debug mode enabled")
