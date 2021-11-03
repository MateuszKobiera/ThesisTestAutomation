import logging

FORMATTER = logging.Formatter("%(asctime)5s — %(name)15s — %(levelname)5s — %(message)s")


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    return logger
