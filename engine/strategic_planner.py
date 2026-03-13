from database import get_tasks
from engine.life_orchestrator import run_life_orchestrator
from engine.task_scoring import rank_tasks


def generate_daily_strategy():

    tasks = get_tasks()

    if tasks is None:
        tasks = []

    # Get system state
    data = run_life_orchestrator()
    life_score = data.get("life_score", 0)

    # -------------------------
    # Filter incomplete tasks
    # -------------------------

    open_tasks = []

    for task in tasks:
        try:
            if not task.get("completed"):
                open_tasks.append(task)
        except:
            pass

    # -------------------------
    # AI Task Ranking
    # -------------------------

    ranked_tasks = rank_tasks(open_tasks)

    # -------------------------
    # Strategic boost if life score low
    # -------------------------

    if life_score < 40:
        ranked_tasks = sorted(
            ranked_tasks,
            key=lambda x: x["score"] + 5,
            reverse=True
        )

    # -------------------------
    # Select top 3
    # -------------------------

    top_tasks = []

    for item in ranked_tasks[:3]:

        task = item["task"]

        try:
            top_tasks.append(task["title"])
        except:
            pass

    return top_tasks