# ============================================================
# AI LIFE ORGANIZER
# ============================================================

"""
Deployment Flow

Your Computer
      ↓
GitHub (store the code)
      ↓
Streamlit Cloud (deploy website)
      ↓
Flutter mobile wrapper
      ↓
Google Play Store + Apple App Store

This project can evolve into:
• AI Life Planner
• Productivity AI Assistant
• Task-to-Action Generator
"""

# ============================================================
# IMPORTS
# ============================================================

import os
import re
import datetime
import streamlit as st
from openai import OpenAI

from database import (
    add_task,
    get_tasks,
    complete_task,
    delete_task,
    update_streak,
    get_streak,
    init_db
)

# ============================================================
# INITIALIZATION
# ============================================================

init_db()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def extract_time(task):
    t = task.lower()

    match = re.search(r"\b\d{1,2}(:\d{2})?\s?(am|pm)?\b", t)

    if match:
        return match.group()

    return None


def extract_sentences(text):

    sentences = re.split(r"[.\n]", text)

    results = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        sentence = re.sub(
            r"\b(tomorrow|today|tonight|later)\b",
            "",
            sentence,
            flags=re.IGNORECASE
        )

        sentence = re.sub(
            r"\b(i need to|need to|i want to|remember to|i should)\b",
            "",
            sentence,
            flags=re.IGNORECASE
        )

        parts = re.split(r",|\band\b", sentence, flags=re.IGNORECASE)

        for part in parts:
            part = part.strip()

            if part:
                results.append(part)

    return results


def detect_current_time_block():

    hour = datetime.datetime.now().hour

    if hour < 12:
        return "morning"

    elif hour < 17:
        return "afternoon"

    else:
        return "evening"


# ============================================================
# AI FUNCTIONS
# ============================================================

def ai_organize_text(text):

    prompt = f"""
You organize messy thoughts.

Convert the text into:

Goals
Tasks
Habits

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You organize thoughts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def ai_schedule_tasks(task_list):

    prompt = f"""
Create a daily schedule between 8:00 and 20:00.

Tasks:
{task_list}

Return format:

09:00 Task
10:00 Task
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You create schedules."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception:
        return None


