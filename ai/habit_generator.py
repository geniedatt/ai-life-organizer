from ai.ai_engine import ai_chat


def generate_habits_from_strategy(strategy):

    prompt = f"""
From the life strategy below, extract daily habits the user should practice.

Return ONLY simple daily habits.

Example format:

- Drink a glass of water after waking up
- Exercise for 20 minutes
- Write down 3 business ideas
- Send a message to a family member

Life Strategy:
{strategy}
"""

    habits = ai_chat(prompt, "You extract positive daily habits.")

    if habits:
        return habits.split("\n")
    else:
        return []