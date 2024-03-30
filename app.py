import urllib.request
import json
import os
import ssl
import pandas as pd
import streamlit as st

# get env vars
API_URL = st.secrets['API']
API_KEY = st.secrets['KEY']
API = st.secrets['ENDPOINT']

# This is needed to allow self-signed certificates
def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
with st.form(key='my_form_to_submit'):
    st.text_input("Write your request here:", key="req")
    submit_button = st.form_submit_button(label='Submit')
    
data = st.session_state.req

body = str.encode(data)

url = API_URL
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = API_KEY
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': API }

req = urllib.request.Request(url, body, headers)

if submit_button:
    try:
        # Azure endpoint response
        response = urllib.request.urlopen(req)
        result = response.read()
        data = json.loads(result.decode())
    
        # Extract the 'response' value and load it as another JSON
        response_data = json.loads(data['response'])
        df = pd.DataFrame(response_data)
    
        # Streamlit
        st.write("Here's are some matches:")
        st.write(df)
        
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))