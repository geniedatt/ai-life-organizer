import streamlit as st
from database import get_habits, log_habit_completion, calculate_streak


def habits_page():

    st.title("🔥 Habit Streak Leaderboard")

    habits = get_habits()

    if not habits:
        st.info("No habits yet. Generate a life strategy first.")
        return

    # ---------------------------------
    # CALCULATE REAL STREAKS
    # ---------------------------------

    habit_data = []

    for habit in habits:

        habit_id = habit[0]
        habit_name = habit[1]

        streak = calculate_streak(habit_id)

        habit_data.append({
            "id": habit_id,
            "name": habit_name,
            "streak": streak
        })

    # Sort by real streak
    habit_data = sorted(habit_data, key=lambda x: x["streak"], reverse=True)

    # -----------------------------
    # HABIT OF THE WEEK
    # -----------------------------

    top_habit = habit_data[0]

    st.subheader("🏆 Habit of the Week")

    st.success(
        f"{top_habit['name']}\n\n"
        f"You're on a **{top_habit['streak']} day streak**. Keep the momentum going!"
    )

    st.divider()

    # -----------------------------
    # AI HABIT COACH
    # -----------------------------

    st.subheader("🤖 AI Habit Coaching")

    weak_habits = [h for h in habit_data if h["streak"] == 0]

    if weak_habits:

        habit = weak_habits[0]

        st.warning(
            f"You haven't started **{habit['name']}** yet.\n\n"
            "Try doing a **5-minute version today** to kickstart the streak."
        )

    else:

        st.info(
            "Great job! All your habits have active streaks. Keep building momentum."
        )

    st.divider()

    # -----------------------------
    # TODAY'S HABITS
    # -----------------------------

    st.subheader("✅ Today's Habits")

    for habit in habit_data:

        habit_id = habit["id"]
        habit_name = habit["name"]

        checked = st.checkbox(habit_name, key=f"habit_{habit_id}")

        if checked:
            log_habit_completion(habit_id)

        streak = calculate_streak(habit_id)

        st.caption(f"🔥 {streak} day streak")

    st.divider()

    # -----------------------------
    # TOP 3 HABITS
    # -----------------------------

    if len(habit_data) >= 3:

        col1, col2, col3 = st.columns(3)

        gold = habit_data[0]
        silver = habit_data[1]
        bronze = habit_data[2]

        col1.metric(
            label=f"🥇 {gold['name']}",
            value=f"🔥 {gold['streak']} days"
        )

        col2.metric(
            label=f"🥈 {silver['name']}",
            value=f"🔥 {silver['streak']} days"
        )

        col3.metric(
            label=f"🥉 {bronze['name']}",
            value=f"🔥 {bronze['streak']} days"
        )

        st.divider()

        remaining = habit_data[3:]

    else:

        remaining = habit_data

    # -----------------------------
    # FULL LEADERBOARD
    # -----------------------------

    st.subheader("📊 Full Habit Rankings")

    for i, habit in enumerate(remaining, start=4):

        st.markdown(
            f"**{i}. {habit['name']}** — 🔥 {habit['streak']} days"
        )
