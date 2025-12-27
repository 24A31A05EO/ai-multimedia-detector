import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-detector")

def log_event(message: str):
    logger.info(message)
