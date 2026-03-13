import streamlit as st

from engine.strategic_center import generate_command_center
from engine.life_score import calculate_life_score
from engine.momentum import calculate_momentum

from database import get_tasks, get_habits, get_habit_activity
from ai.strategic_alerts import generate_alerts


def ai_life_dashboard():

    st.title("🧠 AI Life Dashboard")

    tasks = get_tasks()
    habits = get_habits()
    from database import get_all_habit_activity

    habit_logs = get_all_habit_activity()

    # Core metrics
    life_score = calculate_life_score(tasks, habits)
    momentum = calculate_momentum(habit_logs)

    command_data = generate_command_center()

    alerts = generate_alerts(tasks)

    # --------------------------
    # TOP METRICS
    # --------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric("Life Score", life_score)
    col2.metric("Momentum", f"{momentum}%")
    col3.metric("Level", command_data["level"])

    # --------------------------
    # STRATEGIC FOCUS
    # --------------------------

    st.subheader("🎯 Strategic Focus")

    for f in command_data["focus"]:
        st.write("•", f)

    # --------------------------
    # ALERTS
    # --------------------------

    if alerts:

        st.subheader("⚠ Strategic Alerts")

        for a in alerts:
            st.warning(a)

    # --------------------------
    # AI DAILY BRIEFING
    # --------------------------

    st.subheader("📣 AI Daily Briefing")

    st.write(command_data["briefing"])

    # --------------------------
    # DAILY EXECUTION
    # --------------------------

    st.subheader("✅ Today's Execution")

    today_tasks = [t for t in tasks if not t["completed"]][:5]

    for t in today_tasks:

        st.write("⬜", t["title"])