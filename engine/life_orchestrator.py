from database import get_tasks, get_habits

from ai.chief_of_staff import chief_of_staff_analysis
from ai.trajectory_simulator import simulate_life_trajectory
from engine.adaptive_strategy import generate_adaptive_strategy


def run_life_orchestrator():

    tasks = get_tasks()
    habits = get_habits()

    if tasks is None:
        tasks = []

    if habits is None:
        habits = []

    # -------------------------
    # TASK METRICS
    # -------------------------

    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:
        try:
            if task[3] == 1:
                completed_tasks += 1
        except:
            pass

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round((completed_tasks / total_tasks) * 100)

    # -------------------------
    # HABIT MOMENTUM
    # -------------------------

    habit_score = 0

    for habit in habits:
        try:
            streak = habit[2]
            habit_score += streak
        except:
            pass

    # -------------------------
    # AI SYSTEMS
    # -------------------------

    chief = chief_of_staff_analysis(tasks, habits)

    trajectory = simulate_life_trajectory(tasks, habits)

    adaptive = generate_adaptive_strategy(tasks, habits)

    # -------------------------
    # LIFE SCORE
    # -------------------------

    life_score = completion_rate + habit_score

    # -------------------------
    # ORCHESTRATOR OUTPUT
    # -------------------------

    return {
        "life_score": life_score,
        "task_completion": completion_rate,
        "habit_strength": habit_score,
        "chief_of_staff": chief,
        "trajectory": trajectory,
        "adaptive_strategy": adaptive
    }