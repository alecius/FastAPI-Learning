from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def user_name(name: str=None): #optional & default values by none or any name
    return {"name":name}


@app.get("/product")
def product_list(name: str = None, price:int=0): #multiply querys
    return {
        "name":name,
        "price":price
    }