import streamlit as st
from database import get_tasks
from ai.planner import weekly_plan

def dashboard_page():

    tasks = get_tasks()

    st.subheader("Daily Briefing")

    st.write(f"You have {len(tasks)} tasks.")

    plan = weekly_plan(tasks)

    if plan:
        st.subheader("Weekly Plan")
        st.markdown(plan)
