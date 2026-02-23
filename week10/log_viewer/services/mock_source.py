from abc import ABC, abstractmethod
import csv
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
class CsvLogSource(ILogSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_logs(self) -> List[str]:
        logs = []
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                # ใช้ csv.reader เพื่ออ่านไฟล์ csv
                reader = csv.reader(f)
                for row in reader:
                    if row:  # ตรวจสอบว่าบรรทัดไม่ว่าง
                        # สมมติว่าไฟล์ CSV มีคอลัมน์เดียว หรือต้องการรวมทุกคอลัมน์
                        logs.append(" | ".join(row)) 
            return logs
        except FileNotFoundError:
            return ["Error: ไม่พบไฟล์ CSV"]
        except Exception as e:
            return [f"Error: เกิดข้อผิดพลาดในการอ่าน CSV ({str(e)})"]