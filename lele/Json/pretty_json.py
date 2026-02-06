import json
from lele.Json import serializer

print(f"serializer: {serializer}")

def pretty_json(json_dict: dict, indent=4):
    sanitized_dict = json_dict.copy()
    sanitized_dict = {serializer(key): serializer(item) for key, item in sanitized_dict.items()}
    return json.dumps(sanitized_dict, indent=indent)


def test_():
    CONFIG = {
        "comment": "Toy settings for CPU execution",
        "max_dataset_size": 100,
        "batch_size": 32,
        "epochs": 1,
        "learning_rate": 0.01,
        "max_new_tokens": 100,
        "temperature": 1
    }
    print(f"config: {pretty_json(CONFIG)}")
