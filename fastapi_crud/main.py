from fastapi import FastAPI
from database import SessionLocal
from models import User
from schema import UserCreate,UpdateUser

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Hello Harshit"
    }
    
@app.get("/user/{id}")
def about_user(id:int):  
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()

    return user


@app.post("/user-creation")
def get_user(user:UserCreate):
    db = SessionLocal()

    new_users = User(
        name = user.name,
        email = user.email
    )

    db.add(new_users)
    db.commit()
    return {
        "message":"User Created"
    }

@app.put("/update-user/{id}")
def update_user(id:int,data:UpdateUser):
    db = SessionLocal()

    user = db.query(User).fillter(User.id == id).first()

    user.name == data.name
    user.email == user.email
    db.commit()
    return{
        "message":"Update Successfull"
    }
  
@app.delete("/delete-user/{id}")
def delete_user(id:int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()

    db.delete(user)
    db.commit()

    return{
        "message":"Deletion Completed"
    }


    

    