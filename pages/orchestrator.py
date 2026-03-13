import streamlit as st

from engine.life_orchestrator import run_life_orchestrator


def orchestrator_page():

    st.title("🧠 AI Life Orchestrator")

    with st.spinner("Analyzing your life systems..."):

        data = run_life_orchestrator()

    st.metric("🌍 Life Score", data["life_score"])
    st.metric("✅ Task Completion", f"{data['task_completion']}%")
    st.metric("🔥 Habit Strength", data["habit_strength"])

    st.divider()

    st.subheader("🧠 Chief of Staff Advice")
    st.write(data["chief_of_staff"])

    st.divider()

    st.subheader("📈 Life Trajectory")
    st.write(data["trajectory"])

    st.divider()

    st.subheader("⚙️ Adaptive Strategy")
    st.write(data["adaptive_strategy"])