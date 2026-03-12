import streamlit as st
from services.achievement_service import get_achievements


def achievements_page():

    st.title("🏆 Achievements")

    achievements = get_achievements()

    if not achievements:
        st.info("No achievements yet. Start completing tasks!")

    for a in achievements:
        st.success(a)