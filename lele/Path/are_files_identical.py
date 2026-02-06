import filecmp

def are_files_identical(file1, file2): 
    if not file1.exists(): return False
    if not file2.exists(): return False
    return filecmp.cmp(file1, file2, shallow=False)


import pytest
@pytest.mark.todo
def test_():
    pass
