
from fastapi import Request
import jwt

def login(request : Request):
    
    auth = request.headers.get("Authorization")
    

def encode(request : Request):
    # auth = request.headers.get("Authorization")
    # if not auth:
    #     return {"error": "Authorization header is missing"}
    
    try:
        token = jwt.encode({"user": "example_user"}, "secret", algorithm="HS256")
        return {"token": token}
    except Exception as e:
        return {"error": str(e)}
    
def decode(request : Request):
    auth = request.headers.get("Authorization")
    if not auth:
        return {"error": "Authorization header is missing"}
    
    try:
        token = auth.split(" ")[1]  # Assuming the format is "Bearer <token>"
        decoded = jwt.decode(token, "secret", algorithms=["HS256"])
        return {"decoded": decoded}
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    except Exception as e:
        return {"error": str(e)}
