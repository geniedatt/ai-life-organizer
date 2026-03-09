import streamlit as st

st.title("AI Life Organizer")

brain_dump = st.text_area("Write everything on your mind")

def organize_text(text):
    goals = []
    tasks = []
    habits = []

    lines = text.split("\n")

    for line in lines:
        l = line.lower()

        if "learn" in l or "start" in l or "build" in l:
            goals.append(line)

        elif "clean" in l or "call" in l or "buy" in l:
            tasks.append(line)

        elif "every" in l or "daily" in l or "gym" in l:
            habits.append(line)

        else:
            tasks.append(line)

    return goals, tasks, habits


if st.button("Organize My Life", key="organize_button"):

    goals, tasks, habits = organize_text(brain_dump)

    st.subheader("🎯 Goals")
    for g in goals:
        st.write("•", g)

    st.subheader("📋 Tasks")
    for t in tasks:
        st.write("•", t)

    st.subheader("🔁 Habits")
    for h in habits:
        st.write("•", h)
