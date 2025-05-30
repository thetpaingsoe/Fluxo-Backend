from fastapi import APIRouter, Request
from .. import auth
router = APIRouter(tags=["Auths"])

@router.post("/login")
def login(request: Request):    
    return auth.login(request)

@router.get("/encode")
def encode(request: Request):
    return auth.encode(request)

@router.get("/decode")
def decode(request: Request):
    return auth.decode(request)