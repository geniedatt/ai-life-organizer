from ai.ai_engine import ai_chat


def generate_habits(strategy_text):

    prompt = f"""
From the following life strategy, extract daily habits.

Rules:
- Return ONLY habits
- One habit per line
- No numbering
- No explanations
- Keep habits short and repeatable

Strategy:
{strategy_text}
"""

    result = ai_chat(
        prompt,
        "You are an expert habit designer that extracts daily habits from strategies."
    )

    return result
