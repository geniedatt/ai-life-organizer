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
    # HABIT OF THE WEEK
    # -----------------------------

    top_habit = habits[0]

    st.subheader("🏆 Habit of the Week")

    st.success(
        f"{top_habit[1]}\n\n"
        f"You're on a **{top_habit[2]} day streak**. Keep the momentum going!"
    )

    st.divider()

    # -----------------------------
    # AI HABIT COACH
    # -----------------------------

    st.subheader("🤖 AI Habit Coaching")

    weak_habits = [h for h in habits if h[2] == 0]

    if weak_habits:

        habit = weak_habits[0]

        st.warning(
            f"You haven't started **{habit[1]}** yet.\n\n"
            "Try doing a **5-minute version today** to kickstart the streak."
        )

    else:

        st.info(
            "Great job! All your habits have active streaks. Keep building momentum."
        )

    st.divider()

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
