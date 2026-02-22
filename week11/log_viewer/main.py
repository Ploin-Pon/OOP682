import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.factory import SourceFactory
from services.file_source import FileLogSource
from services.mock_source import MockLogSource
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # แก้ไขตรงนี้: ให้ชี้ไปที่ Path ของไฟล์ logs.txt ของคุณ
    # หากไฟล์อยู่ที่ log_viewer/logs/logs.txt ให้ใส่ path ตามนั้น
    #source = FileLogSource("logs/logs.txt")  # หรือใช้ SourceFactory.create_source("file") ก็ได้
    source = MockLogSource()
    # Inject เข้าไปใน UI
    window = MainWindow(source)
    window.show()

    sys.exit(app.exec())