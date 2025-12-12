# dashboard/config/logger.py

import logging
from .settings import LOG_LEVEL, LOG_FORMAT

def setup_logger(name: str) -> logging.Logger:
    """Configurar e retornar um logger"""
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    logger = logging.getLogger(name)
    return logger
