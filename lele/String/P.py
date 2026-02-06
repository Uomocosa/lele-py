from pathlib import Path


def P(path): return Path(path).resolve()


def test_():
    P('.')
    assert P('../') == Path('.').resolve().parent
    assert P('../../') == Path('.').resolve().parent.parent
    assert P('../../../') == Path('.').resolve().parent.parent.parent