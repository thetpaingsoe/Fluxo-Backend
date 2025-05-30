from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel) : 
    name : str
    start_time : datetime
    end_time : Optional[datetime] = None

class TaskCreate(TaskBase) : 
    pass

class TaskUpdate(BaseModel) : 
    name : Optional[str] = None
    start_time : Optional[datetime] = None
    end_time : Optional[datetime] = None

class TaskOut(TaskBase) : 
    id : int
    created_at: datetime

    class Config : 
        orm_mode = True
