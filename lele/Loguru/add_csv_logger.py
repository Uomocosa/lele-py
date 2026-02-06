from loguru import logger
from pathlib import Path

def add_csv_logger(csv_file: Path, csv_header: str, label: str):
    assert csv_file.suffix == ".csv"
    assert label == label.upper(), "Label must be uppercase"
    
    if not csv_file.exists():
        csv_file.parent.mkdir(parents=True, exist_ok=True)
        if not csv_header.endswith("\n"): csv_header += "\n"
        csv_file.write_text(csv_header)

    csv_format = "{message}" 
    logger.add(
        csv_file, 
        format=csv_format, 
        filter=lambda record: record["extra"].get("type") == label,
        level="TRACE"
    )



import pytest
@pytest.mark.todo
def test_():
    from lele.Loguru.__global__ import HELPER_DIR
    csv_file = HELPER_DIR / "Tests" / "test.csv"
    add_csv_logger(
        csv_file = csv_file, 
        csv_header = "message", 
        label = "COOL_LABEL")
    logger.bind(type="COOL_LABEL").trace("Test message")
    assert csv_file.read_text().strip().endswith("Test message")
