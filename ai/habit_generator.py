from ai.ai_engine import ai_chat


def generate_habits(strategy_text):

    prompt = f"""
From the strategy below, extract ONLY true DAILY HABITS.

Rules:
- Habits must be repeatable daily behaviors
- Max 6 habits
- One habit per line
- No numbering
- No explanations
- Do NOT include one-time tasks or projects

Good examples:
exercise 30 minutes
drink 2 liters of water
study AI for 1 hour
practice mindfulness

Strategy:
{strategy_text}
"""

    result = ai_chat(
        prompt,
        "You are an expert habit designer who extracts only essential daily habits."
    )

    return result
