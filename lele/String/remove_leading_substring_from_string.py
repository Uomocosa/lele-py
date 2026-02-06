from loguru import logger
import re

def remove_leading_substring_from_string(string, substring):
    if not string: return ''
    return re.sub(rf'^({substring})+', '', string)

import pytest
@pytest.mark.parametrize("input,expected", [
    (("3+5", "3"), "+5"), 
    (("hello", "h"), "ello"), 
    (("<br>", "<br>"), ""), 
])
def test_(input, expected):
    assert remove_leading_substring_from_string(*input) == expected
