from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump()) # **task.dict()
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task : 
        return None
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) : 
    db_task = get_task(db, task_id)
    if db_task: 
        db.delete(db_task)
        db.commit()
    return db_task