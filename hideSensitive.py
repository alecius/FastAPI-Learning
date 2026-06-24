from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users =[]

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.post("/user")
def post_user(user:User):
    users.append(user)
    return user

@app.get("/user", response_model=UserResponse)
def get_user():
    return users[-1]
    
