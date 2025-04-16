# Tech with Tim YouTube URL: https://youtu.be/o8p7uQCGD0U?si=IMFm2bjI1tH-8Ti1

# Use 'streamlit run APP_NAME.py' in terminal to run the application

# This example (for the cache_resource part) is not written all that well
# because once we hit 'Close File', there is no way to open it back up
# besides completely killing the web server and then re-running it.
# (A refresh of the page will not open it back up)

# Other than the above, at least the tutorial does
# effectively show us the two methods of caching

import streamlit as st
import time

# Separate sections
cache_data = False
cache_resource = True

if cache_data:
    # cache_data is only for immutable types
    @st.cache_data(ttl=60)  # Cache this data for 60 seconds (Remove it for "permanent" cache)
    def fetch_data():
        # Simulate a slow data-fetching process
        time.sleep(3)  # Delays to mimic an API call
        return {"data": "This is cached data!"}

    st.write("Fetching data...")
    data = fetch_data()
    st.write(data)

elif cache_resource:
    file_path = "example.txt"

    # cache_resource is mutable (meaning the resource can be changed)
    @st.cache_resource
    def get_file_handler():
        # Open the file in append mode, which creates the file if it doesn't exist
        file = open(file_path, "a+")
        return file

    # Use the cached file handler
    file_handler = get_file_handler()

    # Write to the file using the cached handler
    if st.button("Write to File"):
        file_handler.write("New line of text\n")
        file_handler.flush()  # Ensure the content is written immediately
        st.success("Wrote a new line to the file!")

    # Read and display the file contents
    if st.button("Read File"):
        file_handler.seek(0)  # Move to the beginning of the file
        content = file_handler.read()
        st.text(content)

    # Always make sure to close the file when done (useful for resource cleanup)
    file_closed = st.button("Close File", on_click=file_handler.close)
else:
    st.write("## Error: Neither section variable in the code is set to True.")