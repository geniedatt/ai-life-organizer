import streamlit as st
from ai.auto_planner import generate_daily_plan


def daily_plan_page():

    st.title("📅 AI Daily Plan")

    plan = generate_daily_plan()

    st.subheader("Morning")

    for item in plan["morning"]:
        st.write("•", item)

    st.subheader("Afternoon")

    for item in plan["afternoon"]:
        st.write("•", item)

    st.subheader("Evening")

    for item in plan["evening"]:
        st.write("•", item)