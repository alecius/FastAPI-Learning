from pydantic import BaseModel

class register(BaseModel):
    username: str
    password: str

class login(BaseModel):
    username:str
    password:str 
    