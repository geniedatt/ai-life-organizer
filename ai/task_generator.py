from ai.ai_engine import ai_chat


def generate_tasks(strategy_text):

    prompt = f"""
From the following life strategy, extract a clean list of actionable tasks.

Rules:
- Return ONLY tasks
- One task per line
- No explanations
- No numbering
- Keep tasks practical

Strategy:
{strategy_text}
"""

    result = ai_chat(
        prompt,
        "You are an expert productivity planner that converts strategies into concrete tasks."
    )

    return result
