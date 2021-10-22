import logging
import sys

FORMATTER = logging.Formatter("%(asctime)5s — %(name)15s — %(levelname)5s — %(message)s")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    return logger
