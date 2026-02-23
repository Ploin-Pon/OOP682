from PySide6.QtWidgets import QMainWindow # หรือ PyQt6
from interfaces.data_source import ILogSource
from PySide6.QtWidgets import *
from abc import ABC, abstractmethod
from typing import List

class MainWindow(QMainWindow):
    # รับ Abstraction เข้ามา (DIP)
    def __init__(self, source: ILogSource):
        super().__init__()
        self.source = source  # Composition
        self.init_ui()
        self.load_data()
        
    def init_ui(self):
        self.setWindowTitle("Log Viewer")
        self.setGeometry(100, 100, 600, 400)
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(10, 10, 580, 380)
    
    def load_data(self):
        # UI ไม่รู้ว่าข้อมูลมาจากไหน รู้แค่ get_logs()
        logs = self.source.get_logs()
        self.list_widget.addItems(logs)

'''class SourceFactory:
    @staticmethod
    def create_source(source_type: str) -> ILogSource:
        if source_type == "file":
            return FileLogSource("app.log")
        elif source_type == "mock":
            return MockLogSource()
        else:
            raise ValueError("Unknown type")
# Strategy Interface'''
class IFilterStrategy(ABC):
    @abstractmethod
    def filter(self, logs: List[str]) -> List[str]:
        pass

# Concrete Strategies
class ErrorOnlyFilter(IFilterStrategy):
    def filter(self, logs):
        return [l for l in logs if "ERROR" in l]

class NoFilter(IFilterStrategy):
    def filter(self, logs):
        return logs