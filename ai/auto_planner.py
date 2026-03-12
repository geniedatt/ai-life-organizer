from database import get_tasks, get_habits
from engine.life_engine import analyze_life_system


def generate_daily_plan():

    data = analyze_life_system()

    tasks = data["tasks"]
    habits = data["habits"]

    plan = {
        "morning": [],
        "afternoon": [],
        "evening": []
    }

    for habit in habits[:2]:
        plan["morning"].append(habit[1])

    for task in tasks[:3]:
        plan["afternoon"].append(task[1])

    if tasks:
        plan["evening"].append("Review completed tasks")

    return plan