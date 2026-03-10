from ai.ai_engine import ai_chat

def goal_breakdown(goals):

    prompt = f"""
Break these goals into action steps.

Goals:
{goals}

Return actions.
"""

    return ai_chat(prompt,"You are a life coach.")
