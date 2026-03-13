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

# AI Systems
from ui.coach_chat import coach_chat_page
from ui.life_map import life_map_page
from ui.strategy_generator import strategy_generator_page

# Command Center
from pages.orchestrator import orchestrator_page

# Monetization
from pages.upgrade import upgrade_page

# Performance
from ui.daily_plan import daily_plan_page
from ui.achievements import achievements_page
from ui.weekly_review import weekly_review_page
from ui.leaderboard import leaderboard_page


# -------------------------
# INITIALIZE DATABASE
# -------------------------
init_db()

st.set_page_config(
    page_title="AI Life Organizer",
    page_icon="🧠",
    layout="wide"
)

# -------------------------
# PWA SUPPORT
# -------------------------
st.markdown(
    """
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#0e1117">
""",
    unsafe_allow_html=True
)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🧠 AI Life Organizer")

page = None

# -------------------------
# COMMAND CENTER
# -------------------------
st.sidebar.header("⚡ Command")

if st.sidebar.button("Dashboard"):
    page = "dashboard"

if st.sidebar.button("Command Center"):
    page = "command_center"

# -------------------------
# EXECUTION
# -------------------------
st.sidebar.header("🎯 Execution")

if st.sidebar.button("Goals"):
    page = "goals"

if st.sidebar.button("Tasks"):
    page = "tasks"

if st.sidebar.button("Habits"):
    page = "habits"

if st.sidebar.button("Daily Plan"):
    page = "daily_plan"

if st.sidebar.button("Weekly Plan"):
    page = "weekly"

# -------------------------
# AI SYSTEMS
# -------------------------
st.sidebar.header("🤖 AI Systems")

if st.sidebar.button("AI Coach"):
    page = "coach"

if st.sidebar.button("Life Map"):
    page = "life_map"

if st.sidebar.button("Life Strategy"):
    page = "life_strategy"

# -------------------------
# PERFORMANCE
# -------------------------
st.sidebar.header("📈 Performance")

if st.sidebar.button("Analytics"):
    page = "analytics"

if st.sidebar.button("Weekly Review"):
    page = "weekly_review"

if st.sidebar.button("Achievements"):
    page = "achievements"

if st.sidebar.button("Leaderboard"):
    page = "leaderboard"

# -------------------------
# ACCOUNT
# -------------------------
st.sidebar.header("👤 Account")

if st.sidebar.button("Profile"):
    page = "profile"

if st.sidebar.button("Upgrade to Pro 🚀"):
    page = "upgrade"

# -------------------------
# DEFAULT PAGE
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if page:
    st.session_state.page = page

# -------------------------
# ROUTING
# -------------------------
if st.session_state.page == "dashboard":
    dashboard_page()

elif st.session_state.page == "command_center":
    orchestrator_page()

elif st.session_state.page == "goals":
    goals_page()

elif st.session_state.page == "tasks":
    tasks_page()

elif st.session_state.page == "habits":
    habits_page()

elif st.session_state.page == "daily_plan":
    daily_plan_page()

elif st.session_state.page == "weekly":
    weekly_page()

elif st.session_state.page == "coach":
    coach_chat_page()

elif st.session_state.page == "life_map":
    life_map_page()

elif st.session_state.page == "life_strategy":
    strategy_generator_page()

elif st.session_state.page == "analytics":
    analytics_page()

elif st.session_state.page == "weekly_review":
    weekly_review_page()

elif st.session_state.page == "achievements":
    achievements_page()

elif st.session_state.page == "leaderboard":
    leaderboard_page()

elif st.session_state.page == "profile":
    profile_page()

elif st.session_state.page == "upgrade":
    upgrade_page()