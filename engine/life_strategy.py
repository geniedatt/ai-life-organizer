from engine.life_orchestrator import run_life_orchestrator


def generate_life_strategy():

    data = run_life_orchestrator()

    life_score = data.get("life_score", 0)
    completion = data.get("task_completion", 0)
    habit_strength = data.get("habit_strength", 0)

    focus = []
    opportunities = []
    risks = []
    moves = []

    # -------------------------
    # Focus Areas
    # -------------------------

    if life_score < 40:

        focus.append("Stabilize your daily habits")
        focus.append("Reduce task overload")

        moves.append("Focus on completing a few critical tasks daily")

    elif life_score < 70:

        focus.append("Improve execution consistency")
        focus.append("Strengthen habit routines")

        moves.append("Maintain steady progress on strategic tasks")

    else:

        focus.append("Scale your ambitions")
        focus.append("Pursue high-impact projects")

        moves.append("Push major strategic initiatives")

    # -------------------------
    # Opportunities
    # -------------------------

    if habit_strength > 50:
        opportunities.append("Your habit system is strengthening")

    if completion > 60:
        opportunities.append("Task execution momentum is strong")

    # -------------------------
    # Risks
    # -------------------------

    if completion < 40:
        risks.append("Too many unfinished tasks")

    if habit_strength < 20:
        risks.append("Habit momentum is very low")

    if life_score < 30:
        risks.append("Overall system stability is weak")

    return {
        "focus": focus,
        "opportunities": opportunities,
        "risks": risks,
        "moves": moves
    }