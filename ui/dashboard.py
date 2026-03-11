import streamlit as st

from database import get_tasks, get_habits
from ai.planner import weekly_plan
from services.strategy_service import build_full_strategy
from ai.daily_briefing import generate_daily_briefing


def dashboard_page():

    # -----------------------------
    # DAILY BRIEFING
    # -----------------------------

    st.subheader("Daily Briefing")

    tasks = get_tasks()
    habits = get_habits()

    st.write(f"You have {len(tasks)} tasks.")

    # Generate briefing once per session
    if "daily_briefing" not in st.session_state:

        with st.spinner("Preparing your daily briefing..."):

            briefing = generate_daily_briefing(tasks, habits)

            if briefing:
                st.session_state.daily_briefing = briefing

    if "daily_briefing" in st.session_state:
        st.markdown(st.session_state.daily_briefing)

    # -----------------------------
    # AI LIFE STRATEGY
    # -----------------------------

    st.subheader("🧠 AI Life Strategy")

    life_input = st.text_area(
        "Brain dump everything on your mind (goals, worries, ideas, things you want to improve)",
        placeholder="Example: I want to get healthier, start a business, spend more time with family, and feel less stressed."
    )

    if st.button("Generate Life Plan"):

        if life_input.strip():

            with st.spinner("Generating your AI life strategy..."):

                strategy = build_full_strategy(life_input)

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