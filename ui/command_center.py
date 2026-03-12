import streamlit as st
from engine.command_center import get_command_center


def command_center_page():

    st.title("🧠 AI Strategic Command Center")

    data = get_command_center()

    col1, col2, col3 = st.columns(3)

    col1.metric("XP", data["xp"])
    col2.metric("Level", data["level"])
    col3.metric("Momentum", data["momentum"])

    st.divider()

    st.subheader("System Diagnostics")

    st.write(f"Task Pressure: {data['task_pressure']}")
    st.write(f"Habit Stability: {data['habit_stability']}")

    st.divider()

    st.subheader("Strategic Focus")

    st.success(data["strategic_focus"])

    st.divider()

    st.subheader("Today's Priorities")

    for p in data["priorities"]:
        st.write(f"• {p}")

    st.divider()

    st.subheader("AI Commander Advice")

    st.info(data["advice"])