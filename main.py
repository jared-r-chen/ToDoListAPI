from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from services.DBService import *

class Task(BaseModel):
    name: str
    status: int

# Load .env file into environment variables
load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from EC2!"}

@app.post("/task/{userId}")
async def say_hello(userId: int, body: Task):
    print(body)
    insertNewTask(userId, body.name, body.status)
    return {"message": f"Task Saved: {body.name}, {body.status}"}

@app.get("/task/{userId}")
async def get_tasks(userId: int):
    tasks = getAllTasks(userId)
    for task in tasks:
        print(task)
    return {"message": f"Tasks for user {userId}", "tasks": tasks}

@app.put("/task/{taskId}")
async def update_task(taskId: int, body: Task):
    print(body)
    updateTask(taskId, body.name, body.status)
    return {"message": f"Task Updated: {body.name}, {body.status}"}

@app.delete("/task/{taskId}")
async def delete_task(taskId: int):
    deleteTask(taskId)
    return {"message": f"Task Deleted: {taskId}"}