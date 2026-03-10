import streamlit as st
from database import get_tasks,get_streak

def habits_page():

    st.subheader("🔥 Habit Streaks")

    tasks=get_tasks()

    for task_id,task,done in tasks:

        if "daily" in task.lower():

            streak=get_streak(task_id)

            st.write(f"{task} 🔥 {streak} days")
