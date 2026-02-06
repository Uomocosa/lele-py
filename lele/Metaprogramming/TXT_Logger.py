import warnings
from pathlib import Path
from lele.Path import P, has_content

def test_():
    from lele.Metaprogramming.__global__ import HELPER_DIR
    txt_file = HELPER_DIR / "Metaprogramming" / "txt_logger_test.txt"
    txt_logger = TXT_Logger(txt_file)
    assert txt_file.exists()
    assert txt_file.read_text('utf-8') == ""
    txt_logger.append("first_row")
    txt_logger.append("second_row\nthird_row")
    assert txt_file.read_text('utf-8') == "first_row\nsecond_row\nthird_row\n"


class TXT_Logger:
    def __init__(self, txt_file_Path: Path, create_new_file=True):
        self.txt_file_Path = P(txt_file_Path)
        self.create_new_file = create_new_file
        self._initialize_file()

    def _initialize_file(self):
        assert self.txt_file_Path.suffix == ".txt", f"File must be .txt, got {self.txt_file_Path.suffix}"
        self.txt_file_Path.parent.mkdir(parents=True, exist_ok=True)
        if self.create_new_file:
            self._clear_file()
        elif not self.txt_file_Path.exists():
            self._clear_file() # Create empty file if it doesn't exist even if append mode was requested

    def _clear_file(self):
        with open(self.txt_file_Path, 'w', encoding='utf-8') as f:
            pass 

    def append(self, line: str):
        with open(self.txt_file_Path, 'a', encoding='utf-8') as f:
            f.write(line+"\n")
            f.flush()
