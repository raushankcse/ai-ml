# import necessary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai


# set the page configuration
st.set_page_config(page_title="VitalImage Analytics", page_icon=":robot:")

# set the logo


# set the title
st.title("Vial image analytics")

#set the subtitle

st.subheader("An application that can help users to identify medical image")

uploaded_file = st.file_uploader("Upload the medical image", type = ["png", "jpg", "jpeg"])