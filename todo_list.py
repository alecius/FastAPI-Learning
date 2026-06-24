from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def add_todos(list:Todo):
    todos.append(list)
    return {"message":"List Added","data":list}


@app.get("/todos")
def get_todo():
    return todos

@app.get("/todos/{todos_id}")
def get_todo(todos_id:int):
    for todo in todos:
        if todo.id == todos_id:
            return todo
        
    return {"error not found":todos_id}


@app.put("/todos/{todos_id}")
def update_todo(todos_id:int,update_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todos_id :
            todos[index] = update_todo
            return{
                "Succefully Updated":
                update_todo
            }  
        return{"CANNOT UPDATE"}

@app.delete("/todos/{todos_id}")
def delete_todo(todos_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todos_id:
            todos.pop(index)
            return{"Successfully Deleted"}
        
        return{"Cannnot Deleted"}