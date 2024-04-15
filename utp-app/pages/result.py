import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Display header with a blue divider
st.header("Prospective Candidates", divider='blue')

# Read data from 'out.csv' file
df = pd.read_csv('out.csv')

# Display a message
st.write("Here are some matches: (*You add candidates to invite by checking the box in the __'Invite'__ column*)")

# Allow editing of the data using the data editor
df = st.data_editor(df, hide_index=True, disabled=['ID', 'Student', 'Education', 'UndergradMajor', 'DeveloperType', 'YearsCoding', 'LanguageWorkedWith', 'FrameworkWorkedWith', 'Gender'])

# Check if the "Add Invitees" button is clicked
if st.button("Add Invitees ➕"):
    # Filter the data to get the invited candidates
    df.to_csv('out.csv', index=False)
    invited_df = df[df['Invite']]
    invited_df.to_csv('invited.csv', index=False)
    st.warning('Candidates added to the invite list. ✅')
    # Add a link to the "invite.py" page
    st.page_link("pages/invite.py", label="Send Invitations", icon="✉️")

# Add a link to the "app.py" page
st.page_link("app.py", label="Search again", icon="🔍")
