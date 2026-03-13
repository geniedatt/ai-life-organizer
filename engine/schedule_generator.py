from datetime import datetime, timedelta
from database import get_tasks
from engine.task_scoring import rank_tasks


def generate_daily_schedule():

    tasks = get_tasks()

    if tasks is None:
        tasks = []

    ranked = rank_tasks(tasks)

    # -------------------------
    # Workday start
    # -------------------------

    start_time = datetime.now().replace(
        hour=9,
        minute=0,
        second=0,
        microsecond=0
    )

    schedule = []

    current_time = start_time

    # -------------------------
    # Schedule top tasks
    # -------------------------

    for item in ranked[:5]:

        task = item["task"]

        block_start = current_time
        block_end = current_time + timedelta(minutes=60)

        schedule.append({
            "time": f"{block_start.strftime('%H:%M')} - {block_end.strftime('%H:%M')}",
            "task": task.get("title", "Task")
        })

        current_time = block_end

    # -------------------------
    # Add review block
    # -------------------------

    review_start = current_time
    review_end = current_time + timedelta(minutes=30)

    schedule.append({
        "time": f"{review_start.strftime('%H:%M')} - {review_end.strftime('%H:%M')}",
        "task": "Daily Review & Planning"
    })

    return schedule