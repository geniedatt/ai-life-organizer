import streamlit as st


def leaderboard_page():

    st.title("🔥 Habit Streak Leaderboard")

    leaderboard = [
        ("Alex", 52),
        ("Sarah", 48),
        ("You", 31),
        ("Chris", 22)
    ]

    for rank, (name, streak) in enumerate(leaderboard, start=1):

        st.write(f"{rank}. {name} — {streak} day streak")