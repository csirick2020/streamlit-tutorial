# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st

# Separate the examples
wrong_way = False
right_way = True

if wrong_way:
    st.write("This is the wrong way.")

    if "step" not in st.session_state:
        st.session_state.step = 1

    if "info" not in st.session_state:
        st.session_state.info = {}

    if st.session_state.step == 1:
        st.header("Part 1: Info")

        name = st.text_input("Name", value=st.session_state.info.get("name", ""))

        # Because of the Streamlit flow and the way it re-runs the entire
        # script when a state change occurs, this code will not work...

        # That is to say, we will have to push the "Next" or the "Back"
        # button twice to get anywhere, instead of just once - (which is
        # both impractical and confusing for any user).

        if st.button("Next"):
            st.session_state.info["name"] = name
            st.session_state.step = 2

    elif st.session_state.step == 2:
        st.header("Part 2: Review")

        st.subheader("Please review this:")
        st.write(f"**Name**: {st.session_state.info.get('name', '')}")

        if st.button("Submit"):
            st.success("Great!")
            st.balloons()
            st.session_state.info = {}

        if st.button("Back"):
            st.session_state.step = 1

# In order to fix the problem above, we need to use 'callbacks'
if right_way:
    st.write("This is the right way.")

    if "step" not in st.session_state:
        st.session_state.step = 1

    if "info" not in st.session_state:
        st.session_state.info = {}

    # Here is our 'callback' function
    def go_to_step2(name):
        st.session_state.info["name"] = name
        st.session_state.step = 2

    def go_to_step1():
        st.session_state.step = 1

    if st.session_state.step == 1:
        st.header("Part 1: Info")

        name = st.text_input("Name", value=st.session_state.info.get("name", ""))

        st.button("Next", on_click=go_to_step2, args=(name,))

    if st.session_state.step == 2:
        st.header("Part 2: Review")

        st.subheader("Please review this:")
        st.write(f"**Name**: {st.session_state.info.get('name', '')}")

        if st.button("Submit"):
            st.success("Great!")
            st.balloons()
            st.session_state.info = {}

        st.button("Back", on_click=go_to_step1)
