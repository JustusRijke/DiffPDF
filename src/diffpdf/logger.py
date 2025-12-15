import logging

import colorlog

LOG_FORMAT = (
    "%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d (%(funcName)s): %(message)s"
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_COLORS = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "red,bg_white",
}


def setup_logging(verbosity, save_log):
    if verbosity == 0:
        level = logging.WARNING
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG

    formatter = colorlog.ColoredFormatter(
        f"%(log_color)s{LOG_FORMAT}%(reset)s",
        datefmt=DATE_FORMAT,
        log_colors=LOG_COLORS,
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)

    if save_log:  # pragma: no cover
        file_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
        file_handler = logging.FileHandler("log.txt")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
