import streamlit as st
from database import get_tasks, get_weekly_plan, save_weekly_plan
from ai.planner import weekly_plan


def weekly_page():

    st.title("📅 Weekly Plan")

    tasks = get_tasks()

    if not tasks:
        st.info("No tasks available yet.")
        return

    task_list = [task[1] for task in tasks]

    # Check session first
    if "weekly_plan" not in st.session_state:

        # Check database
        saved_plan = get_weekly_plan()

        if saved_plan:
            st.session_state.weekly_plan = saved_plan

        else:
            with st.spinner("Generating weekly plan..."):

                plan = weekly_plan(task_list)

                if plan:
                    st.session_state.weekly_plan = plan
                    save_weekly_plan(plan)

    st.markdown(st.session_state.weekly_plan)

    if st.button("🔄 Regenerate Weekly Plan"):

        with st.spinner("Updating plan..."):

            plan = weekly_plan(task_list)

            if plan:
                st.session_state.weekly_plan = plan
                save_weekly_plan(plan)