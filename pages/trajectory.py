import streamlit as st
from ai.trajectory_simulator import simulate_life_trajectory


def trajectory_page():

    st.title("🔮 Life Trajectory Simulator")

    result = simulate_life_trajectory()

    col1, col2, col3 = st.columns(3)

    col1.metric("Life Score", result["life_score"])
    col2.metric("Momentum", result["momentum"])
    col3.metric("Task Completion", f"{result['completion_rate']*100:.0f}%")

    st.subheader("📈 Current Trajectory")

    trajectory = result["trajectory"]

    if trajectory == "high_growth":
        st.success("🚀 High Growth")

    elif trajectory == "steady_progress":
        st.info("📈 Steady Progress")

    else:
        st.warning("⚠ Stagnation Risk")

    st.write(result["prediction"])