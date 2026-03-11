from ai.goal_parser import extract_goals
import streamlit as st
import streamlit as st

def goals_page():

    st.subheader("🎯 Top Life Goals")

    if "life_strategy" in st.session_state:

        goals = extract_goals(st.session_state.life_strategy)

        if goals:

            for goal in goals:
                st.markdown(f"- {goal}")

        else:
            st.info("No goals detected yet.")

    else:
        st.info("Generate a life strategy first.")

