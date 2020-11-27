import logging
import os
import sys
from logging import handlers
from datetime import datetime


def get_logger(ar_log_path, ar_file_name="Unknow", ar_log_level=10):
    log_name = os.path.join(ar_log_path, "{}_{}.log".format(ar_file_name, datetime.now().strftime("%Y%m%d%H%M%S")))
    try:

        logger = logging.getLogger(ar_file_name)
        logger.setLevel(ar_log_level)
        log_format = logging.Formatter("%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s")

        login_stream_handler = logging.StreamHandler(sys.stdout)
        login_stream_handler.setFormatter(log_format)
        logger.addHandler(login_stream_handler)

        file_handler = handlers.RotatingFileHandler(log_name, maxBytes=(1048576 * 5), backupCount=7)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    except Exception as Exc:
        print(str(Exc))
        logger = None
    return logger
