from promptflow.core import tool
import psycopg2
import os
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
def fetch_query(query):
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user="citus",
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port=5432,
        sslmode="require"
    )
    cur = conn.cursor()

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

@tool
def my_python_tool(query:str) -> str:
    print ("Query: ", query)
    return fetch_query(query)
