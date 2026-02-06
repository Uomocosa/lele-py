from pathlib import Path
import os, sys
from loguru import logger

def setup_logger_with_debug_option(file: Path, debug=False):
    logger.remove()
    current_file_path = os.path.abspath(file)
    def filer(record):
        if record["level"].no >= logger.level("WARNING").no:
            return True
        if record["file"].path == current_file_path:
            return True
        return False
            
    logger.add(
        sys.__stderr__, 
        level="DEBUG" if debug else "INFO", 
        format = (
            "<green>{time:HH:mm:ss}</green> | "
            "<level>{message}</level>"
        ),
        filter = filer
    )
    logger.info("Logger setup complete")
