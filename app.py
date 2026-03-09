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
from database import add_task, get_tasks, complete_task

import os
api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st

st.title("AI Life Organizer")

brain_dump = st.text_area("Write everything on your mind")

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


if st.button("Organize My Life", key="organize_button"):

    goals, tasks, habits = organize_text(brain_dump)

    st.subheader("🎯 Goals")
    for g in goals:
        st.write("•", g)

    st.subheader("📋 Tasks")
    for t in tasks:
        add_task(t)
        st.write("•", t)

    st.subheader("🔁 Habits")
    for h in habits:
        st.write("•", h)

st.subheader("🗂 Saved Tasks")

saved_tasks = get_tasks()

for task in saved_tasks:
    task_id = task[0]
    task_text = task[1]
    completed = task[2]

    if completed:
        st.write(f"✅ {task_text}")
    else:
        if st.button(f"Complete: {task_text}", key=f"task_{task_id}"):
            complete_task(task_id)
            st.experimental_rerun()
