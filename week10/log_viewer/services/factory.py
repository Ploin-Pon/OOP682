from interfaces.data_source import ILogSource
from services.file_source import FileLogSource
from services.mock_source import CsvLogSource, MockLogSource

class SourceFactory:
    @staticmethod
    def create_source(source_type: str, path: str = None):
        if source_type == "mock":
            return MockLogSource()
        elif source_type == "file":
            return FileLogSource(path or "logs.txt")
        elif source_type == "csv":
            return CsvLogSource(path or "logs.csv") # เพิ่มเงื่อนไขนี้เข้าไป
        else:
            raise ValueError(f"Unknown source type: {source_type}")