from interfaces.data_source import ILogSource
from services.file_source import FileLogSource
from services.mock_source import MockLogSource

class SourceFactory:
    @staticmethod
    def create_source(source_type: str) -> ILogSource:
        if source_type == "file":
            return FileLogSource("app.log")
        elif source_type == "mock":
            return MockLogSource()
        else:
            raise ValueError("Unknown type")
# Strategy Interface