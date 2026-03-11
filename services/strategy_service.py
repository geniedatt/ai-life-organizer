from ai.life_strategy import generate_life_strategy
from ai.task_generator import generate_tasks
from ai.habit_generator import generate_habits

from database import add_task, add_habit


def build_full_strategy(brain_dump):

    # Generate full AI strategy
    strategy = generate_life_strategy(brain_dump)

    if not strategy:
        return None

    # Generate tasks
    tasks = generate_tasks(strategy)

    if tasks:
        for t in tasks.split("\n"):
            clean = t.strip("-• ").strip()
            if clean:
                add_task(clean)

    # Generate habits
    habits = generate_habits(strategy)

    if habits:
        for h in habits.split("\n"):
            clean = h.strip("-• ").strip()
            if clean:
                add_habit(clean)

    return strategy
