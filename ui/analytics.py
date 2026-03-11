import streamlit as st
from database import get_tasks, get_habits


def analytics_page():

    st.title("📊 Productivity Analytics")

    tasks = get_tasks()
    habits = get_habits()

    total_tasks = len(tasks)
    total_habits = len(habits)

    completed_tasks = sum(task[2] for task in tasks)

    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tasks", total_tasks)
    col2.metric("Completed Tasks", completed_tasks)
    col3.metric("Active Habits", total_habits)

    if tasks:

        completion_rate = (completed_tasks / total_tasks) * 100

        st.subheader("Task Completion Rate")

        st.progress(completion_rate / 100)

        st.write(f"{completion_rate:.1f}% of tasks completed")