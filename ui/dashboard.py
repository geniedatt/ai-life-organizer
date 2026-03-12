import streamlit as st

from database import (
    get_tasks,
    get_habits,
    get_weekly_plan,
    save_weekly_plan,
    update_habit_streak
)

from ai.planner import weekly_plan
from services.strategy_service import build_full_strategy
from ai.daily_briefing import generate_daily_briefing
from services.mission_service import generate_daily_mission


def dashboard_page():

    st.title("🧠 AI Life Organizer")

    tasks = get_tasks()
    habits = get_habits()

    # --------------------------------------------------
    # DAILY BRIEFING
    # --------------------------------------------------

    st.subheader("🧠 Daily Briefing")

    if "daily_briefing" not in st.session_state:

        with st.spinner("Preparing your daily briefing..."):

            briefing = generate_daily_briefing()

            if briefing:
                st.session_state.daily_briefing = briefing

    if "daily_briefing" in st.session_state:

        briefing = st.session_state.daily_briefing

        st.metric("Momentum", briefing["momentum"])

        st.write("### 🎯 Top Priorities Today")

        for p in briefing["priorities"]:
            st.write(f"• {p}")

        st.write("### 🧭 System Advice")

        st.info(briefing["advice"])

        col1, col2 = st.columns(2)

        col1.metric("⚡ XP", briefing["xp"])
        col2.metric("🏆 Level", briefing["level"])

    st.divider()

    # -----------------------------
    # DAILY MISSION
    # -----------------------------

    st.subheader("🎯 Today's Mission")

    if "daily_mission" not in st.session_state:

        mission = generate_daily_mission()
        st.session_state.daily_mission = mission

    for step, item in enumerate(st.session_state.daily_mission, start=1):

        st.write(f"{step}. {item}")

    st.divider()

    # --------------------------------------------------
    # DAILY HABITS
    # --------------------------------------------------

    if habits:

        st.subheader("🔥 Daily Habits")

        col1, col2, col3 = st.columns(3)

        col1.markdown("### 🏃 Health")
        col2.markdown("### 💼 Work")
        col3.markdown("### 🧠 Learning")

        health_keywords = ["exercise", "water", "health", "stretch", "sleep", "workout"]
        work_keywords = ["business", "code", "project", "mvp", "software", "build"]
        learning_keywords = ["study", "learn", "read", "course", "ai"]

        for habit in habits:

            habit_id = habit[0]
            habit_name = habit[1]
            streak = habit[2]

            label = f"{habit_name} — 🔥 {streak} day streak"
            lower = habit_name.lower()

            if any(k in lower for k in health_keywords):

                completed = col1.checkbox(label, key=f"habit_{habit_id}")

            elif any(k in lower for k in learning_keywords):

                completed = col3.checkbox(label, key=f"habit_{habit_id}")

            else:

                completed = col2.checkbox(label, key=f"habit_{habit_id}")

            if completed and not st.session_state.get(f"logged_{habit_id}"):

                update_habit_streak(habit_id)
                st.session_state[f"logged_{habit_id}"] = True

                st.rerun()

    st.divider()

    # --------------------------------------------------
    # AI LIFE STRATEGY
    # --------------------------------------------------

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

    # --------------------------------------------------
    # DISPLAY LIFE STRATEGY
    # --------------------------------------------------

    if "life_strategy" in st.session_state:

        st.subheader("🚀 Your 30 Day Life Strategy")

        st.markdown(st.session_state.life_strategy)

    st.divider()

    # --------------------------------------------------
    # WEEKLY PLAN
    # --------------------------------------------------

    if tasks:

        stored_plan = get_weekly_plan()

        if not stored_plan:

            with st.spinner("Creating your weekly plan..."):

                stored_plan = weekly_plan(tasks)

                if stored_plan:
                    save_weekly_plan(stored_plan)

        if stored_plan:

            st.subheader("📅 Weekly Plan")

            st.markdown(stored_plan)