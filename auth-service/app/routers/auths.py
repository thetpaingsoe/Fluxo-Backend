from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Auths"])

@router.get("/login")
def login():
    return {"message": "Hello Auth"}