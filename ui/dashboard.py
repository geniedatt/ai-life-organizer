from ai.life_strategy import generate_life_strategy
from ai.planner import weekly_plan
from database import get_tasks
import streamlit as st


def dashboard_page():

    st.subheader("Daily Briefing")

    tasks = get_tasks()

    st.write(f"You have {len(tasks)} tasks.")

    # -----------------------------
    # AI LIFE STRATEGY SECTION
    # -----------------------------

    st.subheader("🧠 AI Life Strategy")

    life_input = st.text_area(
        "Describe your life goals, problems, or ambitions",
        placeholder="Example: I want to get healthier, learn coding, and start a business..."
    )

    if st.button("Generate Life Plan"):

        if life_input.strip():

            with st.spinner("Generating your AI life strategy..."):

                strategy = generate_life_strategy(life_input)

                if strategy:
                    st.session_state.life_strategy = strategy

        else:
            st.warning("Please describe your goals first.")

    # -----------------------------
    # DISPLAY LIFE STRATEGY
    # -----------------------------

    if "life_strategy" in st.session_state:

        st.subheader("🚀 Your 30 Day Life Strategy")

        st.markdown(st.session_state.life_strategy)

    # -----------------------------
    # WEEKLY PLAN
    # -----------------------------

    if tasks:

        plan = weekly_plan(tasks)

        if plan:
            st.subheader("📅 Weekly Plan")
            st.markdown(plan)
            