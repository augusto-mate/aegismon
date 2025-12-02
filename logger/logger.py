# aegismon/logging/logger.py
import logging
from logging.handlers import RotatingFileHandler

def get_logger(name="aegismon", logfile="aegismon.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # File handler with rotation
    fh = RotatingFileHandler(logfile, maxBytes=5*1024*1024, backupCount=3)
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
