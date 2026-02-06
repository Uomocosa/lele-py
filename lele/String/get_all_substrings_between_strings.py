import re
from typing import List

def get_all_substrings_between_strings(text: str, start: str, end: str) -> List[str]:
    text = str(text)
    start = str(start)
    end = str(end)
    pattern = rf"{re.escape(start)}(.*?){re.escape(end)}"
    match = re.search(pattern, text, re.DOTALL)
    match = re.findall(pattern, text, re.DOTALL)
    return match


import pytest
@pytest.mark.parametrize("input,expected", [
    (("AttestBA", "test", "A"), ['B']),
    (("1A21B21C12", "1", "2"), ['A', 'B', 'C1']),
])
def test_(input, expected):
    assert get_all_substrings_between_strings(*input) == expected
