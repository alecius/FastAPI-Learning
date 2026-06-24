from fastapi import FastAPI,Depends,HTTPException
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

fake_dbuser = {
    "username" : "harshit",
    "password" : "1234"
}

secret_key = "mysecretkey"  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data:dict):
    return jwt.encode(
        data,
        secret_key,
        algorithm="HS256"   
    )

def verify_token(token:str):
    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms="HS256"
        )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail= "Invalid Token"
        )

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    if(
        form_data.username != fake_dbuser["username"]
        or
        form_data.password != fake_dbuser["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    access_token =  create_token({
        "user":form_data.username
    })

    return{
        "access_token":access_token,
        "token_type":"bearer"
    }

@app.get("/profile")
def profile(token:str = Depends(oauth2_scheme) ):
    payload = verify_token(token)

    return{
        "message":"protected route",
        "user":payload["user"]
    }
