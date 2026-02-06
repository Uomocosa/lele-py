import lele
from lele.Path import P
import os
import shutil

def delete_path(path) -> None:
	path = P(path)
	if path.is_dir():
		try:
			os.access(path, os.W_OK)
			shutil.rmtree(path)
		except PermissionError as e:
			lele.Subprocess.hard_delete_path(path)
	else:
		os.chmod(path, 0o777)
		os.remove(path)


import pytest
@pytest.mark.todo
def test_delete_path(path):
	pass
