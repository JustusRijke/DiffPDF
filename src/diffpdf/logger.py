import logging

LOG_FORMAT = (
    "%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d (%(funcName)s): %(message)s"
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(verbose: bool) -> logging.Logger:
    if verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)

    return logger
