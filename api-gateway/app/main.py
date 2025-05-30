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
    
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://task-service:8000/tasks/{task_id}")
            response.raise_for_status()
            task = response.json()
            return task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching task {task_id}: {str(e)}")

@app.post("/tasks")
async def create_task(task: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://task-service:8000/tasks/", json=task)
            response.raise_for_status()
            created_task = response.json()
            return created_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://task-service:8000/tasks/{task_id}", json=task)
            response.raise_for_status()
            updated_task = response.json()
            return updated_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error updating task {task_id}: {str(e)}")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://task-service:8000/tasks/{task_id}")
            response.raise_for_status()
            deleted_task = response.json()
            return deleted_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task {task_id}: {str(e)}")

@app.get("/login")
async def login():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8000/login")
        return response.json()
