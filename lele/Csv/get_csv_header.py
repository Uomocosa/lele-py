import csv
from pathlib import Path
from loguru import logger

def get_csv_header(csv_file: Path) -> str:
    logger.warning(f"Don't use this function! It just gets the first row of a CSV file.")
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # This grabs the first row
    return header

def test_():
    from .__global__ import INPUT_CSV
    assert get_csv_header(INPUT_CSV) == ['HEADER_1', 'HEADER_2', 'HEADER_3']
