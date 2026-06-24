from fastapi import FastAPI,Header,HTTPException
from jose import jwt,JWTError
from datetime import datetime,timedelta

app = FastAPI()

secret_key = "MYSECRETKEY"

def create_access_token(username:str):
    expire = datetime.utcnow()+timedelta(minutes=30)
    payload = {
        "sub":username,
        "expire":expire
    }
    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256"
    )
    return token

def token_verify(token:str):
    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms="HS256"
        )
        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    
    
@app.post("/login")
def login(username:str):
    token = create_access_token(username)
            
    return{
        "access_token" : token,
        "token_type" : "bearer"
    }


@app.grt("/profile")
def profile(authorization : str = Header()):
    token = authorization.split(" ")[1]
    payload = token_verify(token)

    return{
        "username" : payload["sub"]
    }
        
    
