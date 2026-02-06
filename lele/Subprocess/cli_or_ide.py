import sys

def cli_or_ide():
    if sys.stdin.isatty(): return 'cli'
    else: return 'ide'

import pytest
@pytest.mark.skip(reason="not easy to test")
def test_():
    pass
