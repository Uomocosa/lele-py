import csv
import warnings
from pathlib import Path
from lele.Path import P, has_content

def test_():
    from lele.Metaprogramming.__global__ import HELPER_DIR
    csv_file = HELPER_DIR / "Metaprogramming" / "simple_file.csv"
    csv_logger = CSV_Logger(csv_file, header=["id", "name", "test"], create_new_file=True)
    assert csv_file.exists()
    assert csv_file.read_text('utf-8') == "id,name,test\n"
    csv_logger.append(["0", "A", "this should be printed"])
    csv_logger.append(["1", "B", "this should be printed"])
    assert csv_file.read_text('utf-8') == "id,name,test\n0,A,this should be printed\n1,B,this should be printed\n"


class CSV_Logger():
    def __init__(self, csv_file_Path: Path, header: list=[], create_new_file=False):
        self.csv_file_Path = P(csv_file_Path)
        self.header = header
        self.create_new_file = create_new_file
        self._initialize_file()

    def _initialize_file(self):
        assert self.csv_file_Path.suffix == ".csv"
        self.csv_file_Path.parent.mkdir(exist_ok=True)
        if self.create_new_file: self._create_new_file()
        if self.csv_file_Path.exists() and has_content(self.csv_file_Path):
            with open(self.csv_file_Path, "r") as f: old_header = f.readline().strip()
            if expected_header := ",".join(self.header) != old_header:
                warnings.warn(
                    f"Existing header '{old_header}' in {self.csv_file_Path} "
                    f"does not match expected header '{expected_header}'. "
                    "Appending data may corrupt the file.",
                    UserWarning  # This is a good, specific warning type to use
                )
        else: self._create_new_file()
            
    def _create_new_file(self):
        with open(self.csv_file_Path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            f.flush() # Ensure header is written to disk

    def append(self, data: list):
        assert len(data) == len(self.header)
        with open(self.csv_file_Path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.flush() # Flush buffer to disk immediately
