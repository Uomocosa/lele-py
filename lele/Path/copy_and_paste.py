import lele
from lele import __my_variables__ as myvars
from lele.Path import P
import shutil
from loguru import logger


def copy_and_paste(src, dst):
	src = P(src)
	logger.debug(f"src:\n\t'{src}'")
	dst = P(dst)
	logger.debug(f"dst:\n\t'{dst}'")
	assert src.exists()
	if src.is_dir():
		shutil.copytree(
			src,
			dst,
			dirs_exist_ok=True,
		)
	else:
		shutil.copy2(
			src,
			dst,
		)


import pytest
@pytest.mark.todo
def test_():
	pass
