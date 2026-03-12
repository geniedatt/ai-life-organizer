from database import get_habits, get_tasks
from services.xp_service import calculate_xp


def generate_daily_briefing(tasks, habits):

    habits = get_habits()
    tasks = get_tasks()

    xp, level = calculate_xp()

    habit_count = len(habits)
    task_count = len(tasks)

    momentum = "Low"

    if xp > 500:
        momentum = "High"
    elif xp > 200:
        momentum = "Medium"

    priorities = []

    if task_count > 0:
        priorities.append("Complete your most important task")

    if habit_count > 0:
        priorities.append("Maintain your habit streaks")

    priorities.append("Schedule a deep work block")

    advice = "Stay consistent today."

    if momentum == "Low":
        advice = "Focus on small wins to rebuild momentum."

    if momentum == "High":
        advice = "You have strong momentum. Push your biggest goal today."

    return {
        "momentum": momentum,
        "priorities": priorities,
        "advice": advice,
        "xp": xp,
        "level": level
    }