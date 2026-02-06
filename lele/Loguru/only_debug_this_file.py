import lele
from lele.Path import P
from pathlib import Path
from loguru import logger
import sys

def only_debug_this_file(path: Path):
    path = P(path)
    logger.remove()
    logger.add(
        sys.__stderr__, 
        filter=lele.Loguru.debug_specific_files([path.name])
    )
