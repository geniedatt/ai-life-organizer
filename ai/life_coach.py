from engine.life_engine import analyze_life_system


def generate_coaching_response(user_message):

    data = analyze_life_system()

    xp = data["xp"]
    level = data["level"]
    momentum = data["momentum"]
    tasks = len(data["tasks"])
    habits = len(data["habits"])

    context = f"""
User Stats:
XP: {xp}
Level: {level}
Momentum: {momentum}
Active Tasks: {tasks}
Active Habits: {habits}
"""

    response = f"""
Life Coach Analysis

{context}

Your question: {user_message}

Strategic Advice:
Focus on consistency. Completing tasks and maintaining habits will increase your momentum and level up your life system.
"""

    return response