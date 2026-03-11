from ai.ai_engine import ai_chat


def generate_daily_briefing(tasks, habits):

    task_list = "\n".join([t[1] for t in tasks])
    habit_list = "\n".join([h[1] for h in habits])

    prompt = f"""
Create a SHORT daily briefing for a productivity dashboard.

Rules:
- Maximum 5 sentences
- Keep it concise
- Avoid long motivational paragraphs
- Focus on today's priorities

Tasks:
{task_list}

Habits:
{habit_list}

Return format:

Good morning message.

Today's Focus:
• key focus
• key focus
• key focus

Short encouraging closing sentence.
"""

    result = ai_chat(prompt, "You are a concise productivity coach.")

    return result