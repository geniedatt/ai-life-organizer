import streamlit as st
import plotly.graph_objects as go
from database import get_tasks, get_habits


def life_map_page():

    st.title("🧬 Life Map")

    tasks = get_tasks()
    habits = get_habits()

    labels = ["Life System"]

    parents = [""]

    values = [10]

    for task in tasks:
        labels.append(task[1])
        parents.append("Life System")
        values.append(5)

    for habit in habits:
        labels.append(habit[1])
        parents.append("Life System")
        values.append(3)

    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values
    ))

    st.plotly_chart(fig, use_container_width=True)