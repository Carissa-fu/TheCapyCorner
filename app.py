import streamlit as st
import json
import os
import random
import pandas as pd
from datetime import datetime

# Function to load custom CSS
def load_css():
    css = """
    <style>
    /* Set the background color */
    body {
        background-color: #EAE7E2;
    }
    
    /* Style the sidebar background */
    [data-testid="stSidebar"] {
        background-color: #D7E2E8;
    }
    
    /* Style the title text */
    h1 {
        color: #B9CBD9;
        text-align: center;
    }
    
    /* Style the text areas (input boxes) */
    textarea, input {
        background-color: #FEDDD8 !important;
        border: 2px solid #FCC9C5 !important;
        color: black !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    /* Style the submit button */
    div.stButton > button {
        background-color: #CFE3E2 !important;
        color: black !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        padding: 8px 16px !important;
    }
    
    /* Style the tabs */
    .stTabs {
        background-color: #D7E2E8 !important;
    }
    
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load the custom CSS
load_css()

# Function to load journal entries
def load_entries():
    if os.path.exists("entries.json"):
        with open("entries.json", "r") as file:
            return json.load(file)
    return []

# Function to save journal entries
def save_entries(entries):
    with open("entries.json", "w") as file:
        json.dump(entries, file)

# Function to load logs
def load_log():
    if os.path.exists("log.json"):
        with open("log.json", "r") as file:
            return json.load(file)
    return []

# Function to save logs
def save_log(logs):
    with open("log.json", "w") as file:
        json.dump(logs, file)
# List of affirmations
affirmations = {
    "happy": [
        "Keep up the great work!",
        "Happiness is contagious, spread it around!",
        "You are a beacon of joy!"
    ],
    "sad": [
        "It's okay to feel sad sometimes.",
        "Take one step at a time.",
        "You are stronger than you think."
    ],
    "angry": [
        "Take a deep breath and relax.",
        "Try to channel your anger into something productive.",
        "It's okay to feel angry, just don't let it control you."
    ],
    "anxious": [
        "Focus on what you can control.",
        "Take deep breaths to calm your mind.",
        "Everything will be okay."
    ],
    "excited": [
        "Enjoy the moment!",
        "Share your excitement with others!",
        "Keep the positive energy flowing!"
    ],
    "stressed": [
        "Take a break and relax.",
        "Try some deep breathing exercises.",
        "Focus on one task at a time."
    ]
}

# Function to get a random affirmation
def get_affirmation(mood):
    if mood.lower() in affirmations:
        return random.choice(affirmations[mood.lower()])
    else:
        return "Thank you for sharing your feelings."

# Load existing entries into session state
if "entries" not in st.session_state:
    st.session_state.entries = load_entries()

if "log" not in st.session_state:
    st.session_state.log = load_log()

st.image("capybara3.png")
st.text("⋆ ˚｡⋆୨ The Capy Corner ୧⋆ ˚｡⋆")
st.title("Capy Mood Tracker and Journal")

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Mood Tracker", "Mental Health Resources", "Healthy Habits"])

# Mood Tracker
# Tab 1: Mood Tracker
with tab1:
    # Form to collect mood and journal entry
    with st.form(key="journal_form"):
        mood = st.selectbox("How are you feeling?", ["Happy", "Sad", "Angry", "Anxious", "Excited", "Stressed", "Other"])
        journal_entry = st.text_area("What's on your mind?")
        submit_button = st.form_submit_button(label="Submit")

    # Handle form submission
    if submit_button:
        entry = {"mood": mood, "journal_entry": journal_entry}
        st.session_state.entries.append(entry)
        save_entries(st.session_state.entries)
        st.success("Your entry has been saved!")
        st.write(get_affirmation(mood))
        if mood.lower() == "stressed":
            st.warning("Coping Strategies: Take a break, try some deep breathing exercises, and focus on one task at a time.")

    # Display previous entries with delete functionality
    st.header("Previous Entries")
    for index, entry in enumerate(st.session_state.entries):
        st.subheader(f"Mood: {entry['mood']}")
        st.write(entry["journal_entry"])

        # Create a delete button for each entry
        delete_button = st.button(f"Delete Entry {index+1}", key=f"delete_{index}")
        
        # When the delete button is clicked, remove the entry
        if delete_button:
            st.session_state.entries.pop(index)
            save_entries(st.session_state.entries)
            # Here we are simply updating the session state directly without using st.experimental_rerun or reloading
            st.success(f"Entry {index+1} has been deleted.")
            break  # Prevents index shift error after deleting an entry

        st.write("---")

# Tab 2: Mental Health Resources for Adolescents
with tab2:
    st.header("Mental Health Resources for Adolescents")
    st.write("Here are some helpful resources for mental health support:")
    
    with st.expander("National Suicide Prevention Lifeline"):
        st.write("Call 1-800-273-TALK (1-800-273-8255) for 24/7 confidential support.")
    
    with st.expander("Crisis Text Line"):
        st.write("Text HOME to 741741 to connect with a trained crisis counselor.")
    
    with st.expander("Teen Mental Health Resources"):
        st.write("Visit [Teen Mental Health](https://teenmentalhealth.org) for more information on mental health topics.")
    
    with st.expander("Adolescent Counseling Services"):
        st.write("[Counseling services](https://www.counsellingtorontoteens.com/) designed for adolescents can help guide you through difficult situations.")

# Tab 3: Building Healthy Habits
with tab3:
    st.header("Building Healthy Habits")
    st.write("Here are some tips for building and maintaining healthy habits:")

    with st.expander("Establish a Morning Routine"):
        st.write("Start each day with a positive and calming routine. This could include activities like journaling, stretching, or enjoying a nutritious breakfast. Establishing a morning routine is crucial for adolescents as it sets the tone for the day ahead. A consistent routine helps create structure, reduces stress, and boosts productivity by allowing teens to start their day with purpose. Incorporating calming activities, like stretching, journaling, or enjoying a healthy breakfast, can enhance mental well-being, improve focus, and foster a sense of control. By making mornings predictable and positive, adolescents can feel more prepared and confident in handling the challenges of their day.")
    
    with st.expander("Set Achievable Goals"):
        st.write("Set specific, measurable, achievable, relevant, and time-bound (SMART) goals. Track your progress to stay motivated.")
    
    with st.expander("Get Active"):
        st.write("Exercise regularly to improve your physical and mental health. Find an activity that you enjoy, such as walking, yoga, or dancing. Being active is essential for adolescents as it not only improves physical health but also supports mental well-being. Regular exercise boosts energy levels, enhances mood, and reduces stress, making it easier to manage school and social pressures. Whether it's through sports, dancing, or simple activities like walking or stretching, staying active promotes better sleep, improves focus, and increases overall happiness. Encouraging physical activity helps teens build healthy habits that last a lifetime and contribute to both their physical and emotional resilience.")
    
    with st.expander("Stay Hydrated"):
        st.write("Drinking enough water helps your body function optimally and improves mood and energy levels.")
    
    with st.expander("Prioritize Sleep"):
        st.write("Aim for 7-9 hours of sleep per night. A consistent sleep schedule helps boost mental and physical well-being. Prioritizing sleep is vital for adolescents as it supports both physical and mental health. During sleep, the body repairs itself, consolidates memories, and recharges energy levels. Teenagers need 7-9 hours of sleep to improve mood, focus, and academic performance. Consistent sleep patterns can help regulate emotions, reduce stress, and boost cognitive function, leading to better decision-making and problem-solving. By establishing a regular sleep schedule, adolescents can enhance their overall well-being, improve mental clarity, and feel more energized to take on daily challenges.")
    