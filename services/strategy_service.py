from ai.life_strategy import generate_life_strategy
from ai.task_generator import generate_tasks_from_strategy
from ai.habit_generator import generate_habits_from_strategy
from database import add_task, add_habit


def build_full_strategy(brain_dump):

    strategy = generate_life_strategy(brain_dump)

    if not strategy:
        return None

    tasks = generate_tasks_from_strategy(strategy)
    habits = generate_habits_from_strategy(strategy)

    for task in tasks:
        clean = task.replace("-", "").strip()
        if clean:
            add_task(clean)

    for habit in habits:
        clean = habit.replace("-", "").strip()
        if clean:
            add_habit(clean)

    return strategy