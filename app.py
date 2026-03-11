import streamlit as st

from database import init_db
from ui.dashboard import dashboard_page
from ui.goals import goals_page
from ui.tasks import tasks_page
from ui.habits import habits_page
from ui.analytics import analytics_page
from ui.weekly import weekly_page

# Initialize database
init_db()

st.set_page_config(
    page_title="AI Life Organizer",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------

st.sidebar.title("🧠 AI Life Organizer")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "Goals",
        "Tasks",
        "Habits",
        "Weekly Plan",
        "Analytics"
    ]
)

# -----------------------------
# PAGE ROUTING
# -----------------------------

if page == "Dashboard":
    dashboard_page()

elif page == "Goals":
    goals_page()

elif page == "Tasks":
    tasks_page()

elif page == "Habits":
    habits_page()

elif page == "Weekly Plan":
    weekly_page()

elif page == "Analytics":
    analytics_page()