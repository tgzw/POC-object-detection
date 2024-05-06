import logging


def getLogger(name, level=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO if not level else level)

    # Define the custom format
    log_format = "%(asctime)s - %(pathname)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s"

    # Add a console handler if not already added
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)

    return logger
