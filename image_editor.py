# YouTube URL: https://www.youtube.com/watch?v=ckOAnis8lWg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=22

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Image file uploader
image = st.file_uploader("Upload Your Image", type=["jpg", "png", "jpeg"])

# Placeholders for image properties
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    info.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    # Get user input
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    # Get user input
    degree = st.number_input("Degree")
    st.markdown("<h2 style='text-align: center;'>Filters</h2>", unsafe_allow_html=True)
    # Get input via "dropdown" style box
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))
    # Add button for submission
    s_btn = st.button("Submit")
    if s_btn:  # If button is clicked
        # Apply editing changes
        edited = img.resize((width, height)).rotate(degree)
        filtered=edited
        if filters != None:
            if filters == "Blur":
                filtered = edited.filter(BLUR)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered = edited.filter(EMBOSS)
            else:  # User chose "Smooth"
                filtered = edited.filter(SMOOTH)
        st.image(filtered)
