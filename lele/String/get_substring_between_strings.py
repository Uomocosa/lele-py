import lele
from lele import __my_variables__ as myvars
import re
from loguru import logger


def get_substring_between_strings(text: str, start: str, end: str):
    text = str(text)
    start = str(start)
    end = str(end)
    pattern = rf"{re.escape(start)}(.*?){re.escape(end)}"
    match = re.search(pattern, text, re.DOTALL)
    if match: return match.group(1).strip()
    else: return None


def test_():
    assert get_substring_between_strings("AttestBA", "test", "A") == "B"
    assert get_substring_between_strings("1A21B21C12", "1", "2") == "A"
