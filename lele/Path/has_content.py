from pathlib import Path
import os
from lele.Path import P


def has_content(path: Path):
    path = P(path)
    assert path.exists()
    if path.is_file(): return os.path.getsize(path) >= 0
    elif path.is_dir(): return path.stat().st_size >= 0


import pytest
@pytest.mark.todo
def test_():
    pass
