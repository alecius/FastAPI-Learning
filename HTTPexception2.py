from fastapi import FastAPI,HTTPException,requests
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFound(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UserNotFound)
def user_not_found_handler(request:requests,exc:UserNotFound):
    return JSONResponse(
        status_code =404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )

@app.get("/user{name}")
def get_user(name:str):
    if name!="harshit":
        raise UserNotFound(name)
    return {
        "name":name
    }