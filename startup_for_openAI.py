import streamlit as st
import json
from openai import OpenAI

st.title("AI Life Organizer")

client = OpenAI(api_key="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")

brain_dump = st.text_area("Write everything on your mind")

if st.button("Organize My Life", key="organize_button"):

    prompt = f"""
Organize the following text into JSON with three categories:
goals, tasks, habits.

Text:
{brain_dump}

Return ONLY valid JSON in this format:
{{
"goals": [],
"tasks": [],
"habits": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You organize messy thoughts."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    try:
        data = json.loads(result)

        st.subheader("🎯 Goals")
        for g in data["goals"]:
            st.write("•", g)

        st.subheader("📋 Tasks")
        for t in data["tasks"]:
            st.write("•", t)

        st.subheader("🔁 Habits")
        for h in data["habits"]:
            st.write("•", h)

    except:
        st.write(result)