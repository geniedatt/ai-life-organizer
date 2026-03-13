import streamlit as st
from engine.life_orchestrator import run_life_orchestrator

def orchestrator_page():


    st.title("🧠 AI Strategic Command Center")

    # -------------------------
    # RUN LIFE ORCHESTRATOR
    # -------------------------

    data = run_life_orchestrator()

    life_score = data.get("life_score", 0)
    task_completion = data.get("task_completion", 0)
    habit_strength = data.get("habit_strength", 0)

    chief = data.get("chief_of_staff", {})
    trajectory = data.get("trajectory", {})
    adaptive = data.get("adaptive_strategy", [])

    # -------------------------
    # EXECUTIVE METRICS
    # -------------------------

    st.subheader("⚡ Executive Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Life Score",
        value=life_score
    )

    col2.metric(
        label="Task Completion %",
        value=task_completion
    )

    col3.metric(
        label="Habit Strength",
        value=habit_strength
    )

    st.divider()

    # -------------------------
    # LIFE TRAJECTORY
    # -------------------------

    st.subheader("📈 Life Trajectory Forecast")

    if trajectory:

        prediction = trajectory.get("prediction", "")
        trajectory_status = trajectory.get("trajectory", "")

        st.info(prediction)

        st.write("**Trajectory Status:**", trajectory_status)

    else:

        st.info("No trajectory data available yet.")

    st.divider()

    # -------------------------
    # CHIEF OF STAFF BRIEFING
    # -------------------------

    st.subheader("🧠 Chief of Staff Briefing")

    if chief:

        focus = chief.get("focus", [])
        risks = chief.get("risks", [])
        advice = chief.get("advice", [])

        if focus:

            st.write("### 🎯 Strategic Focus")

            for item in focus:
                st.write("•", item)

        if risks:

            st.write("### ⚠ Strategic Risks")

            for risk in risks:
                st.warning(risk)

        if advice:

            st.write("### 🤖 AI Advice")

            for tip in advice:
                st.write("•", tip)

    else:

        st.info("Chief of Staff analysis not available.")

    st.divider()

    # -------------------------
    # ADAPTIVE STRATEGY
    # -------------------------

    st.subheader("⚙ Adaptive Strategy")

    if adaptive:

        for change in adaptive:
            st.write("•", change)

    else:

        st.info("No adaptive strategy changes suggested yet.")

    st.divider()

    # -------------------------
    # EXECUTIVE SUMMARY
    # -------------------------

    st.subheader("📊 System Summary")

    st.write(
    """
```

This Command Center analyzes your **tasks, habits, and momentum** to determine
your current life trajectory and provide strategic guidance.

The AI system continuously evaluates:

• Execution consistency
• Habit momentum
• Strategic risks
• Future trajectory

Use this dashboard daily to guide your decisions.
"""
)
