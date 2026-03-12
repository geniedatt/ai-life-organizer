import streamlit as st
from datetime import date
from database import get_habits, get_habit_activity, calculate_xp


def war_room_page():

    st.title("⚔️ Daily War Room")
    xp, level = calculate_xp()

    st.metric("🏆 Life XP", xp)
    st.caption(f"LEVEL {level}")

    habits = get_habits()

    if not habits:
        st.info("Generate a life strategy first to create your battle plan.")
        return



    # -----------------------------
    # TODAY'S EXECUTION SCORE
    # -----------------------------

    today_completed = 0

    for habit in habits:

        habit_id = habit[0]

        activity = get_habit_activity(habit_id)

        if not activity:
            continue

        for record in activity:
            if str(record[0]) == str(date.today()):
                today_completed += 1
                break

    total = len(habits)

    score = int((today_completed / total) * 100) if total else 0


    st.metric("⚡ Execution Score", f"{score}/100")


    # -----------------------------
    # STATUS MESSAGE
    # -----------------------------

    if score == 100:
        st.success("🏆 DAY WON. Elite execution.")

    elif score >= 70:
        st.info("Strong execution. Finish the remaining targets.")

    elif score >= 40:
        st.warning("Momentum building. Stay focused.")

    else:
        st.error("Battle not started. Execute your first habit.")


    st.divider()


    # -----------------------------
    # TODAY'S TARGETS
    # -----------------------------

    st.subheader("🎯 Today's Targets")

    for habit in habits:

        habit_name = habit[1]

        st.write(f"☐ {habit_name}")


    st.divider()


    # -----------------------------
    # WIN THE DAY BUTTON
    # -----------------------------

    if score == 100:

        if st.button("🏆 WIN THE DAY"):

            st.success("SYSTEM UPDATE: Day completed with elite execution.")

            xp, level = calculate_xp()

            st.markdown(
                f"""
    ### 🏆 DAILY WIN

    Execution Score: **100**

    Life XP: **{xp}**

    Level: **{level}**

    Streak Momentum: **Rising**

    #AI Life Organizer
    """
            )

            st.balloons()