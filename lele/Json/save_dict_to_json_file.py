import json
from pathlib import Path
from lele.String import P
from lele.Json import serializer


def save_dict_to_json_file(data: dict, file: Path):
    file_Path = P(file)
    file_Path.parent.mkdir(parents=True, exist_ok=True)
    sanitized_data = data.copy()
    sanitized_data = {serializer(key): serializer(item) for key, item in sanitized_data.items()}
    with file_Path.open('w', encoding='utf-8') as f:
        json.dump(sanitized_data, f, indent=4)


def test_():
    from lele.Json.__global__ import HELPER_DIR
    path = HELPER_DIR/"Json"/"save_dict_to_json_file.json"
    data = {
        "here": P('.'),
        "a": 1,
        "b": 2,
        3: "c",
    }
    save_dict_to_json_file(data, path)
    print(path.read_text())
