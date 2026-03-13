import streamlit as st
from ai.chief_of_staff import chief_of_staff_advice


def chief_of_staff_page():

    st.title("🧠 Personal AI Chief of Staff")

    report = chief_of_staff_advice()

    state = report["state"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Life Score", state["life_score"])
    col2.metric("Momentum", state["momentum"])
    col3.metric("Task Completion", f"{state['completion_rate']*100:.0f}%")

    st.subheader("🎯 Strategic Focus")

    for f in report["focus"]:
        st.write("•", f)

    if report["risks"]:

        st.subheader("⚠ Risks")

        for r in report["risks"]:
            st.warning(r)

    st.subheader("🧭 Chief of Staff Advice")

    for a in report["advice"]:
        st.info(a)