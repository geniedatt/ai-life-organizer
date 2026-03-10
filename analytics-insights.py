import streamlit as st
from database import get_tasks

def analytics_page():

    tasks = get_tasks()

    total = len(tasks)

    completed = sum(1 for _,_,done in tasks if done)

    rate = 0 if total==0 else round((completed/total)*100)

    st.subheader("📊 Productivity")

    col1,col2,col3 = st.columns(3)

    col1.metric("Tasks",total)
    col2.metric("Completed",completed)
    col3.metric("Completion",f"{rate}%")
