import streamlit as st


def strategist_page():

    st.title("🧠 AI Life Strategist")

    st.write("Answer a few questions to generate your life strategy.")

    # --------------------------------
    # QUESTIONS
    # --------------------------------

    life_goal = st.text_area(
        "Where do you want your life to be in 3 years?"
    )

    focus_area = st.selectbox(
        "Which area needs the most improvement?",
        ["Health", "Career", "Finances", "Productivity", "Relationships"]
    )

    struggle = st.text_area(
        "What habits do you struggle with most?"
    )

    # --------------------------------
    # GENERATE STRATEGY
    # --------------------------------

    if st.button("Generate Life Strategy"):

        st.subheader("📜 Your Life Strategy")

        st.markdown(
            f"""
### Focus Area
{focus_area}

### 3 Year Vision
{life_goal}

### Key Habit Focus
{struggle}

### Recommended Daily Habits
• Exercise
• Deep Work
• Reading
• Drink Water

### Weekly Systems
• Weekly planning
• Habit review
• Goal progress check
"""
        )