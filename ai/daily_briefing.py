from ai.ai_engine import ai_chat


def generate_daily_briefing(tasks, habits):

    task_list = "\n".join([t[1] for t in tasks])
    habit_list = "\n".join([h[1] for h in habits])

    prompt = f"""
You are a motivational productivity coach.

Create a short morning briefing for the user.

Tasks:
{task_list}

Habits:
{habit_list}

The briefing should include:

• encouragement
• today's focus
• recognition of their progress

Keep it concise and motivating.
"""

    result = ai_chat(prompt, "You are an encouraging productivity coach.")

    return result