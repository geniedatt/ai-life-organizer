from ai.ai_engine import ai_chat


def generate_life_strategy(goal):

    prompt = f"""
You are an elite life strategist.

Create a life strategy for this goal:

Goal: {goal}

Return:

Projects
Tasks
Habits
"""

    return ai_chat(prompt, "You are a strategic life planner.")