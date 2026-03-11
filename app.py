from database import init_db
import streamlit as st

from ui.dashboard import dashboard_page
from ui.tasks import tasks_page
from ui.goals import goals_page
from ui.habits import habits_page
from analytics.insights import analytics_page

init_db()

st.set_page_config(
    page_title="AI Life Organizer",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Life Organizer")
st.caption("Turn thoughts into organized goals, tasks, and habits.")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Dashboard",
    "Tasks",
    "Goals",
    "Habits",
    "Analytics"
])

with tab1:
    dashboard_page()

with tab2:
    tasks_page()

with tab3:
    goals_page()

with tab4:
    habits_page()

with tab5:
    analytics_page()
    