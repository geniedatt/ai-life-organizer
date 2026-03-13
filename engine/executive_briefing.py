from engine.life_orchestrator import run_life_orchestrator


def generate_executive_briefing():

    data = run_life_orchestrator()

    life_score = data.get("life_score", 0)
    task_completion = data.get("task_completion", 0)
    habit_strength = data.get("habit_strength", 0)

    chief = data.get("chief_of_staff", {})
    trajectory = data.get("trajectory", {})

    focus = chief.get("focus", [])
    risks = chief.get("risks", [])
    advice = chief.get("advice", [])

    trajectory_status = trajectory.get("trajectory", "")

    # -------------------------
    # Greeting
    # -------------------------

    greeting = "Good day."

    if life_score >= 70:
        greeting = "You're performing well."

    elif life_score < 40:
        greeting = "Your system needs stabilization."

    # -------------------------
    # Briefing text
    # -------------------------

    summary = f"""
{greeting}

Your current **Life Score** is {life_score}.

System Metrics:
• Task Completion: {task_completion}%
• Habit Strength: {habit_strength}

Trajectory Status: **{trajectory_status}**
"""

    return {
        "summary": summary,
        "focus": focus,
        "risks": risks,
        "advice": advice
    }