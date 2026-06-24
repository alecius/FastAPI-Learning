from fastapi import FastAPI,status

app = FastAPI()

@app.get("/create-user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"user created"
        }

@app.get("/user")
def get_user():
    return{
        "status":"success",
        "message":"User fetched",
        "data":{
            "name":"harshit",
            "age":"20"
        }
        }