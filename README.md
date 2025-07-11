# FastAPI Crash Course: Todo App

This project is my hands-on crash course attempt at learning [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## What does this project do?

It's a simple Todo API that demonstrates the basics of FastAPI, including:

- **CRUD operations**: Create, Read, Update, and Delete todos
- **Pydantic models**: For data validation and serialization
- **Path and query parameters**: For flexible API endpoints
- **Error handling**: Using FastAPI's `HTTPException`

## Endpoints

- `GET /` — Welcome message
- `GET /todos` — List all todos (optionally limit with `first_n`)
- `GET /todos{todo_id}` — Get a specific todo by ID
- `POST /todos` — Create a new todo
- `PUT /todos/{todo_id}` — Update an existing todo
- `DELETE /todos/{todo_id}` — Delete a todo

## How to run

1. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the server:
   ```bash
   uvicorn main:api --reload
   ```
3. Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs (Swagger UI).

## Why this project?

I wanted to get a feel for FastAPI's syntax, features, and development flow by building something practical and minimal. This project is not production-ready, but a learning playground.

---

Feel free to use this as a reference for your own FastAPI learning journey!
