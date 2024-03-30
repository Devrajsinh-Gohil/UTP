# SELECTED: PROBLEM STATEMENT 1
### Transforming Early Talent Engagement and Hiring through Advanced Analytics and AI
### OBJECTIVE:
The goal is to invent a disruptive talent engagement and hiring experience powered by advanced data analytics and AI. The solution should be able to analyze large amounts of data quickly and accurately, provide insightful recommendations to both job seekers and employers, and ultimately enhance the efficiency and effectiveness of the talent engagement and hiring process on Unstop. The solution should also be scalable and adaptable to the changing dynamics of the job market.

# SOLUTION

### CONCEPT
![Blank diagram](https://github.com/Devrajsinh-Gohil/UTP/assets/103804567/6f510d23-4781-4510-a0f1-bf678fafa84d)

- **EXTRACT**: By interfacing with Database, it’s schema is extracted and forwarded to LLM. The interfacing can be done Python, C++, Java etc.
- **ANALYZE**: The input schema is then analyzed by LLM to understand the structure of data in database.
- **GENERATE**: After analyzing the data LLM is then provided a  request in Natural Language which has the requirements of Hiring Organization. The LLM Generates the Query according to the request and structure of database.
- **FETCH**: The Query is then fired to database via database interface and the result is received from the database.
- **FILTER**: The result is then given to LLM for better filtering and matching the most suitable candidates according to the requirement of Organization.
- **FORMAT**: After filtering LLM will format the data according to the file format as per the requirement of the platform.

# PROOF OF CONCEPT
<img width="403" alt="Graph" src="https://github.com/Devrajsinh-Gohil/UTP/assets/103804567/61092f20-7084-46e3-9b66-637243534a9c">

- **TECH STACK**: Azure OpenAI (gpt-35-turbo) for LLM, AzureMachine Learning for using Prompt Flow service and Deployment,Python for interacting with API and Streamlit package to run the User Interface.
- **INPUT**: User requirement in Natural Language.
- **DATA** (PYTHON): Due to resource and storage constraints, a dummy dataset in form of python dictionary is used.
- **GET CANDIDATES** (LLM): filters candidate according to the user input and formats JSON output.
- **GET JSON** (LLM): The output of GET CANDIDATES is then corrected if anomalies are present and the output assures output is syntactically correct.
- **OUTPUT**: The output contains the JSON format containing the data of candidates according to the request and sent to User Interface via API deployed.

## Video
https://github.com/Devrajsinh-Gohil/UTP/assets/103804567/7cac2921-e867-4bdb-85e2-7845c621a00f


## DEPLOYMENT
Deployed using: [Streamlit App](https://utp-pstmt1-poc.streamlit.app/)
