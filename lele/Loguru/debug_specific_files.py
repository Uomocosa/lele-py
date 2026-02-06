from loguru import logger
from typing import List

def debug_specific_files(file_names:List[str]):
    def filter(record):
        if record["level"].name != "DEBUG":
            return True
        record_file_name = str(record["file"].name)
        record_file_stem = str(record["file"].name)
        if record_file_stem.endswith(".py"): 
            record_file_stem = record_file_stem.removesuffix(".py")
        if record_file_name in file_names:
            return True
        if record_file_stem in file_names:
            return True
        return False
    return filter

import pytest
@pytest.mark.todo
def test_():
    pass
