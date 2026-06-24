from fastapi import FastAPI,Depends

app = FastAPI()

def owner():
    return {
        "name":"harshit"
    }

@app.get("/user")
def user(data = Depends(owner)):
    return data

@app.get("/daddy")
def daddy(data = Depends(owner)):
    return data
    
