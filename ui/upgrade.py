import streamlit as st
from services.stripe_service import create_checkout_session

def upgrade_page():

    st.title("🚀 Upgrade to Pro")

    st.write("Unlock AI Coach, Strategy Engine, Analytics")

    if st.button("Upgrade Now"):
        url = create_checkout_session(st.session_state.user["id"])
        st.markdown(f"[Click here to pay]({url})")


