import rapidjson
from pathlib import Path
import lele

def get_dict_from_jsonc(path: Path) -> dict:
    assert path.suffix == ".jsonc"
    parse_mode = rapidjson.PM_COMMENTS | rapidjson.PM_TRAILING_COMMAS
    with open(path, 'r') as f:
        config_dict = rapidjson.load(f, parse_mode=parse_mode)
    return config_dict


import pytest
@pytest.mark.todo
def test_(): pass
