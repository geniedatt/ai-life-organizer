from ai.ai_engine import ai_chat


def generate_life_strategy(brain_dump):

    prompt = f"""
You are an AI life strategist.

From the user's thoughts below, create a 30-day life improvement plan.

Include:

1. Top 3 Life Goals
2. Weekly Focus Plan
3. Daily Habits
4. First Actions To Start Today

User thoughts:
{brain_dump}

Return a clear structured plan.
"""

    return ai_chat(prompt, "You are an expert life coach and strategist.")