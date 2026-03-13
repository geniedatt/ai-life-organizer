import streamlit as st

from engine.life_orchestrator import run_life_orchestrator


def orchestrator_page():

    st.title("🧠 AI Strategic Command Center")

    with st.spinner("Analyzing your life systems..."):
        data = run_life_orchestrator()

    st.divider()

    # --------------------------
    # Core Metrics
    # --------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric("🌍 Life Score", data["life_score"])
    col2.metric("✅ Task Completion", f'{data["task_completion"]}%')
    col3.metric("🔥 Habit Strength", data["habit_strength"])

    st.divider()

    # --------------------------
    # Trajectory
    # --------------------------

    st.subheader("📈 Future Trajectory")

    trajectory = data["trajectory"]

    st.write(f"**Trajectory:** {trajectory['trajectory']}")
    st.info(trajectory["prediction"])

    st.divider()

    # --------------------------
    # Chief of Staff
    # --------------------------

    st.subheader("🤖 Chief of Staff")

    st.write(data["chief_of_staff"])

    st.divider()

    # --------------------------
    # Adaptive Strategy
    # --------------------------

    st.subheader("🧠 Adaptive Strategy")

    st.write(data["adaptive_strategy"])