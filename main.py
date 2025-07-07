from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {
        "todo_id": 1,
        "todo_name": "Buy groceries",
        "todo_description": "Go to carrefour",
    },
    {
        "todo_id": 2,
        "todo_name": "Sports",
        "todo_description": "Go to the gym",
    },
    {
        "todo_id": 3,
        "todo_name": "Study",
        "todo_description": "Study for the exam",
    },
    {
        "todo_id": 4,
        "todo_name": "Read a book",
        "todo_description": "Read the Lord of the Rings",
    },
]


# GET, POST, PUT, DELETE
@api.get("/")
def index():
    return {"message": "Hello World"}


@api.get("/todos{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {"result": todo}
    return {"result": "Todo not found"}


@api.get("/todos")
def get_todos(first_n: int = 0):
    if first_n > 0:
        return {"result": all_todos[:first_n]}
    return {"result": all_todos}


@api.post("/todos")
def create_todo(todo: dict):
    new_todo_id = len(all_todos) + 1
    new_todo = {
        "todo_id": new_todo_id,
        "todo_name": todo["todo_name"],
        "todo_description": todo["todo_description"],
    }
    all_todos.append(new_todo)
    return {"added new todo": new_todo}


@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            todo["todo_name"] = updated_todo["todo_name"]
            todo["todo_description"] = updated_todo["todo_description"]
            return {"updated todo": todo}
    return {"result": "Todo not found"}


@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            all_todos.remove(todo)
            return {"result": "Todo deleted"}
    return {"result": "Todo not found"}
