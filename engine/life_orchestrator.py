from database import get_tasks, get_habits
from engine.life_score import calculate_life_score


def orchestrate_life():

    tasks = get_tasks()
    habits = get_habits()

    life_score = calculate_life_score(tasks, habits)

    priorities = []

    if life_score < 40:

        priorities.append("Stabilize habits")
        priorities.append("Reduce task load")

    elif life_score < 70:

        priorities.append("Improve consistency")
        priorities.append("Focus on top goals")

    else:

        priorities.append("Scale ambition")
        priorities.append("Increase challenge")

    return {
        "life_score": life_score,
        "priorities": priorities
    }