import streamlit as st
from ai.strategy_generator import generate_life_strategy


def strategy_generator_page():

    st.title("🧠 Life Strategy Generator")

    goal = st.text_input("Enter your major life goal")

    if st.button("Generate Strategy"):

        strategy = generate_life_strategy(goal)

        st.subheader("AI Life Strategy")

        st.write(strategy)