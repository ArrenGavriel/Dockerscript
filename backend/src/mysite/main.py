from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # import cors middleware
from pydantic import BaseModel

app = FastAPI()

# cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TodoItem(BaseModel):
    id: int
    content: str

class TodoItemCreate(BaseModel):
    content: str

todos: list[TodoItem] = []
id_counter = 1

@app.post("/todos", response_model=TodoItem)
async def create_todo(item: TodoItemCreate):
    global id_counter
    new_todo = TodoItem(id=id_counter, content=item.content)
    todos.append(new_todo)
    id_counter += 1
    return new_todo

@app.get("/todos", response_model=list[TodoItem])
async def read_todos():
    return todos

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
        raise HTTPException(status_code=404, detail="Todo not found")