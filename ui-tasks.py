import streamlit as st
from database import add_task,get_tasks,complete_task,delete_task

def tasks_page():

    st.subheader("Tasks")

    new_task = st.text_input("Add task")

    if st.button("Add"):

        if new_task:
            add_task(new_task)

    tasks=get_tasks()

    for task_id,task,done in tasks:

        col1,col2=st.columns([4,1])

        with col1:

            if st.checkbox(task,value=done,key=f"task_{task_id}"):

                if not done:
                    complete_task(task_id)
                    st.rerun()

        with col2:

            if st.button("❌",key=f"del{task_id}"):

                delete_task(task_id)
                st.rerun()
