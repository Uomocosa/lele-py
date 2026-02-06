from lele.Path import P
from loguru import logger


def search_file(directory, filename):
	dir_Path = P(directory)
	assert dir_Path.exists(), f"Path '{directory}' does not exist"
	assert dir_Path.is_dir(), f"'{directory}' is not a directory"
	filename = str(filename)
	return list(dir_Path.rglob(filename))


def test_():
	from lele import __my_variables__ as myvars
	synchting_Path = myvars.synchting_Path/'Obsidian Vaults'
	filename = "DnD - Index.md"
	file_Paths = search_file(synchting_Path, filename)
	logger.debug(file_Paths)
	assert file_Paths != []
