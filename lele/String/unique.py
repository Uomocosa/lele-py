import datetime, time


def unique():
    out = list()
    now = datetime.datetime.now()
    unique_str = now.strftime("%Y_%m_%d_%H%M%S_%f")
    time.sleep(0.0000000000000001)
    return unique_str


def test_():
    a = unique()
    b = unique()
    assert a != b
