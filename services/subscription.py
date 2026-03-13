import streamlit as st


def is_pro_user():

    if "pro_user" not in st.session_state:
        st.session_state.pro_user = False

    return st.session_state.pro_user


def activate_pro():

    st.session_state.pro_user = True