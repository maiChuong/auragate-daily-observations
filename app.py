import streamlit as st
import json

# Example CrewAI JSON output (replace with actual pipeline output)
sample_output = {
    "title": "AuraGate Daily Observations",
    "date": "February 25, 2026",
    "recipient": "Executive Team",
    "executive_summary": "Vietnam is rapidly positioning itself as a key player in the global tech landscape...",
    "key_themes": [
        "AI Regulation",
        "Cryptocurrency Dynamics",
        "Investment Opportunities",
        "Renewable Energy Growth",
        "Workforce Development"
    ],
    "detailed_analysis": [
        {"heading": "Vietnam's First Standalone AI Law", "content": "On February 5, 2026, Vietnam enacted its first standalone AI law..."},
        {"heading": "Cryptocurrency Landscape", "content": "In light of Bitcoin's recent downturn..."},
        {"heading": "Investment Trends", "content": "With a focus on AI and semiconductor technologies..."},
    ],
    "forward_implications": "As Vietnam navigates the complexities of technological advancements...",
    "next_steps": [
        "Schedule a strategy meeting to discuss insights.",
        "Identify key stakeholders for partnership opportunities."
    ],
    "closing_note": "Thank you for your attention to these critical developments."
}

st.title("AuraGate Daily Observations Preview")

# Editable fields
title = st.text_input("Title", sample_output["title"])
date = st.text_input("Date", sample_output["date"])
recipient = st.text_input("Recipient", sample_output["recipient"])
executive_summary = st.text_area("Executive Summary", sample_output["executive_summary"])

st.subheader("Key Themes")
edited_themes = []
for theme in sample_output["key_themes"]:
    edited_themes.append(st.text_input("Theme", theme))

st.subheader("Detailed Analysis")
edited_analysis = []
for section in sample_output["detailed_analysis"]:
    heading = st.text_input("Heading", section["heading"])
    content = st.text_area("Content", section["content"])
    edited_analysis.append({"heading": heading, "content": content})

forward_implications = st.text_area("Forward-Looking Implications", sample_output["forward_implications"])

st.subheader("Next Steps")
edited_steps = []
for step in sample_output["next_steps"]:
    edited_steps.append(st.text_input("Step", step))

closing_note = st.text_area("Closing Note", sample_output["closing_note"])

# Buttons for workflow
col1, col2 = st.columns(2)
with col1:
    if st.button("Approve"):
        st.success("Report approved for dispatch.")
with col2:
    if st.button("Reject"):
        st.error("Report rejected. Please revise.")

# Export options
st.download_button("Download JSON", data=json.dumps(sample_output, indent=2), file_name="daily_observations.json")
