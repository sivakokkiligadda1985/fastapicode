from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
#Adding a comment in sivadev1
#Adding a comment in sivadev1 only
#Adding changes from test1 only

#Test code only


app = FastAPI()

# Pydantic model for TODO
class Todo(BaseModel):
    name: str
    completed: bool
    #main branch chage in main.py
    #change from sivadev3
# In-memory database
todos: List[Todo] = []

# Create a new TODO
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo
#Adding a comment in sivadev1

# Read all TODOs
@app.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

# Read a single TODO by index
@app.get("/todos/{index}", response_model=Todo)
def get_todo(index: int):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[index]

# Update a TODO by index
@app.put("/todos/{index}", response_model=Todo)
def update_todo(index: int, todo: Todo):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[index] = todo
    return todo

# Delete a TODO by index
@app.delete("/todos/{index}", response_model=Todo)
def delete_todo(index: int):
    if index < 0 or index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    deleted_todo = todos.pop(index)
    return deleted_todo


#run command: uvicorn main:app --reloaduvicorn main:app --reload
