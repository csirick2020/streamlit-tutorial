# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st
from datetime import datetime  # To set mix, max dates on st.date_input

st.title("User Information Form")

# Initialize a dictionary for form values
form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

# A form kind of handles its own "state" internally...
with st.form(key="user_info_form"):  # 'key' gives the form a unique identifier
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["dob"] = st.date_input('Enter your birthdate', min_value=min_date, max_value=max_date)

    submit_button = st.form_submit_button(label="Submit")  # You NEED to have a submit button (in any form)
    if submit_button:
        # Handle if one or more fields are left empty
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            # display the submitted info
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
