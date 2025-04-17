import streamlit as st

# The only way to change how the sidebar label appears
# is to change the actual file name, but we can change
# how the title appears in the browser tab (at the top)
st.set_page_config(page_title="New Page")

# The line above has to come before anything else in the code 
st.title("Page 1")

# Notice that in the text input below,
# the state (and therefore input content)
# will be destroyed anytime we switch to
# another page and come back. To handle this
# differently, we would need to use 'session_state'
st.text_input("Name")
