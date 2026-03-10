from ai.ai_engine import ai_chat

def weekly_plan(tasks):

    prompt = f"""
Choose the 3 most important tasks.

{tasks}
"""

    return ai_chat(prompt,"You are a productivity coach.")


def daily_schedule(tasks):

    prompt = f"""
Create a daily schedule between 8:00 and 20:00.

Tasks:
{tasks}
"""

    return ai_chat(prompt,"You create schedules.")
