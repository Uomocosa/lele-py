import lele
from lele.Path import P

THIS_FOLDER = P(__file__).parent
HELPER_DIR = THIS_FOLDER / '__HELPER_DIR__'

assert THIS_FOLDER.exists()
assert HELPER_DIR.exists()

def test_():
    pass
