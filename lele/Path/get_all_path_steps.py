import lele
from pathlib import Path
from typing import List

def get_all_path_steps(path: Path) -> List[str]:
    """
    Returns all suffix paths of increasing length.
    e.g. "a/b/c" -> ["c", "b/c", "a/b/c"]
    """
    parts = Path(path).parts
    steps = []
    for i in range(1, len(parts) + 1):
        partial_path = Path(*parts[-i:])
        steps.append(partial_path.as_posix())
    return steps

import pytest
@pytest.mark.parametrize("input,expected", [
    ("a/b/c", ["c", "b/c", "a/b/c"]),
    ("home", ["home"]),
    ("home/user", ["user", "home/user"]),
    ("home/user/documents", ["documents", "user/documents", "home/user/documents"]),
])
def test_get_all_path_steps(input,expected):
    assert get_all_path_steps(input) == expected
