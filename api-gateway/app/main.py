from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/")
async def get_home():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8000")
        return response.json()

@app.get("/tasks")
async def get_tasks():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://task-service:8000/tasks/")
            response.raise_for_status()
            tasks = response.json()
            return tasks  # Directly return the list
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {str(e)}")
    
@app.get("/test")
async def get_test():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://task-service:8000/tasks/test/1")
        return response.json()

@app.get("/login")
async def login():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8000/login")
        return response.json()
