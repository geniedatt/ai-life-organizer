import streamlit as st

from database import init_db

# Core Pages
from ui.dashboard import dashboard_page
from ui.goals import goals_page
from ui.tasks import tasks_page
from ui.habits import habits_page
from ui.analytics import analytics_page
from ui.weekly import weekly_page
from ui.profile import profile_page

# AI Features
from ui.coach_chat import coach_chat_page
from ui.life_map import life_map_page
from ui.command_center import command_center_page
from ui.strategy_generator import strategy_generator_page
from ui.strategist import strategist_page
from ui.war_room import war_room_page

# Gamification / Viral Features
from ui.daily_plan import daily_plan_page
from ui.achievements import achievements_page
from ui.weekly_review import weekly_review_page
from ui.leaderboard import leaderboard_page


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------

init_db()


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Life Organizer",
    page_icon="🧠",
    layout="wide"
)


# -----------------------------
# PWA SUPPORT
# -----------------------------

st.markdown(
    """
    <link rel="manifest" href="/static/manifest.json">
    <meta name="theme-color" content="#0e1117">
    """,
    unsafe_allow_html=True
)


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------

st.sidebar.title("🧠 AI Life Organizer")

page = st.sidebar.radio(
    "Navigate",
    [

        # COMMAND
        "Dashboard",
        "AI Strategist",
        "War Room",

        # EXECUTION
        "Goals",
        "Tasks",
        "Habits",
        "Daily Plan",
        "Weekly Plan",

        # AI
        "AI Coach",
        "Life Map",
        "Command Center",
        "Life Strategy",

        # PERFORMANCE
        "Analytics",
        "Weekly Review",
        "Achievements",
        "Leaderboard",

        # ACCOUNT
        "Profile",
    ]
)


# -----------------------------
# PAGE ROUTING
# -----------------------------

if page == "Dashboard":
    dashboard_page()

elif page == "AI Strategist":
    strategist_page()

elif page == "War Room":
    war_room_page()

elif page == "Goals":
    goals_page()

elif page == "Tasks":
    tasks_page()

elif page == "Habits":
    habits_page()

elif page == "Daily Plan":
    daily_plan_page()

elif page == "Weekly Plan":
    weekly_page()

elif page == "AI Coach":
    coach_chat_page()

elif page == "Life Map":
    life_map_page()

elif page == "Command Center":
    command_center_page()

elif page == "Life Strategy":
    strategy_generator_page()

elif page == "Analytics":
    analytics_page()

elif page == "Weekly Review":
    weekly_review_page()

elif page == "Achievements":
    achievements_page()

elif page == "Leaderboard":
    leaderboard_page()

elif page == "Profile":
    profile_page()