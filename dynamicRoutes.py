from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}") #fetching dynamic
def get_users(user_id:int): #datatype define in route
    return {"user_id": user_id}