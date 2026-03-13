from database import get_tasks, get_habits
from engine.life_engine import calculate_xp
from ai.daily_briefing import generate_daily_briefing

def generate_command_center():

    tasks = get_tasks()
    habits = get_habits()

    xp, level = calculate_xp()

    completed_tasks = sum(1 for t in tasks if t["completed"])
    total_tasks = len(tasks)

    completion_rate = 0
    if total_tasks > 0:
        completion_rate = completed_tasks / total_tasks

    habit_strength = len(habits)

    briefing = generate_daily_briefing(tasks, habits)

    focus = []

    if completion_rate < 0.4:
        focus.append("Reduce task overload")

    if habit_strength < 3:
        focus.append("Build foundational habits")

    if completion_rate > 0.7:
        focus.append("Increase goal difficulty")

    return {
        "xp": xp,
        "level": level,
        "completion_rate": completion_rate,
        "habit_strength": habit_strength,
        "focus": focus,
        "briefing": briefing
    }