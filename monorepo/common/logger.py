import datetime
import logging
import os
from monorepo.common.constants import LOGS_PATH


def get_logger(name: str = "sdi", level: str = "INFO", filename: str = "sdi") -> logging.Logger:
    """
        Factory pattern for logger
    """
    now = datetime.datetime.now()
    datetime_suffix = now.strftime("%Y_%m_%d")
    filename_base = os.path.basename(filename)
    if filename_base.find(".py") > 0:
        filename_base = filename_base[:-3]
    log_filename = "{0}_{1}.log".format(filename_base, datetime_suffix)
    log_full_filename = os.path.join(LOGS_PATH, log_filename)
    logging.basicConfig(filename=log_full_filename, filemode='a+', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(name)
    logger.setLevel(logging._nameToLevel.get(level))
    return logger
    


