import os

from api.app.config import PROJECT_ROOT_PATH, DEBUG_MODE
from loguru import logger

logger.add(os.path.join(PROJECT_ROOT_PATH, "api/logs/root.log"), level=DEBUG_MODE)
