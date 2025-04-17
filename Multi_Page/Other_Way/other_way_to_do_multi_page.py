# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

import streamlit as st
import pandas as pd
import numpy as np

# Define page functions
def intro():
    st.title("Welcome to My App")
    st.write("""
             This is the introduction page. Use the dropdown to navigate to different demos.
    """)

def plotting_demo():
    st.title("Plotting Demo")
    st.write("Here, we create a simple plot.")

    # Example plot with random data
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

def mapping_demo():
    st.title("Mapping Demo")
    st.write("This page shows a map with random points.")

    # Generate some random geospatial data
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"]
    )
    st.map(map_data)

def data_frame_demo():
    st.title("DataFrame Demo")
    st.write("Here we display a sample data frame.")

    # Display a sample data frame
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Column A", "Column B", "Column C"]
    )
    st.dataframe(df)

# Dictionary to map page names to functions
page_names_to_funcs = {
    "-": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

# Sidebar for page navigation
selected_page = st.sidebar.selectbox("Choose a page", options=page_names_to_funcs.keys())

# Run the function associated with the selected page
page_names_to_funcs[selected_page]()
