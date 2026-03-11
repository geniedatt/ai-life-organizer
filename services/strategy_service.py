from ai.life_strategy import generate_life_strategy
from ai.task_generator import generate_tasks
from ai.habit_generator import generate_habits

from database import add_task, add_habit


def build_full_strategy(brain_dump):

    strategy = generate_life_strategy(brain_dump)

    if not strategy:
        return None

    # -----------------------------
    # EXTRACT TASKS
    # -----------------------------

    tasks = generate_tasks(strategy)

    if tasks:
        lines = tasks.split("\n")

        for line in lines:

            clean = line.strip()

            if not clean:
                continue

            clean = clean.replace("•", "").replace("-", "").strip()

            if len(clean) > 3:
                add_task(clean)

    # -----------------------------
    # EXTRACT HABITS
    # -----------------------------

    habits = generate_habits(strategy)

    if habits:
        lines = habits.split("\n")

        for line in lines:

            clean = line.strip()

            if not clean:
                continue

            clean = clean.replace("•", "").replace("-", "").strip()

            if len(clean) > 3:
                add_habit(clean)

    return strategy
