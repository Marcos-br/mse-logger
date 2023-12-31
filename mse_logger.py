import logging
import sys
import uuid
import traceback
from logging.handlers import RotatingFileHandler
from datetime import datetime

log_filename = f"logfile_{datetime.now().strftime('%Y-%m')}.log"
file_handler = RotatingFileHandler(
    log_filename, maxBytes=10 * 1024 * 1024, backupCount=5
)
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def mse_logger(func):
    def wrapper(*args, **kwargs):
        execution_uuid = str(uuid.uuid4())

        try:
            logger.info(
                f"{func.__module__}.{func.__name__} - Entrada ({execution_uuid}): {args}, {kwargs}"
            )

            result = func(*args, **kwargs)

            logger.info(
                f"{func.__module__}.{func.__name__} - Saida ({execution_uuid}): {result}"
            )

            return result

        except Exception as e:
            _, _, tb = sys.exc_info()
            extracted_tb = traceback.extract_tb(tb)
            last_line = extracted_tb[-1]

            logger.error(
                f"{func.__module__}.{func.__name__} - Erro ({execution_uuid}): {str(e)}\n"
                f"File: {last_line[0]}, Line: {last_line[1]}, Function: {last_line[2]}, Line Contents: {last_line[3]}, Erro ({execution_uuid}): {str(e)}"
            )

            raise e

    return wrapper
