import pandas as pd
import streamlit as st
import requests

# Create a form to input the request
with st.form(key='my_form_to_submit'):
    st.text_input("Write your request here:", key="req")
    submit_button = st.form_submit_button(label='Submit')

# Get the request data from the form
data = st.session_state.req

# Check if the submit button is clicked
if submit_button:
    try:
        # Define the URL of the API
        url = "http://localhost:55000/score"

        # Define the data to be sent in the request
        request = {
            "request": data
        }

        # Send the POST request to the API
        response = requests.post(url, json=request)

        # Check if the request was successful (status code 200)
        if response.status_code == 400:
            st.toast('Please provide more specifics', icon="😅")
        elif response.status_code == 200:
            # Extract the 'response' value and load it as another JSON
            response_data = response.json()
            json_data = response_data['response']

            # Convert the 'response' list to a Pandas DataFrame
            df = pd.DataFrame(json_data, columns=['ID', 'Student', 'Education', 'UndergradMajor', 'DeveloperType', 'YearsCoding', 'LanguageWorkedWith', 'FrameworkWorkedWith', 'Gender'])
            df['DeveloperType'] = df['DeveloperType'].str.replace(';', ',')
            df['LanguageWorkedWith'] = df['LanguageWorkedWith'].str.replace(';', ',')
            df['FrameworkWorkedWith'] = df['FrameworkWorkedWith'].str.replace(';', ',')
            df['Invite'] = False
            df.to_csv('out.csv', index=False)
            st.page_link("pages/result.py", label="Matches found! Click here to view", icon="➡️")

        else:
            st.toast('Some error occurred', icon="🔴")
    except:
        st.toast('Trying to connect, try again in sometime.', icon="😇")