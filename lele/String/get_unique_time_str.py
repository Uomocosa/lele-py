import datetime, time
from loguru import logger

def get_unique_time_str():
	out = list()
	now = datetime.datetime.now()
	unique_str = now.strftime("%Y_%m_%d_%H%M%S_%f")
	time.sleep(0.0000000000000001)
	return unique_str


def test_():
    a = get_unique_time_str()
    b = get_unique_time_str()
    c = get_unique_time_str()
    logger.debug(f"string_a = {a}")
    logger.debug(f"string_b = {b}")
    logger.debug(f"string_c = {c}")
    assert a != b
    assert b != c
    assert a != c
