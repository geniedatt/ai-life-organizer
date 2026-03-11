import re


def extract_goals(strategy_text):

    if not strategy_text:
        return []

    # Find the Top 3 Life Goals section
    match = re.search(
        r"Top 3 Life Goals(.*?)(Weekly Focus Plan|Daily Habits|Actionable Tasks)",
        strategy_text,
        re.DOTALL | re.IGNORECASE
    )

    if not match:
        return []

    goals_block = match.group(1)

    # Extract numbered or bullet goals
    goals = re.findall(r"\d+\.\s*(.*)|-\s*(.*)", goals_block)

    cleaned = []

    for g in goals:
        goal = g[0] if g[0] else g[1]
        if goal.strip():
            cleaned.append(goal.strip())

    return cleaned