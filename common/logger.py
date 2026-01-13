import logging
import os
import time

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class Logger:
    def __init__(self, name="PytestFramework"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Preventing duplicate log output
        if not self.logger.handlers:
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s')

            fh = logging.FileHandler(os.path.join(LOG_DIR, f"{time.strftime('%Y-%m-%d')}.log"), encoding="utf-8")
            fh.setFormatter(fmt)
            self.logger.addHandler(fh)

            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            self.logger.addHandler(sh)

log = Logger().logger

