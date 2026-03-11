import streamlit as st
from ai.goal_parser import extract_goals


def goals_page():

    st.title("🎯 Life Goals")

    if "life_strategy" in st.session_state:

        goals = extract_goals(st.session_state.life_strategy)

        if goals:
            for goal in goals:
                st.markdown(f"- {goal}")
        else:
            st.info("No goals detected.")

    else:
        st.info("Generate a life strategy from the dashboard first.")