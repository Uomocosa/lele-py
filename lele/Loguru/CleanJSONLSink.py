import json
from pathlib import Path
from loguru import logger

class CleanJSONLSink:
    def __init__(self, filepath: Path):
        # Open in 'w' mode to start fresh every time you run the example
        filepath.parent.mkdir(parents=True, exist_ok=True)
        self.file = filepath.open("w")
        
    def __call__(self, message):
        # Extract ONLY the bound variables and write as JSON
        json.dump(message.record["extra"], self.file)
        self.file.write("\n")
        self.file.flush()
        
        
import pytest
@pytest.mark.todo
def test_():
    from lele.Loguru.__global__ import HELPER_DIR
    
    def example_fn():
        epoch = 0
        train_loss = 0.1
        val_loss = 0.2
        logger.bind(
            log_type="log_unique_name_1",
            epoch=epoch + 1,
            train_loss=float(train_loss),
            val_loss=float(val_loss)
        ).info("Metrics captured: {extra}", extra=locals())
        
    logger.add(
        CleanJSONLSink(HELPER_DIR/"CleanJSONLSink_test.jsonl"),
        filter=lambda record: record["extra"].get("log_type") == "log_unique_name_1",
        level="TRACE",
    )
    
    example_fn()
