from database import get_tasks, get_habits, get_all_habit_activity
from engine.life_score import calculate_life_score
from engine.momentum import calculate_momentum


def simulate_life_trajectory(tasks=None, habits=None):

    # Allow orchestrator to pass data or fetch it internally
    if tasks is None:
        tasks = get_tasks()

    if habits is None:
        habits = get_habits()

    habit_logs = get_all_habit_activity()

    life_score = calculate_life_score(tasks, habits)
    momentum = calculate_momentum(habit_logs)

    completed_tasks = sum(1 for t in tasks if t["completed"])
    total_tasks = len(tasks)

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = completed_tasks / total_tasks

    # ------------------------
    # Project future state
    # ------------------------

    progress_factor = (
        (life_score * 0.4) +
        (momentum * 0.4) +
        (completion_rate * 100 * 0.2)
    )

    if progress_factor < 40:

        trajectory = "stagnation"

        prediction = (
            "If your current behavior continues, progress will likely stall. "
            "You may struggle to maintain consistency and motivation."
        )

    elif progress_factor < 70:

        trajectory = "steady_progress"

        prediction = (
            "You are on a stable path. Consistent execution will slowly improve your results."
        )

    else:

        trajectory = "high_growth"

        prediction = (
            "You are on a strong trajectory. If momentum continues, you can achieve major progress in the next 90 days."
        )

    return {
        "life_score": life_score,
        "momentum": momentum,
        "completion_rate": completion_rate,
        "trajectory": trajectory,
        "prediction": prediction
    }