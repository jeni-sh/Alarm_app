import streamlit as st
from datetime import datetime
import time

st.title("⏰ Alarm Clock")

alarm_time = st.text_input("Enter alarm time (HH:MM:SS)")

if "alarm_set" not in st.session_state:
    st.session_state.alarm_set = False

if st.button("Set Alarm"):
    st.session_state.alarm_set = True
    st.session_state.time = alarm_time

current_time = datetime.now().strftime("%H:%M:%S")
st.write("Current Time:", current_time)

if st.session_state.alarm_set:
    if current_time == st.session_state.time:
        st.error("⏰ Wake up!")

        audio_file = open("alarm.wav", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/wav")

        st.session_state.alarm_set = False

# Refresh every second
time.sleep(1)
st.rerun()