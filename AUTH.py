from fastapi import FastAPI,Depends,Header,HTTPException

app=FastAPI()

def authetication(token:str = Header(None)):
    if token!="harshit000":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return{
        "User":"Authorized User"
    }

@app.get("/auth-user")
def data(user=Depends(authetication)):
    return{
        "message":"Secure data accessed",
        "user":user
    }