import streamlit as st

from services.xp_service import calculate_xp
from database import get_tasks, get_habits
from ai.daily_briefing import generate_daily_briefing


def war_room_page():

    st.title("⚔️ AI War Room")

    st.subheader("Your Strategic Life Dashboard")

    # --------------------------------
    # LOAD DATA
    # --------------------------------

    tasks = get_tasks()
    habits = get_habits()

    xp, level = calculate_xp()

    briefing = generate_daily_briefing(tasks, habits)

    # --------------------------------
    # CORE METRICS
    # --------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric("XP", xp)
    col2.metric("Level", level)
    col3.metric("Momentum", briefing["momentum"])

    st.divider()

    # --------------------------------
    # SYSTEM STATUS
    # --------------------------------

    st.subheader("System Status")

    st.write(f"Active Tasks: {len(tasks)}")
    st.write(f"Active Habits: {len(habits)}")

    # --------------------------------
    # STRATEGIC PRIORITIES
    # --------------------------------

    st.subheader("Today's Strategic Priorities")

    for p in briefing["priorities"]:
        st.write(f"• {p}")

    st.divider()

    # --------------------------------
    # AI COMMANDER ADVICE
    # --------------------------------

    st.subheader("AI Commander Advice")

    st.info(briefing["advice"])