'''
Your Computer
      ↓
GitHub (store the code)
      ↓
Streamlit Cloud (deploy website)
      ↓
Flutter mobile wrapper
      ↓
Google Play Store + Apple App Store



What has been built could evolve into something like:

AI life planner

productivity AI assistant

task-to-action generator

'''


from database import add_task, get_tasks, complete_task, delete_task, update_streak, get_streak, init_db
import os
import re
from openai import OpenAI
import streamlit as st

init_db()

def extract_time(task):

    t = task.lower()

    # detect specific clock times
    time_match = re.search(r"\b\d{1,2}(:\d{2})?\s?(am|pm)?\b", t)

    if time_match:
        return time_match.group()

    return None

if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("OpenAI API key not found in Streamlit secrets.")
    st.stop()

st.title("🧠 AI Life Organizer")
st.caption("Turn your thoughts into organized goals, tasks, and habits.")
st.divider()

brain_dump = st.text_area(
    "🧠 Brain Dump",
    placeholder="Write everything on your mind...\n\nExample:\nCall mom\nBuy groceries\nStart learning Python\nGo to the gym daily",
    height=200
)

def extract_sentences(text):

    sentences = re.split(r"[.\n]", text)

    results = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        # remove filler phrases
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


def ai_organize_text(text):

    prompt = f"""
You are an assistant that organizes messy thoughts.

Convert the text into three sections:

Goals
Tasks
Habits

Return the result in this format:

Goals:
- item

Tasks:
- item

Habits:
- item

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You organize messy thoughts into goals, tasks and habits."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def organize_text(text):
    goals = []
    tasks = []
    habits = []

    goal_words = [
    "learn","start","build","launch","create","develop","study","improve"
]

    habit_words = [
        "daily","every","routine","habit","gym","exercise","meditate","read"
    ]

    task_verbs = [
        "call","buy","clean","finish","send","email","schedule","pay","write",
        "review","fix","prepare","submit","update","plan","organize","meet"
]

    lines = extract_sentences(text)

    for line in lines:
        line = line.strip()
        if not line:
            continue
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

    if "daily" in t or "every day" in t:
        return "daily"

    # detect explicit clock time
    specific_time = extract_time(task)

    if specific_time:
        return f"time: {specific_time}"

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

        time_slot = detect_time(task)

        if time_slot == "morning":
            morning.append(task)

        elif time_slot == "afternoon":
            afternoon.append(task)

        elif time_slot == "evening":
            evening.append(task)

        elif time_slot == "tomorrow":
            tomorrow.append(task)

        elif time_slot == "daily":
            daily.append(task)

        elif time_slot.startswith("time:"):
            time_value = time_slot.replace("time: ", "")
            clean_task = re.sub(r"\b\d{1,2}(:\d{2})?\s?(am|pm)?\b", "", task).strip()

            scheduled.append((time_value, clean_task))

        else:
            unscheduled.append(task)

    return morning, afternoon, evening, tomorrow, daily, unscheduled, scheduled

def prioritize_tasks(tasks):

    urgent = []
    important = []
    later = []

    for _, task, _ in tasks:

        t = task.lower()

        if "today" in t or "asap" in t or "urgent" in t:
            urgent.append(task)

        elif "tomorrow" in t or "soon" in t:
            important.append(task)

        else:
            later.append(task)

    return urgent, important, later


def calculate_stats(tasks):

    total_tasks = len(tasks)

    completed_tasks = sum(1 for _, _, completed in tasks if completed)

    if total_tasks == 0:
        completion_rate = 0
    else:
        completion_rate = round((completed_tasks / total_tasks) * 100)

    return total_tasks, completed_tasks, completion_rate


if st.button("✨ Organize My Life", key="organize_button", use_container_width=True):

    if brain_dump.strip():

        ai_result = ai_organize_text(brain_dump)
        st.markdown(ai_result)

        goals, tasks, habits = organize_text(brain_dump)

        for t in tasks:
            add_task(t)

    else:
        st.warning("Please enter something in the brain dump.")
        goals, tasks, habits = [], [], []

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎯 Goals")
        for g in goals:
            st.write("•", g)

    with col2:
        st.subheader("📋 Tasks")
        for t in tasks:
            st.write("•", t)

    with col3:
        st.subheader("🔁 Habits")
        for h in habits:
            st.write("•", h)


st.subheader("📋 Saved Tasks")

tasks = get_tasks()

completed_count = 0

for task_id, task, completed in tasks:

    col1, col2 = st.columns([4,1])

    if completed:
        completed_count += 1

    with col1:
        if st.checkbox(task, value=completed, key=f"task_{task_id}"):
            if not completed:
                complete_task(task_id)
                update_streak(task_id)
                st.success("Task completed!")
                st.rerun()

    with col2:
        if st.button("❌", key=f"delete_{task_id}"):
            delete_task(task_id)
            st.rerun()
    

st.subheader("🗓 Daily Plan")

saved_tasks = get_tasks()


morning, afternoon, evening, tomorrow, daily, unscheduled, scheduled = generate_daily_plan(saved_tasks)

st.write("☀️ Morning")
for t in morning:
    st.write("•", t)

st.write("🌤 Afternoon")
for t in afternoon:
    st.write("•", t)

st.write("🌙 Evening")
for t in evening:
    st.write("•", t)

st.write("📅 Tomorrow")
for t in tomorrow:
    st.write("•", t)

st.write("🔁 Daily")
for t in daily:
    st.write("•", t)

st.write("📌 Unscheduled")
for t in unscheduled:
    st.write("•", t)

st.write("⏰ Scheduled")
for time, task in scheduled:
    st.write(f"{time} • {task}")
    

st.subheader("⚡ Task Priority")

saved_tasks = get_tasks()

urgent, important, later = prioritize_tasks(saved_tasks)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔥 Urgent")
    for t in urgent:
        st.write("•", t)

with col2:
    st.markdown("### ⚡ Important")
    for t in important:
        st.write("•", t)

with col3:
    st.markdown("### 🌱 Later")
    for t in later:
        st.write("•", t)

st.subheader("📊 Productivity Dashboard")

saved_tasks = get_tasks()

total_tasks, completed_tasks, completion_rate = calculate_stats(saved_tasks)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📋 Total Tasks", total_tasks)

with col2:
    st.metric("✅ Completed", completed_tasks)

with col3:
    st.metric("🎯 Completion Rate", f"{completion_rate}%")

st.subheader("🔥 Habit Streaks")

saved_tasks = get_tasks()

for task_id, task, completed in saved_tasks:

    if "daily" in task.lower() or "every" in task.lower():

        streak = get_streak(task_id)

        st.write(f"{task} 🔥 {streak} days")

