from fastapi import APIRouter, Request
from .. import auth
router = APIRouter(tags=["Auths"])

@router.get("/login")
def login(request: Request):    
    return auth.login(request)