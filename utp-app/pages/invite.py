import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Display header with a blue divider
st.header("Invitations", divider='blue')

# Display a message for the candidates you are inviting
st.write('Candidates you are inviting:')

# Read the invited candidates data from a CSV file
df = pd.read_csv('invited.csv')

# Display the data in a dataframe
st.dataframe(df, hide_index=True)

# Add a link to edit invitations
st.page_link("pages/result.py", label="edit invitations?")

# Check if the "Send Invites" button is clicked
if st.button('Send Invites 📬'):
    # Display a warning message with the number of candidates invited and their IDs
    st.warning(f"Invitations sent to {len(df)} candidates: {df['ID'].to_list()}! 🎉")

# Add a link to search for other roles in the app
st.page_link("app.py", label="Search for other roles", icon="🔍")