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
from database import add_task, get_tasks, complete_task, delete_task
import os
import streamlit as st

api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Life Organizer")
st.caption("Turn your thoughts into organized goals, tasks, and habits.")
st.divider()

brain_dump = st.text_area(
    "🧠 Brain Dump",
    placeholder="Write everything on your mind...\n\nExample:\nCall mom\nBuy groceries\nStart learning Python\nGo to the gym daily",
    height=200
)

def organize_text(text):
    goals = []
    tasks = []
    habits = []

    lines = text.split("\n")

    for line in lines:
        l = line.lower()

        if "learn" in l or "start" in l or "build" in l:
            goals.append(line)

        elif "clean" in l or "call" in l or "buy" in l:
            tasks.append(line)

        elif "every" in l or "daily" in l or "gym" in l:
            habits.append(line)

        else:
            tasks.append(line)

    return goals, tasks, habits


def generate_daily_plan(tasks):
    morning = []
    afternoon = []
    evening = []

    for i, task in enumerate(tasks):
        task_text = task[1]

        if i % 3 == 0:
            morning.append(task_text)
        elif i % 3 == 1:
            afternoon.append(task_text)
        else:
            evening.append(task_text)

    return morning, afternoon, evening


if st.button("✨ Organize My Life", key="organize_button", use_container_width=True):

    goals, tasks, habits = organize_text(brain_dump)

    for t in tasks:
        add_task(t)

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
                st.success("Task completed!")
                st.rerun()

    with col2:
        if st.button("❌", key=f"delete_{task_id}"):
            delete_task(task_id)
            st.rerun()
    

st.subheader("🗓 Daily Plan")

saved_tasks = get_tasks()

morning, afternoon, evening = generate_daily_plan(saved_tasks)

st.write("☀️ Morning")
for t in morning:
    st.write("•", t)

st.write("🌤 Afternoon")
for t in afternoon:
    st.write("•", t)

st.write("🌙 Evening")
for t in evening:
    st.write("•", t)
