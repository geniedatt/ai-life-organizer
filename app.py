from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from ui.login import login_page
from ui.dashboard import dashboard_page
from ui.upgrade import upgrade_page

import os

st.write("SUPABASE_URL:", os.getenv("SUPABASE_URL"))

# -------------------------
# SESSION INIT
# -------------------------
if "token" not in st.session_state:
    st.session_state.token = None

if "user" not in st.session_state:
    st.session_state.user = None

# -------------------------
# AUTH CHECK
# -------------------------
if not st.session_state.token:
    login_page()
    st.stop()

# -------------------------
# NAVIGATION
# -------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Upgrade"]
)

if page == "Dashboard":
    dashboard_page()

elif page == "Upgrade":
    upgrade_page()