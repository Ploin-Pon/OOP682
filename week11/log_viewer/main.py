import sys
from PySide6.QtWidgets import QApplication
from services.file_source import FileLogSource
from services.mock_source import MockLogSource
from ui.main_window import MainWindow


def main():
    print("Hello from log-viewer!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = MockLogSource()
    log = FileLogSource("logs/voters.log")
    viewer = MainWindow(log)
    viewer.show()
    app.exec()
