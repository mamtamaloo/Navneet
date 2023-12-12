from loguru import logger

from src.constants.constants import LOGURU_FORMAT, LOGURU_LOG_FILE_PATH, LOGURU_ROTATION

logger.add(LOGURU_LOG_FILE_PATH, format=LOGURU_FORMAT, rotation=LOGURU_ROTATION)
