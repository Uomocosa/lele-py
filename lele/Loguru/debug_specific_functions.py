from loguru import logger

def debug_specific_functions(func_names:list):
    def filter(record):
        if record["level"].name != "DEBUG":
            return True
        if record["name"] in func_names:
            return True
        return False
    return filter

import pytest
@pytest.mark.todo
def test_():
    pass
