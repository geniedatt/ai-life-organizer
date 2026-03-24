import streamlit as st
from services.auth import sign_in, sign_up

def login_page():

    st.title("🔐 Login")

    mode = st.radio("Select", ["Login", "Sign Up"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):

        if mode == "Sign Up":
            res = sign_up(email, password)
        else:
            res = sign_in(email, password)

        if "access_token" in res:
            st.session_state.token = res["access_token"]
            st.session_state.user = res["user"]
            st.success("Logged in!")
            st.rerun()
        else:
            st.error(res)