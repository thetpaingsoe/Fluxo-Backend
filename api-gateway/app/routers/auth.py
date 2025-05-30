from fastapi import APIRouter
import httpx

router = APIRouter(prefix="", tags=["Auth"])

@router.get("/login")
async def login():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://auth-service:8000/login")
        return response.json()
