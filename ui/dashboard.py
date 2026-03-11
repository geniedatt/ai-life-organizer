import streamlit as st

from database import get_tasks, add_task, get_habits, add_habit
from ai.life_strategy import generate_life_strategy
from ai.task_generator import generate_tasks_from_strategy
from ai.habit_generator import generate_habits_from_strategy
from ai.planner import weekly_plan


def dashboard_page():

    # -----------------------------
    # DAILY BRIEFING
    # -----------------------------

    st.subheader("Daily Briefing")

    tasks = get_tasks()
    st.write(f"You have {len(tasks)} tasks.")

    habits = get_habits()

    if habits:
        st.subheader("🔥 Daily Habits")

        for habit in habits:
            st.checkbox(habit[1], key=habit[0])

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

                strategy = generate_life_strategy(life_input)

                if strategy:

                    st.session_state.life_strategy = strategy

                    # -----------------------------
                    # GENERATE TASKS
                    # -----------------------------

                    tasks_generated = generate_tasks_from_strategy(strategy)

                    for task in tasks_generated:

                        clean_task = task.replace("-", "").strip()

                        if clean_task:
                            add_task(clean_task)

                    # -----------------------------
                    # GENERATE HABITS
                    # -----------------------------

                    habits_generated = generate_habits_from_strategy(strategy)

                    for habit in habits_generated:

                        clean_habit = habit.replace("-", "").strip()

                        if clean_habit:
                            add_habit(clean_habit)

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