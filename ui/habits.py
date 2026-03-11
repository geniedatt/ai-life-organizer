import pandas as pd
import plotly.express as px
from datetime import date, timedelta
import streamlit as st

from database import (
    get_habits,
    log_habit_completion,
    calculate_streak,
    get_habit_activity
)

# --------------------------------------------------
# HABIT HEATMAP CALENDAR
# --------------------------------------------------

def render_habit_heatmap(habit_id):

    activity = get_habit_activity(habit_id)

    if not activity:
        st.info("No activity yet for this habit.")
        return

    df = pd.DataFrame(activity, columns=["date"])

    df["date"] = pd.to_datetime(df["date"])
    df["completed"] = 1

    start_date = date.today() - timedelta(days=365)
    end_date = date.today()

    all_days = pd.DataFrame({
        "date": pd.date_range(start_date, end_date)
    })

    df = all_days.merge(df, on="date", how="left")
    df["completed"] = df["completed"].fillna(0)

    df["day"] = df["date"].dt.weekday
    df["week"] = df["date"].dt.isocalendar().week

    fig = px.density_heatmap(
        df,
        x="week",
        y="day",
        z="completed",
        nbinsx=53,
        nbinsy=7,
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        height=250,
        margin=dict(t=20, b=20, l=20, r=20),
        yaxis=dict(
            tickmode="array",
            tickvals=[0,1,2,3,4,5,6],
            ticktext=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        )
    )

    st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# MOMENTUM SCORE
# --------------------------------------------------

def calculate_momentum_score(habits):

    total_possible = len(habits) * 7
    total_completed = 0

    for habit in habits:

        habit_id = habit[0]
        activity = get_habit_activity(habit_id)

        if not activity:
            continue

        df = pd.DataFrame(activity, columns=["date"])
        df["date"] = pd.to_datetime(df["date"])

        last_week = df[
            df["date"] >= pd.Timestamp.today() - pd.Timedelta(days=7)
        ]

        total_completed += len(last_week)

    if total_possible == 0:
        return 0

    score = int((total_completed / total_possible) * 100)

    return score


# --------------------------------------------------
# HABITS PAGE
# --------------------------------------------------

def habits_page():

    st.title("🔥 Habit Streak Leaderboard")

    habits = get_habits()

    if not habits:
        st.info("No habits yet. Generate a life strategy first.")
        return

    # --------------------------------------------------
    # MOMENTUM SCORE
    # --------------------------------------------------

    momentum = calculate_momentum_score(habits)

    st.metric("⚡ Momentum Score", f"{momentum}/100")

    if momentum >= 80:
        st.success("You're on fire. Your systems are working.")

    elif momentum >= 60:
        st.info("Solid progress. Stay consistent.")

    elif momentum >= 40:
        st.warning("Momentum is slipping. Focus on your core habits.")

    else:
        st.error("Your system is breaking down. Reset and rebuild momentum.")

    st.divider()

    # --------------------------------------------------
    # CALCULATE REAL STREAKS
    # --------------------------------------------------

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

    habit_data = sorted(
        habit_data,
        key=lambda x: x["streak"],
        reverse=True
    )

    if not habit_data:
        st.warning("No habit data available.")
        return

    # --------------------------------------------------
    # HABIT OF THE WEEK
    # --------------------------------------------------

    top_habit = habit_data[0]

    st.subheader("🏆 Habit of the Week")

    st.success(
        f"{top_habit['name']}\n\n"
        f"You're on a **{top_habit['streak']} day streak**. Keep the momentum going!"
    )

    st.divider()

    # --------------------------------------------------
    # AI HABIT COACH
    # --------------------------------------------------

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

    # --------------------------------------------------
    # TODAY'S HABITS
    # --------------------------------------------------

    st.subheader("✅ Today's Habits")

    for habit in habit_data:

        habit_id = habit["id"]
        habit_name = habit["name"]
        streak = habit["streak"]

        checked = st.checkbox(habit_name, key=f"habit_{habit_id}")

        if checked and not st.session_state.get(f"logged_{habit_id}"):

            log_habit_completion(habit_id)
            st.session_state[f"logged_{habit_id}"] = True

            st.rerun()

        st.caption(f"🔥 {streak} day streak")

    st.divider()

    # --------------------------------------------------
    # TOP 3 HABITS
    # --------------------------------------------------

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

        remaining = habit_data[3:]

    else:

        remaining = habit_data

    st.divider()

    # --------------------------------------------------
    # FULL LEADERBOARD
    # --------------------------------------------------

    st.subheader("📊 Full Habit Rankings")

    start_rank = 4 if len(habit_data) >= 3 else 1

    for i, habit in enumerate(remaining, start=start_rank):

        st.markdown(
            f"**{i}. {habit['name']}** — 🔥 {habit['streak']} days"
        )

    st.divider()

    # --------------------------------------------------
    # HABIT CALENDAR
    # --------------------------------------------------

    st.subheader("📅 Habit Consistency Calendar")

    habit_names = {h["name"]: h["id"] for h in habit_data}

    selected_habit = st.selectbox(
        "Select Habit",
        list(habit_names.keys())
    )

    render_habit_heatmap(habit_names[selected_habit])