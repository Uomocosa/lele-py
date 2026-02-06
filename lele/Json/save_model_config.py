import json
from pathlib import Path
from lele.String import P
from lele.Json import save_dict_to_json_file

def save_model_config(config: dict, file: Path):
    file_Path = P(file)
    config_ = config.copy()
    device = config_.pop("device")
    proper_config = {device: config_}
    save_dict_to_json_file(proper_config, file_Path)


def test_():
    from lele.Json.__global__ import HELPER_DIR
    config = {
        "device": "cpu",
        "path": P('.'),
        "epochs": 10,
        "hello there!": "general kenobi",
    }
    save_model_config(config, HELPER_DIR/"Json"/"save_model_config.json")
