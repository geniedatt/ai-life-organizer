from database import get_memory, save_memory
from ai.ai_engine import ai_chat


def generate_life_strategy(brain_dump):

    # -----------------------------
    # LOAD PAST MEMORIES
    # -----------------------------

    memories = get_memory()

    memory_context = "\n".join(memories)

    # -----------------------------
    # AI PROMPT
    # -----------------------------

    prompt = f"""
You are an elite life strategist and productivity architect.

User long-term context:
{memory_context}

Turn the user's thoughts into a practical 30-day life execution plan.

Your response must include:

### Top 3 Life Goals
Clear and specific goals.

### Weekly Focus Plan
Week 1–4 with concrete objectives.

### Daily Habits
Simple repeatable behaviors.

### Actionable Tasks
Specific things the user can actually do.

### First 3 Actions To Start Today
Immediate next steps.

User thoughts:
{brain_dump}

Make the plan practical, motivating, and clear.
Avoid generic advice.
"""

    # -----------------------------
    # AI GENERATION
    # -----------------------------

    result = ai_chat(
        prompt,
        "You are an elite life strategist and productivity architect."
    )

    # -----------------------------
    # SAVE NEW MEMORY
    # -----------------------------

    if result:
        save_memory(brain_dump)
        return result

    else:
        return "⚠️ AI could not generate a strategy. Please try again."