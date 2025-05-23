from fastapi import FastAPI
from .routers import task
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fluxo Task API")

# Include routers
app.include_router(task.router)