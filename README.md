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

