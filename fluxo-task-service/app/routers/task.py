from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.TaskOut])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id:int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id)

@router.post("/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db : Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None : 
        raise HTTPException(status_code=404, detail="Task Not Found")
    return updated_task

@router.delete("/{task_id}", response_model=schemas.TaskOut)
def delete_task(task_id:int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if deleted_task is None : 
        raise HTTPException(status_code=404, detail="Task Not Found")
    return deleted_task