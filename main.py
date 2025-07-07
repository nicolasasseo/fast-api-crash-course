from fastapi import FastAPI
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    todo_name: str = Field(
        ..., min_length=3, max_length=512, description="The name of the todo"
    )
    todo_description: str = Field(..., description="The description of the todo")
    priority: Priority = Field(
        default=Priority.LOW, description="The priority of the todo"
    )


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(
        None, min_length=3, max_length=512, description="The name of the todo"
    )
    todo_description: Optional[str] = Field(
        None, description="The description of the todo"
    )
    priority: Optional[Priority] = Field(None, description="The priority of the todo")


class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier of the todo")


api = FastAPI()

all_todos = [
    Todo(
        todo_id=1,
        todo_name="Buy groceries",
        todo_description="Go to carrefour",
        priority=Priority.LOW,
    ),
    Todo(
        todo_id=2,
        todo_name="Sports",
        todo_description="Go to the gym",
        priority=Priority.MEDIUM,
    ),
    Todo(
        todo_id=3,
        todo_name="Study",
        todo_description="Study for the exam",
        priority=Priority.HIGH,
    ),
    Todo(
        todo_id=4,
        todo_name="Read a book",
        todo_description="Read the Lord of the Rings",
        priority=Priority.LOW,
    ),
]


# GET, POST, PUT, DELETE
@api.get("/")
def index():
    return {"message": "Hello World"}


@api.get("/todos{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    return {"result": "Todo not found"}


@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = 0):
    if first_n > 0:
        return {"result": all_todos[:first_n]}
    return {"result": all_todos}


@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = len(all_todos) + 1
    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority,
    )
    all_todos.append(new_todo)
    return {"added new todo": new_todo}


@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return {"updated todo": todo}
    return {"result": "Todo not found"}


@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            all_todos.remove(todo)
            return {"deleted todo": todo}
    return {"result": "Todo not found"}
