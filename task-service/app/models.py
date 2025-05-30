from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Task(Base) : 
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
