# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st

st.write("### Button Example")

# In the below example, if we did not add the 'key' parameter/argument,
# We would get an error from Streamlit (Error: DuplicateElementId)
st.button("Ok")
st.write("The button below must have parameter 'key' equals some value.")
st.write("If it didn't, we would get an error since the buttons are the same.")
st.write("Error: Streamlit-DuplicateElementID")
st.button("Ok", key="btn2")

st.divider()

st.write("### Slider Example")
wrong_way = False
right_way = True
if wrong_way:
    st.write("This is the wrong way...")
    min_value = st.slider("Set min. value", 0, 50, 25)
    slider_value = st.slider("Slider", min_value, 100, min_value)
elif right_way:
    st.write("This is the right way...")
    # To fix the wrong way, we need to store the value
    # of the slider in our session state
    if "slider" not in st.session_state:
        st.session_state.slider = 25

    min_value = st.slider("Set min value", 0, 50, 25)

    st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)

st.divider()

st.write("### Checkbox Example")
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    # The user input below will get destroyed as we toggle our checkbox
    # To avoid this, we need to add the 'value' parameter and set it
    # equal to our session_state.user_input
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: {user_input}")
