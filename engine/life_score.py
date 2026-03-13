def calculate_life_score(tasks, habits):

    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)

    task_score = 0
    if total > 0:
        task_score = (completed / total) * 50

    habit_score = min(len(habits) * 10, 50)

    return round(task_score + habit_score)