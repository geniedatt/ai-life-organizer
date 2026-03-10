import streamlit as st

def goals_page():

    st.subheader("🎯 Goals")

    if "goal_actions" in st.session_state:

        st.markdown(st.session_state.goal_actions)

    else:

        st.info("No goals yet. Use the Brain Dump.")

