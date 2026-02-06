import json
from pathlib import Path

def serializer(obj):
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    
    if isinstance(obj, dict):
        return {serializer(k): serializer(v) for k, v in obj.items()}
    
    if isinstance(obj, (list, tuple, set)):
        return [serializer(item) for item in obj]

    if isinstance(obj, Path):
        return str(obj).replace("\\", "/")

    return str(obj)



def test_():
    from lele.Path import P

    json.dumps(serializer([1, "hello", None, True]))
    json.dumps(serializer({"key": "value", "number": 123}))
    json.dumps(serializer(P('.')))
    print(json.dumps(serializer({"key": "value", "inner_dict": {"path": P('.'), "b": 2}})))