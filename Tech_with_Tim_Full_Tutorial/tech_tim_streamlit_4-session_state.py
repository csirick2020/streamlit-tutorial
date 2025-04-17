# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st

# Split this section into subsections
example_without_session_state = False
example_with_session_state = True

if example_without_session_state:

    # A simple counter variable, without session state
    counter = 0

    st.write(f"Counter value: {counter}")

    # Button to increment the counter
    if st.button("Increment Counter"):
        counter += 1
        st.write(f"Counter incremented to {counter}")
    else:
        st.write(f"Counter stays at {counter}")

    # In the above example, the Counter will never go past 1 b/c every time we press
    # the counter button, we're resetting its value to 0 (since the script reruns).

    # This is why we need session state...

if example_with_session_state:

    # If counter doesn't already exist in our "state"
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    # If button is pressed
    if st.button("Increment Counter"):
        st.session_state.counter += 1
        st.write(f"Counter incremented to {st.session_state.counter}")

    # If button is pressed
    if st.button("Reset"):
        st.session_state.counter = 0

    # If the following line were placed above the two (button) 'if
    # statements', the Counter value would always lag behind by one.
    st.write(f"Counter value: {st.session_state.counter}")

    # NOTE: Each session is "per user, per browser reload"
    # ----- This means if a user hits Refresh in their
    # ----- browser, the session will be reset.
