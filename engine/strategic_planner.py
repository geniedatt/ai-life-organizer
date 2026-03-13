from database import get_tasks
from engine.life_orchestrator import run_life_orchestrator


def generate_daily_strategy():

    tasks = get_tasks()

    if tasks is None:
        tasks = []

    data = run_life_orchestrator()

    life_score = data.get("life_score", 0)

    # -------------------------
    # Filter incomplete tasks
    # -------------------------

    open_tasks = []

    for task in tasks:
        try:
            if not task["completed"]:
                open_tasks.append(task)
        except:
            pass

    # -------------------------
    # Prioritize tasks
    # -------------------------

    prioritized = []

    for task in open_tasks:

        score = 0

        # base priority
        score += 10

        try:
            if task.get("priority") == "high":
                score += 20

            if task.get("priority") == "medium":
                score += 10
        except:
            pass

        # strategic boost if life score low
        if life_score < 40:
            score += 5

        prioritized.append((score, task))

    prioritized.sort(reverse=True, key=lambda x: x[0])

    # -------------------------
    # Select top 3
    # -------------------------

    top_tasks = []

    for item in prioritized[:3]:
        task = item[1]

        try:
            top_tasks.append(task["title"])
        except:
            pass

    return top_tasks