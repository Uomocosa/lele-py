import sys
from loguru import logger

def simple_format():
    logger.remove()
    
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>"
    )


def test_():
    simple_format()
    logger.debug("Test message")
    logger.info("Test message")
