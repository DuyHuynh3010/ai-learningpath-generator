import streamlit as st
import json

st.set_page_config(page_title="AI Learning Path Generator", layout="centered")
st.title("📚 AI Learning Path Generator")

career_goal = st.text_input("Enter your career goal (e.g., 'Data Scientist'):")

if career_goal:
    with open("learning_paths.json", "r") as file:
        learning_paths = json.load(file)

    goal = career_goal.strip().title()

    if goal in learning_paths:
        st.success(f"Learning path for: {goal}")
        for stage, topics in learning_paths[goal].items():
            st.subheader(stage)
            for topic in topics:
                st.write(f"- {topic}")
    else:
        st.warning("Sorry, no learning path found for that goal.")