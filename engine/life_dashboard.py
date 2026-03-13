from engine.life_orchestrator import run_life_orchestrator


def generate_life_dashboard():

    data = run_life_orchestrator()

    life_score = data.get("life_score", 0)
    task_completion = data.get("task_completion", 0)
    habit_strength = data.get("habit_strength", 0)

    # Normalize to 0–100
    execution = min(task_completion, 100)
    habits = min(habit_strength, 100)
    momentum = min((habit_strength + task_completion) / 2, 100)
    focus = min(life_score, 100)

    return {
        "execution": execution,
        "habits": habits,
        "momentum": momentum,
        "focus": focus
    }