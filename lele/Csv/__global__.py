import lele

THIS_FOLDER = lele.P(__file__).parent
HELPER_DIR = THIS_FOLDER/'__HELPER_DIR__'
INPUT_CSV = HELPER_DIR/'test_input.csv'

assert HELPER_DIR.exists()
assert INPUT_CSV.exists()

def test_():
    pass
