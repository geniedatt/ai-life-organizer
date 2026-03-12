from ai.ai_engine import ai_chat


def goal_breakdown(goals):

    prompt = f"""
You are a strategic life coach.

Break the following goals into clear actionable steps.

Goals:
{goals}

Return:
Goal
- Step 1
- Step 2
- Step 3
"""

    return ai_chat(prompt, "You are a world class life strategist.")