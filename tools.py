import logging


logger = logging.getLogger(__name__)
FORMAT = "[%(funcName)20s() ] %(message)s"
formatter = logging.Formatter(FORMAT)


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

