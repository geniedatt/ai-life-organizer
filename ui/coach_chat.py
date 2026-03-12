import streamlit as st
from ai.life_coach import generate_coaching_response


def coach_chat_page():

    st.title("🧠 AI Life Coach")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask your life strategist anything...")

    if user_input:

        st.session_state.chat_history.append(("user", user_input))

        response = generate_coaching_response(user_input)

        st.session_state.chat_history.append(("ai", response))

    for role, message in st.session_state.chat_history:

        if role == "user":
            st.chat_message("user").write(message)

        else:
            st.chat_message("assistant").write(message)