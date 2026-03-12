from engine.life_engine import analyze_life_system


def get_command_center():

    data = analyze_life_system()

    tasks = data["tasks"]
    habits = data["habits"]
    xp = data["xp"]
    level = data["level"]

    task_pressure = "Low"

    if len(tasks) > 10:
        task_pressure = "High"
    elif len(tasks) > 5:
        task_pressure = "Medium"

    habit_stability = "Weak"

    if len(habits) >= 5:
        habit_stability = "Strong"
    elif len(habits) >= 3:
        habit_stability = "Moderate"

    strategic_focus = "Build consistency"

    if data["momentum"] == "High":
        strategic_focus = "Push high-impact goals"

    return {
        "xp": xp,
        "level": level,
        "momentum": data["momentum"],
        "task_pressure": task_pressure,
        "habit_stability": habit_stability,
        "strategic_focus": strategic_focus,
        "priorities": data["priorities"],
        "advice": data["advice"]
    }