from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()
    
    # เพิ่มฟังก์ชันนี้ (เพราะ main.py เรียกใช้)
    def get_task_by_id(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create_task(self, task_in: TaskCreate):
        # Validation: Check if title already exists
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(
                status_code=400,
                detail=f"Task with title '{task_in.title}' already exists"
            )
        # Business logic could go here
        return self.repo.create(task_in)
    
    # แก้ชื่อ function ให้มี 'd' (completed) ตามที่ main.py เรียก
    def mark_task_completed(self, task_id: int):
        task = self.repo.update_task_complete(task_id)
        if not task:
             raise HTTPException(status_code=404, detail="Task not found")
        return task