def generate_ai_reminders(tasks):

    incomplete = [task for _, task, completed in tasks if not completed]

    if not incomplete:
        return None

    prompt = f"""
Send friendly reminders for these tasks:

{incomplete}

Return 1-2 short reminders.
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You send reminders."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception:
        return None


# ============================================================
# ORGANIZATION LOGIC
# ============================================================

def organize_text(text):

    goals = []
    tasks = []
    habits = []

    goal_words = [
        "learn","start","build","launch","create",
        "develop","study","improve"
    ]

    habit_words = [
        "daily","every","routine","habit",
        "gym","exercise","meditate","read","workout"
    ]

    task_verbs = [
        "call","buy","clean","finish","send","email",
        "schedule","pay","write","review","fix",
        "prepare","submit","update","plan",
        "organize","meet"
    ]

    lines = extract_sentences(text)

    for line in lines:

        l = line.lower()

        if any(word in l for word in goal_words):
            goals.append(line)

        elif any(word in l for word in habit_words):
            habits.append(line)

        elif any(verb in l for verb in task_verbs):
            tasks.append(line)

        else:
            tasks.append(line)

    return goals, tasks, habits


# ============================================================
# DAILY PLANNING
# ============================================================

def detect_time(task):

    t = task.lower()

    if "morning" in t:
        return "morning"

    if "afternoon" in t:
        return "afternoon"

    if "evening" in t or "tonight" in t:
        return "evening"

    if "tomorrow" in t:
        return "tomorrow"

    if "daily" in t:
        return "daily"

    specific = extract_time(task)

    if specific:
        return f"time: {specific}"

    return "unscheduled"


def generate_daily_plan(tasks):

    morning = []
    afternoon = []
    evening = []
    tomorrow = []
    daily = []
    unscheduled = []
    scheduled = []

    for _, task, _ in tasks:

        slot = detect_time(task)

        if slot == "morning":
            morning.append(task)

        elif slot == "afternoon":
            afternoon.append(task)

        elif slot == "evening":
            evening.append(task)

        elif slot == "tomorrow":
            tomorrow.append(task)

        elif slot == "daily":
            daily.append(task)

        elif slot.startswith("time:"):

            time_value = slot.replace("time: ", "")

            clean = re.sub(
                r"\bat\s*\b\d{1,2}(:\d{2})?\s?(am|pm)?\b",
                "",
                task
            ).strip()

            scheduled.append((time_value, clean))

        else:
            unscheduled.append(task)

    return morning, afternoon, evening, tomorrow, daily, unscheduled, scheduled


# ============================================================
# ANALYTICS
# ============================================================

def prioritize_tasks(tasks):

    urgent = []
    important = []
    later = []

    for _, task, _ in tasks:

        t = task.lower()

        if "today" in t or "asap" in t:
            urgent.append(task)

        elif "tomorrow" in t:
            important.append(task)

        else:
            later.append(task)

    return urgent, important, later


def calculate_stats(tasks):

    total = len(tasks)

    completed = sum(1 for _, _, done in tasks if done)

    rate = 0 if total == 0 else round((completed / total) * 100)

    return total, completed, rate


# ============================================================
# STREAMLIT UI
# ============================================================

st.title("🧠 AI Life Organizer")
st.caption("Turn your thoughts into organized goals, tasks, and habits.")
st.divider()

# ------------------------------------------------------------

saved_tasks = get_tasks()

reminders = generate_ai_reminders(saved_tasks)

if reminders:
    st.subheader("🔔 AI Reminder")
    st.info(reminders)

# ------------------------------------------------------------

brain_dump = st.text_area(
    "🧠 Brain Dump",
    height=200,
    placeholder="Write everything on your mind..."
)

# ------------------------------------------------------------

if st.button("✨ Organize My Life", use_container_width=True):

    if brain_dump.strip():

        try:
            ai_result = ai_organize_text(brain_dump)
            st.markdown(ai_result)

        except Exception:
            st.warning("AI temporarily unavailable. Using local organizer.")

        goals, tasks, habits = organize_text(brain_dump)

        for t in tasks:
            add_task(t)

    else:
        st.warning("Please enter something.")

# ------------------------------------------------------------
# TASK LIST
# ------------------------------------------------------------

st.subheader("📋 Saved Tasks")

tasks = get_tasks()

for task_id, task, completed in tasks:

    col1, col2 = st.columns([4,1])

    with col1:

        if st.checkbox(task, value=completed, key=f"task_{task_id}"):

            if not completed:

                complete_task(task_id)

                time_block = detect_current_time_block()

                update_streak(task_id, time_block)

                st.rerun()

    with col2:

        if st.button("❌", key=f"delete_{task_id}"):

            delete_task(task_id)

            st.rerun()

# ------------------------------------------------------------
# DAILY PLAN
# ------------------------------------------------------------

st.subheader("🗓 Daily Plan")

saved_tasks = get_tasks()

task_text = [task for _, task, _ in saved_tasks]

ai_schedule = ai_schedule_tasks(task_text)

if ai_schedule:

    st.subheader("🤖 AI Daily Schedule")

    for line in ai_schedule.split("\n"):

        if line.strip():
            st.write("•", line)

# ------------------------------------------------------------
# PRODUCTIVITY DASHBOARD
# ------------------------------------------------------------

st.subheader("📊 Productivity Dashboard")

total, completed, rate = calculate_stats(saved_tasks)

col1, col2, col3 = st.columns(3)

col1.metric("📋 Total Tasks", total)
col2.metric("✅ Completed", completed)
col3.metric("🎯 Completion Rate", f"{rate}%")

# ------------------------------------------------------------
# HABIT STREAKS
# ------------------------------------------------------------

st.subheader("🔥 Habit Streaks")

for task_id, task, completed in saved_tasks:

    if "daily" in task.lower() or "every" in task.lower():

        streak = get_streak(task_id)

        st.write(f"{task} 🔥 {streak} days")

        