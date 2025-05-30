from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
async def get_tasks():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://task-service:8000/tasks/")
            response.raise_for_status()
            tasks = response.json()
            return tasks  # Directly return the list
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {str(e)}")
    
@router.get("/{task_id}")
async def get_task(task_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://task-service:8000/tasks/{task_id}")
            response.raise_for_status()
            task = response.json()
            return task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching task {task_id}: {str(e)}")

@router.post("/")
async def create_task(task: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://task-service:8000/tasks/", json=task)
            response.raise_for_status()
            created_task = response.json()
            return created_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")

@router.put("/{task_id}")
async def update_task(task_id: int, task: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://task-service:8000/tasks/{task_id}", json=task)
            response.raise_for_status()
            updated_task = response.json()
            return updated_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error updating task {task_id}: {str(e)}")

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://task-service:8000/tasks/{task_id}")
            response.raise_for_status()
            deleted_task = response.json()
            return deleted_task
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task {task_id}: {str(e)}")
