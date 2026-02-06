import lele
import json
from pathlib import Path

def save_dict_to_jsonc_file(
    dict: dict, 
    path: Path, 
    header: str = None
):
    path = lele.P(path)
    assert path.suffix == ".jsonc"
    
    if header: header = "// " + str(header) + "\n"
    else: header = ""
    
    def json_serializer(obj):
        match obj:
            case Path(): return str(obj)
            case tuple(): return list(obj)
            # case _ if callable(obj): return f"<Callable {getattr(obj, '__name__', 'lambda')}>"
            case _: return f"Type {type(obj)} not serializable"
        
    json_str = json.dumps(dict, default=json_serializer, indent=4)
    path.write_text(header + json_str)





def test_():
    from lele.Json.__global__ import HELPER_DIR
    path = HELPER_DIR/"Json"/"save_dict_to_jsonc_file.jsonc"
    data = {
        "here": lele.P('.'),
        "a": 1,
        "b": 2,
        3: "c",
    }
    save_dict_to_jsonc_file(
        dict=data,
        path=path,
        header="TEST"
    )
    print(path.read_text())

def test_callable_data():
    from lele.Json.__global__ import HELPER_DIR
    path = HELPER_DIR/"Json"/"save_dict_with_callable_to_jsonc_file.jsonc"
    data = {
        "function": lele.P,
        "arg": ".",
        "result": lele.P('.'),
    }
    save_dict_to_jsonc_file(
        dict=data,
        path=path,
        header="TEST"
    )
    print(path.read_text())
