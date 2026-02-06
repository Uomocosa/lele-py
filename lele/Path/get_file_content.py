from lele.Path import P

def get_file_content(file_Path, encoding='utf-8'):
    file_Path = P(file_Path)
    return file_Path.read_text(encoding)

import pytest
@pytest.mark.todo
def test_():
    pass
