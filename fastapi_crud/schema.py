from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str

class UpdateUser(BaseModel):
    name:str
    email:str