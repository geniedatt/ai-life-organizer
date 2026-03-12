from fastapi import FastAPI

from services.xp_service import calculate_xp
from database import get_habits, get_tasks

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Life Organizer API running"}


@app.get("/xp")
def xp():
    xp, level = calculate_xp()
    return {"xp": xp, "level": level}


@app.get("/habits")
def habits():
    habits = get_habits()
    return {"habits": habits}


@app.get("/tasks")
def tasks():
    tasks = get_tasks()
    return {"tasks": tasks}