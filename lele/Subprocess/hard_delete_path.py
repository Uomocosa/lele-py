from lele.Subprocess import run_shell_command
import subprocess
import os
from pathlib import Path


def hard_delete_path(path, raise_error=False):
	path = Path(path).absolute()
	if not os.path.exists(path): 
		if not raise_error: return
		err_msg  = f"Path NOT FOUND\n"
		err_msg += f">>> Path:\n\t{path}\n"
		raise FileNotFoundError(err_msg)
	run_shell_command(f"rd /s /q \"{path}\"")
	

import pytest
@pytest.mark.todo
def test_():
	pass
