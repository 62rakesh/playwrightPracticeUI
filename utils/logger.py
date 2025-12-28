import logging
import os
from datetime import datetime


class Logger:

    @staticmethod
    def get_logger(name):
        logs_dir = "reports/logs"
        os.makedirs(logs_dir, exist_ok=True)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            timestamp = datetime.now().strftime("%y-%m-%d")
            log_file = os.path.join(logs_dir, f"test_execution_{timestamp}.log")

            file_handler = logging.FileHandler(log_file)
            console_handler = logging.StreamHandler()

            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
