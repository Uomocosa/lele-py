from typing import List, Callable
from loguru import logger

def enable_specific_functions(functions: List[Callable]):
    logger.disable("") # disable ALL
    for f in functions:
        logger.enable(f"{f.__module__}")

import pytest
@pytest.mark.todo
def test_():
    pass
