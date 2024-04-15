# DETAILED DECK SUBMISSION
## SELECTED: PROBLEM STATEMENT 1
### Transforming Early Talent Engagement and Hiring through Advanced Analytics and AI
### OBJECTIVE:
The goal is to invent a disruptive talent engagement and hiring experience powered by advanced data analytics and AI. The solution should be able to analyze large amounts of data quickly and accurately, provide insightful recommendations to both job seekers and employers, and ultimately enhance the efficiency and effectiveness of the talent engagement and hiring process on Unstop. The solution should also be scalable and adaptable to the changing dynamics of the job market.

### SOLUTION
Use of LLM instances to analyze data along with the database and match the best candidates according to the requirements of Hiring Organization.
- Video demo: [YouTube](https://youtu.be/fUb6gH7m3So)
- Detailed description in solution.pdf

### CODE
- **utp-app**: contains the frontend using pyhton and stremlit.
  - Run using `streamlit run app.py`.
- **utp-docker**: contains the docker file for creating image.
  - Create image using `docker build . -t utp-serve`.
