
from fastapi import Request

def login(request : Request):
    
    auth = request.headers.get("Authorization")
    
    if not auth: 
        return {"message": "Don't have Auth"}
    else :
        return{"message": "Welcome!"}