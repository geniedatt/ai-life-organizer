import streamlit as st
from ai.weekly_review import generate_weekly_review


def weekly_review_page():

    st.title("📊 Weekly AI Review")

    review = generate_weekly_review()

    st.write(review)