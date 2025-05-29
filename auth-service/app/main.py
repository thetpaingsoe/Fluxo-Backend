from fastapi import FastAPI
from .routers import route

app = FastAPI(title="Fluxo Auth")

app.include_router(route.router)

@app.get("/")
def read_root():
    return {"message": "Hello from root!"}