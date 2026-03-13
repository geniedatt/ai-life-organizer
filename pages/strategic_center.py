import streamlit as st
from engine.strategic_center import generate_command_center

def strategic_center_page():

    st.title("🧠 AI Strategic Command Center")

    data = generate_command_center()

    col1, col2, col3 = st.columns(3)

    col1.metric("XP", data["xp"])
    col2.metric("Level", data["level"])
    col3.metric("Task Completion", f"{data['completion_rate']*100:.0f}%")

    st.subheader("🎯 Strategic Focus")

    for f in data["focus"]:
        st.write("•", f)

    st.subheader("📣 AI Briefing")
    st.write(data["briefing"])