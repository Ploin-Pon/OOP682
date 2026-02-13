'''from PySide6.QtWidgets import QMainWindow
from interfaces.data_source import ILogSource

class MainWindow(QMainWindow):
    # รับ Abstraction เข้ามา (DIP)
    def __init__(self, log_source: ILogSource):
        super().__init__()
        self.log_source = log_source  # Composition
        self.load_logs()
        self.setCentralWidget(self.log_display)
        self.log_display.setReadOnly(True)
        self.log_source = log_source
        self.load_logs()
        self.show()
        

    def load_logs(self):
        # UI ไม่รู้ว่าข้อมูลมาจากไหน รู้แค่ get_logs()
        logs = self.log_source.get_logs()
        self.log_display.setPlainText('\n'.join(logs))'''

from PySide6.QtWidgets import QMainWindow, QTextEdit
from interfaces.data_source import ILogSource

class MainWindow(QMainWindow):
    def __init__(self, log_source: ILogSource):
        super().__init__()
        self.log_source = log_source
        
        # 1. สร้าง Widget ก่อน (ต้องทำก่อนเรียกใช้เสมอ!)
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(False)
        self.setCentralWidget(self.log_display) # เอาไปวางไว้กลางหน้าจอ
        
        self.setWindowTitle("Log Viewer")
        self.resize(600, 400)

        # 2. เมื่อมี Widget แล้ว ถึงจะสั่งโหลดข้อมูลใส่ลงไปได้
        self.load_logs()
        
        self.show()

    def load_logs(self):
        # ดึงข้อมูลผ่าน Interface (DIP)
        logs = self.log_source.get_logs()
        # ตอนนี้ self.log_display ถูกสร้างแล้ว เลยทำงานได้ไม่พัง
        self.log_display.setPlainText('\n'.join(logs))