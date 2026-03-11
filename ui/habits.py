import streamlit as st
from database import get_habits


def habits_page():

    st.title("🔥 Habit Streak Leaderboard")

    habits = get_habits()

    if not habits:
        st.info("No habits yet. Generate a life strategy first.")
        return

    # Sort by streak
    habits = sorted(habits, key=lambda x: x[2], reverse=True)

    # -----------------------------
    # TOP 3 HABITS
    # -----------------------------

    if len(habits) >= 3:

        col1, col2, col3 = st.columns(3)

        gold = habits[0]
        silver = habits[1]
        bronze = habits[2]

        col1.metric(
            label=f"🥇 {gold[1]}",
            value=f"🔥 {gold[2]} days"
        )

        col2.metric(
            label=f"🥈 {silver[1]}",
            value=f"🔥 {silver[2]} days"
        )

        col3.metric(
            label=f"🥉 {bronze[1]}",
            value=f"🔥 {bronze[2]} days"
        )

        st.divider()

        remaining = habits[3:]

    else:

        remaining = habits

    # -----------------------------
    # FULL LEADERBOARD
    # -----------------------------

    st.subheader("📊 Full Habit Rankings")

    for i, habit in enumerate(remaining, start=4):

        habit_name = habit[1]
        streak = habit[2]

        st.markdown(f"**{i}. {habit_name}** — 🔥 {streak} days")
