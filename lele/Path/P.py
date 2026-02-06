from pathlib import Path

def P(path: str) -> Path:
    return Path(path).absolute()


def test_():
    pass