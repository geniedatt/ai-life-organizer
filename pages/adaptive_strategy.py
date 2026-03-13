import streamlit as st
from engine.adaptive_strategy import adjust_strategy


def adaptive_strategy_page():

    st.title("⚙ Adaptive Strategy Engine")

    adjustments = adjust_strategy()

    st.subheader("AI Strategy Adjustments")

    for a in adjustments:
        st.write("•", a)