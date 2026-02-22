from abc import ABC, abstractmethod
from typing import List
class ILogSource(ABC):
    @abstractmethod
    def get_logs(self) -> List[str]:
        pass
    
class FileLogSource(ILogSource):
    def __init__(self, filepath):
        self.filepath = filepath

    def get_logs(self) -> List[str]:
        try:
            with open(self.filepath, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return ["Error: File not found"]
class MockLogSource(ILogSource):
    def get_logs(self) -> List[str]:
        return [
            "[INFO] System started",
            "[WARN] Memory usage high",
            "[ERROR] Connection lost"
        ]