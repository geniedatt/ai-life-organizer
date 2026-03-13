from database import get_tasks, get_habits, get_all_habit_activity
from engine.life_score import calculate_life_score
from engine.momentum import calculate_momentum


def analyze_life_state():

    tasks = get_tasks()
    habits = get_habits()
    habit_logs = get_all_habit_activity()

    life_score = calculate_life_score(tasks, habits)
    momentum = calculate_momentum(habit_logs)

    completed_tasks = sum(1 for t in tasks if t["completed"])
    total_tasks = len(tasks)

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = completed_tasks / total_tasks

    return {
        "life_score": life_score,
        "momentum": momentum,
        "completion_rate": completion_rate,
        "tasks": tasks,
        "habits": habits
    }


def chief_of_staff_advice():

    state = analyze_life_state()

    score = state["life_score"]
    momentum = state["momentum"]
    completion = state["completion_rate"]

    advice = []
    focus = []
    risks = []

    # -------------------------
    # Strategic Analysis
    # -------------------------

    if score < 40:

        focus.append("Stabilize your daily habits")
        focus.append("Reduce task overload")

        advice.append(
            "Your system is unstable. Focus on building consistency before increasing ambition."
        )

    elif score < 70:

        focus.append("Improve execution consistency")

        advice.append(
            "You are making progress but your execution system can still be improved."
        )

    else:

        focus.append("Scale your goals")

        advice.append(
            "Your system is strong. Increase challenge and pursue higher goals."
        )

    # -------------------------
    # Momentum Analysis
    # -------------------------

    if momentum < 40:

        risks.append("Momentum is very low")

        advice.append(
            "You are losing momentum. Reduce complexity and focus on a few critical actions."
        )

    elif momentum > 80:

        advice.append(
            "Momentum is high. This is the best time to push major progress."
        )

    # -------------------------
    # Task Load Analysis
    # -------------------------

    if completion < 0.4:

        risks.append("Too many unfinished tasks")

        advice.append(
            "Your task list may be too large. Remove or postpone low-value tasks."
        )

    return {
        "focus": focus,
        "risks": risks,
        "advice": advice,
        "state": state
    }


# -------------------------------------------------
# ORCHESTRATOR COMPATIBILITY FUNCTION
# -------------------------------------------------

def chief_of_staff_analysis(tasks=None, habits=None):

    report = chief_of_staff_advice()

    advice = report["advice"]
    focus = report["focus"]
    risks = report["risks"]

    output = []

    if focus:
        output.append("Focus: " + ", ".join(focus))

    if risks:
        output.append("Risks: " + ", ".join(risks))

    if advice:
        output.append("Advice: " + " ".join(advice))

    return "\n\n".join(output)