import streamlit as st
from services.xp_service import calculate_xp
from database import get_habits


def profile_page():

    st.title("🏆 My Progress Profile")

    xp, level = calculate_xp()

    habits = get_habits()

    total_streak = sum(h[2] for h in habits) if habits else 0

    st.metric("🏆 Level", level)
    st.metric("⚡ Total XP", xp)
    st.metric("🔥 Total Habit Streak", total_streak)

    st.divider()

    st.subheader("Habit Streaks")

    if habits:

        for habit in habits:

            name = habit[1]
            streak = habit[2]

            st.write(f"**{name}** — 🔥 {streak} days")

    else:

        st.info("No habits yet.")

    st.divider()

    st.subheader("Share Your Progress")

    st.write(
        "Soon you'll be able to share your public progress page with friends."
    )