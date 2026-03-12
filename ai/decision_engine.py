from database import get_tasks, get_habits
from services.xp_service import calculate_xp


def generate_daily_mission():

    tasks = get_tasks()
    habits = get_habits()

    xp, level = calculate_xp()

    mission = []

    if tasks:
        mission.append(f"Complete priority task: {tasks[0][1]}")

    if habits:
        mission.append("Maintain your habit streaks")

    mission.append("Focus 60 minutes on your most important goal")

    if xp < 200:
        mission.append("Build momentum with 3 small wins")

    if xp > 500:
        mission.append("Push a high-impact project")

    return mission