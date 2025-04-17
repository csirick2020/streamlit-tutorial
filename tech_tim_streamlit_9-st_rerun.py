# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

# Forces the app to re-run itself,
# which can help solve problems we
# saw in previous examples.

import streamlit as st

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1

    # Look at the line below...
    # If it were commented out, our counter
    # would always be lagging behind by one.
    st.rerun()  # Manually invoke a rerun to update the state for us

st.write(f"Current Count: {st.session_state.count}")

if st.button("Increment and Update Immediately"):
    increment_and_rerun()
