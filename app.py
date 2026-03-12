import streamlit as st

from database import init_db
from ui.dashboard import dashboard_page
from ui.goals import goals_page
from ui.tasks import tasks_page
from ui.habits import habits_page
from ui.analytics import analytics_page
from ui.weekly import weekly_page
from ui.war_room import war_room_page
from ui.strategist import strategist_page
from ui.profile import profile_page
from ui.coach_chat import coach_chat_page
from ui.life_map import life_map_page
from ui.command_center import command_center_page
from ui.strategy_generator import strategy_generator_page
from ui.daily_plan import daily_plan_page
from ui.achievements import achievements_page
from ui.weekly_review import weekly_review_page
from ui.leaderboard import leaderboard_page



# Initialize database
init_db()

st.set_page_config(
    page_title="AI Life Organizer",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <link rel="manifest" href="/static/manifest.json">
    <meta name="theme-color" content="#0e1117">
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------

st.sidebar.title("🧠 AI Life Organizer")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "AI Strategist",  # ⭐ NEW DAILY COMMAND CENTER
        "War Room",       
        "Goals",
        "Tasks",
        "Habits",
        "Weekly Plan",
        "Analytics",
        "Profile",
        "AI Coach",
        "Life Map",
        "Command Center",
        "Life Strategy",
        "Daily Plan",
        "Achievements",
        "Weekly Review",
        "Leaderboard"

    ]
)

# -----------------------------
# PAGE ROUTING
# -----------------------------

if page == "War Room":
    war_room_page()

elif page == "Daily Plan":
    daily_plan_page()

elif page == "Achievements":
    achievements_page()

elif page == "Weekly Review":
    weekly_review_page()

elif page == "Leaderboard":
    leaderboard_page()

elif page == "Life Strategy":
    strategy_generator_page()

elif page == "Command Center":
    command_center_page()

elif page == "Life Map":
    life_map_page()

elif page == "AI Coach":
    coach_chat_page()

elif page == "Profile":
    profile_page()

elif page == "AI Strategist":
    strategist_page()

elif page == "Dashboard":
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