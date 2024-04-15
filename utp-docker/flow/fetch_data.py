from promptflow.core import tool
import psycopg2
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
def fetch_query(query):
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="utp",
        user="citus",
        password="tduiG@1234",
        host="c-utp-can-db.b5kyj327to67bg.postgres.cosmos.azure.com",
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
