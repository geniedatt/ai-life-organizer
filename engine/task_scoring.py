from datetime import datetime


def score_task(task):

    score = 0

    # -------------------------
    # Priority Weight
    # -------------------------

    priority = task.get("priority", "medium")

    if priority == "high":
        score += 40
    elif priority == "medium":
        score += 20
    else:
        score += 10

    # -------------------------
    # Due Date Urgency
    # -------------------------

    due_date = task.get("due_date")

    if due_date:

        try:
            due = datetime.strptime(due_date, "%Y-%m-%d")
            today = datetime.today()

            days_left = (due - today).days

            if days_left <= 0:
                score += 40
            elif days_left <= 2:
                score += 30
            elif days_left <= 7:
                score += 20
            else:
                score += 10

        except:
            pass

    # -------------------------
    # Strategic Keywords
    # -------------------------

    title = task.get("title", "").lower()

    strategic_words = [
        "build",
        "create",
        "launch",
        "strategy",
        "plan",
        "design",
        "develop",
    ]

    for word in strategic_words:
        if word in title:
            score += 10
            break

    return score


def rank_tasks(tasks):

    scored_tasks = []

    for task in tasks:

        if not task.get("completed"):
            task_score = score_task(task)

            scored_tasks.append(
                {
                    "task": task,
                    "score": task_score
                }
            )

    # Sort by score
    scored_tasks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_tasks