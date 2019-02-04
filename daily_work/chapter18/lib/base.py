import logging.config
from conf import setting


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger
