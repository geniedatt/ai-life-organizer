import streamlit as st
from engine.life_orchestrator import run_life_orchestrator
from engine.executive_briefing import generate_executive_briefing
from engine.strategic_planner import generate_daily_strategy
from engine.schedule_generator import generate_daily_schedule


def orchestrator_page():

    st.title("🧠 AI Strategic Command Center")

    # -------------------------
    # DAILY EXECUTIVE BRIEFING
    # -------------------------

    briefing = generate_executive_briefing()

    st.subheader("🧠 Daily Executive Briefing")

    st.info(briefing.get("summary", ""))

    if briefing.get("focus"):
        st.write("### 🎯 Strategic Focus")
        for f in briefing["focus"]:
            st.write("•", f)

    if briefing.get("risks"):
        st.write("### ⚠ Risks")
        for r in briefing["risks"]:
            st.warning(r)

    if briefing.get("advice"):
        st.write("### 🤖 Strategic Advice")
        for a in briefing["advice"]:
            st.write("•", a)

    st.divider()

    # -------------------------
    # AI STRATEGIC PLANNER
    # -------------------------

    st.subheader("🚀 AI Strategic Planner")

    top_tasks = generate_daily_strategy()

    if top_tasks:

        st.write("### Today's Top Strategic Tasks")

        for task in top_tasks:
            st.success(task)

    else:
        st.info("No tasks available to plan today.")

    st.divider()

    # -------------------------
    # AI DAILY SCHEDULE
    # -------------------------

    st.subheader("🗓 AI Daily Schedule")

    schedule = generate_daily_schedule()

    if schedule:

        for block in schedule:
            st.write(f"**{block['time']}** — {block['task']}")

    else:
        st.info("No tasks available to schedule today.")

    st.divider()

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

    col1.metric("Life Score", life_score)
    col2.metric("Task Completion %", task_completion)
    col3.metric("Habit Strength", habit_strength)

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