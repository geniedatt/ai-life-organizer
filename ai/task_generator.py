from ai.ai_engine import ai_chat


def generate_tasks_from_strategy(strategy):

    prompt = f"""
From the life strategy below, extract actionable tasks the user should complete.

Return ONLY a list of short tasks.

Example format:

- Go for a 20 minute walk
- Brainstorm 5 business ideas
- Call mom
- Prepare a healthy lunch

Life Strategy:
{strategy}
"""

    tasks = ai_chat(prompt, "You extract practical tasks from plans.")

    if tasks:
        return tasks.split("\n")
    else:
        return []