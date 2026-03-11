from ai.ai_engine import ai_chat


def generate_tasks(strategy_text):

    prompt = f"""
From the strategy below, extract the most important actionable tasks.

Rules:
- Max 8 tasks
- One task per line
- No numbering
- No explanations

Strategy:
{strategy_text}
"""

    result = ai_chat(
        prompt,
        "You are an expert productivity planner who extracts the most important tasks."
    )

    return result
