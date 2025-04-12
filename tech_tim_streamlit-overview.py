# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st

# Separate sections (for different parts of the tutorial)
# =========================================================
section1 = False  # st.write and Magic
section2 = False  # Streamlit Data Flow
section3 = False  # Text Elements
section4 = False  # Images
section5 = False  # Data Elements
section6 = False  # Chart Elements
section7 = True  # Form Elements
# =========================================================

# ---------------------------
# 1) st.write and Magic
# ---------------------------
if section1:
    # st.write is considered a "magic command" in streamlit because
    # it will automatically write pretty much anything you give it.
    # Regular text (string)
    st.write("hello world 123")
    # Python object, like key, value pair
    st.write({"key": "value"})
    # Boolean value
    st.write(True)
    # Numbers (no string quotes)
    st.write(123456)

    # Magic (whatever we write in line, even a variable, will appear on the page)
    "This is magic"
    x = (7 * 4) // 2
    # Write the variable x
    x
    # Write (the result of) an expression
    "hello world" if False else "bye"

# ---------------------------
# 2) Streamlit Data Flow
# ---------------------------
elif section2:
    '''Anytime something must be updated on the screen,
        Streamlit reruns your entire script from top to bottom...'''

    # State tracking
    pressed = st.button("Press Me")
    print("First:", pressed)

    pressed2 = st.button("Second Button")
    print("Second:", pressed2)

    "Check the terminal output after each button press!"
    "You will see that both buttons can never have the same state (of True or False)."
    print()  # Blank space between terminal lines

# ---------------------------
# 3) Text Elements
# ---------------------------
elif section3:
    # Display different text elements
    st.title("Super Simple Title")
    st.header("This is a header")
    st.subheader('Subheader')
    st.markdown("This is **Markdown!**")
    st.caption("small text")
    # Display a code snippet (with syntax highlighting)
    code_example = """
    def greet(name):
        print('hello', name)
    """
    st.code(code_example, language="python")
    # Divider
    st.divider()

# ---------------------------
# 4) Images
# ---------------------------
elif section4:
    # Remember to import os module
    import os
    # Display an image
    st.image(os.path.join(os.getcwd(), "static", "STL-at-night.jpg"))  # Optional arguments width, height

# ---------------------------
# 5) Data Elements
# ---------------------------
elif section5:
    import pandas as pd

    # Title
    st.title("Streamlit Elements Demo")

    # Dataframe section
    st.subheader("Dataframe")
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 32, 37, 45],
        'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
    })
    st.dataframe(df)

    # Data Editor Section (Editable dataframe)
    st.subheader("Data Editor")
    editable_df = st.data_editor(df)
    print(editable_df)

    # Static Table Section
    st.subheader("Static Table")
    st.table(df)

    # Metrics Section
    st.subheader("Metrics")
    st.metric(label="Total Rows", value=len(df))
    st.metric(label="Average Age", value=round(df['Age'].mean(), 1))

    # JSON and Dict Section
    st.subheader("JSON and Dictionary")
    st.write("JSON view:")
    sample_dict = {
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "Data Science", "Machine Learning"]
    }
    st.json(sample_dict)

    # Also show it as dictionary
    st.write("Dictionary view:", sample_dict)

    # Explanation
    st.write("Notice how the above two views are the EXACT same. This is because Streamlit treats a Python dictionary like JSON by default.")

# ---------------------------
# 6) Chart Elements
# ---------------------------
elif section6:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Title
    st.title("Streamlit Charts Demo")

    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )

    # Area Chart Section
    st.subheader("Area Chart")
    st.area_chart(chart_data)

    # Bar Chart Section
    st.subheader("Bar Chart")
    st.bar_chart(chart_data)

    # Line Chart Section
    st.subheader("Line Chart")
    st.line_chart(chart_data)

    # Scatter Chart Section
    st.subheader("Scatter Chart")
    scatter_data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    })
    st.scatter_chart(scatter_data)

    # Map Section (displaying random points on a map)
    st.subheader("Map")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],  # Coordinates around SF
        columns=['lat', 'lon']
    )
    st.map(map_data)

    # Pyplot section
    st.subheader("Pyplot Chart")
    fig, ax = plt.subplots()
    ax.plot(chart_data['A'], label='A')
    ax.plot(chart_data['B'], label='B')
    ax.plot(chart_data['C'], label='C')
    ax.set_title("Pyplot Line Chart")
    ax.legend()
    st.pyplot(fig)

# ---------------------------
# 7) Form Elements
# ---------------------------
elif section7:
    import pandas as pd

    # Title
    st.title("Streamlit Form Demo")

    # Form to hold the interactive elements
    with st.form(key="sample_form"):

        # Text Input
        st.subheader("Text Inputs")
        name = st.text_input("Enter your name")
        feedback = st.text_area("Provide your feedback")

        # Date and Time Inputs
        st.subheader("Date and Time Inputs")
        dob = st.date_input("Select your date of birth")
        time = st.time_input("Choose a preferred time")

        # Selectors
        st.subheader("Selectors")
        choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3'])
        gender = st.selectbox("Select your gender", ['Male', 'Female', 'Other'])
        slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])

        # Toggles and Checkboxes
        st.subheader("Toggles & Checkboxes")
        notifications = st.checkbox("Receive notifications?")
        toggle_value = st.checkbox("Enable dark mode?", value=False)

        # Submit Button for the Form
        submit_button = st.form_submit_button(label="Submit")

