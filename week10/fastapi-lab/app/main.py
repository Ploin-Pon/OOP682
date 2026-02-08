from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import SqlTaskRepository
from .services import TaskService
from . import models_orm 
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency Provider
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

# เพิ่มอันนี้กลับมาด้วย (เพราะในรูปมี แต่ในโค้ดคุณหายไป)
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(
    task_id: int, 
    service: TaskService = Depends(get_task_service)
):
    return service.get_task_by_id(task_id)

# แก้ไขชื่อฟังก์ชันให้ตรงกับ Service (เติม d)
@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    # แก้ตรงนี้: ต้องมี d (completed)
    return service.mark_task_completed(task_id)