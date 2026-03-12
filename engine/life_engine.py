from database import get_tasks, get_habits
from services.xp_service import calculate_xp
from ai.daily_briefing import generate_daily_briefing


def analyze_life_system():

    tasks = get_tasks()
    habits = get_habits()

    xp, level = calculate_xp()

    briefing = generate_daily_briefing(tasks, habits)

    return {
        "tasks": tasks,
        "habits": habits,
        "xp": xp,
        "level": level,
        "momentum": briefing["momentum"],
        "priorities": briefing["priorities"],
        "advice": briefing["advice"]
    }