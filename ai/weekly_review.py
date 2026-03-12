from engine.life_engine import analyze_life_system


def generate_weekly_review():

    data = analyze_life_system()

    xp = data["xp"]
    momentum = data["momentum"]

    review = f"""
Weekly Performance Review

Current XP: {xp}
Momentum: {momentum}

Focus for next week:
- Maintain habit consistency
- Complete your highest value tasks
"""

    return review