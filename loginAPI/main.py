from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db
from model import User
from schema import register,login
from auth import password_hash,password_verify

app = FastAPI()


#REGISTER API
@app.post("/register")
def register_api(user_create:register,db:Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == user_create.username).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exits"
        )
    hash_password = password_hash(user_create.password)

    new_user = User(
        username = user_create.username,
        password = hash_password
    )

    db.add(new_user)
    db.commit()

    return{
        "message" : "USER CREATED"
    }

#LOGIN API
@app.post("/login")
def login_api(login_user:login,db:Session= Depends(get_db)):
    db_user = db.query(User).filter(User.username == login_user.username).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invaild username and password"
        )
    
    if not password_verify(login_user.password,db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid username and pasword"
        )
    
    return {
        "message": "login Successfully"
    }