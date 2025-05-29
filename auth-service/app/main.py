from fastapi import FastAPI
from .routers import auths

app = FastAPI(title="Fluxo Auth")

app.include_router(auths.router)

@app.get("/")
def read_root():
    return {"message": "Hello from root!"}