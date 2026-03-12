from database import get_tasks, get_habits


def generate_daily_mission():

    tasks = get_tasks()
    habits = get_habits()

    mission = []

    # Top 2 tasks
    if tasks:
        for task in tasks[:2]:
            mission.append(f"Complete task: {task[1]}")

    # Top habit
    if habits:
        habit = habits[0]
        mission.append(f"Maintain habit streak: {habit[1]}")

    # Default fallback
    if not mission:
        mission.append("Plan your day and define your top priority.")

    return mission