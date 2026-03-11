import streamlit as st
from database import get_tasks
from ai.planner import weekly_plan


def weekly_page():

    st.title("📅 Weekly Plan")

    tasks = get_tasks()

    if not tasks:
        st.info("No tasks available yet.")
        return

    # Convert database rows into task list
    task_list = [task[1] for task in tasks]

    with st.spinner("Generating your weekly plan..."):

        plan = weekly_plan(task_list)

    if plan:
        st.markdown(plan)
    else:
        st.warning("Could not generate a weekly plan.")