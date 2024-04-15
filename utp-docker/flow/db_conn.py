from promptflow.core import tool
import psycopg2
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

def get_table_rows():
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

    # Query to get detailed table structure
    query = """
        SELECT * from developer_data LIMIT 5;
    """
    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def get_table_structure(table_name):
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

    # Query to get detailed table structure
    query = """
        SELECT 
            c.column_name,
            c.data_type,
            c.character_maximum_length,
            CASE 
                WHEN pk.constraint_name IS NOT NULL THEN 'PRIMARY KEY'
                ELSE ''
            END AS constraint_type,
            CASE 
                WHEN fk.constraint_name IS NOT NULL THEN 'FOREIGN KEY'
                ELSE ''
            END AS foreign_key,
            CASE 
                WHEN i.index_name IS NOT NULL THEN 'INDEX'
                ELSE ''
            END AS index_type
        FROM 
            information_schema.columns c
            LEFT JOIN (
                SELECT 
                    kcu.column_name,
                    tc.constraint_name
                FROM 
                    information_schema.key_column_usage kcu
                    JOIN information_schema.table_constraints tc 
                    ON kcu.constraint_name = tc.constraint_name
                    AND kcu.table_schema = tc.table_schema
                    AND kcu.table_name = tc.table_name
                WHERE 
                    tc.constraint_type = 'PRIMARY KEY'
                    AND tc.table_name = %s
            ) pk ON c.column_name = pk.column_name
            LEFT JOIN (
                SELECT 
                    kcu.column_name,
                    tc.constraint_name
                FROM 
                    information_schema.key_column_usage kcu
                    JOIN information_schema.table_constraints tc 
                    ON kcu.constraint_name = tc.constraint_name
                    AND kcu.table_schema = tc.table_schema
                    AND kcu.table_name = tc.table_name
                WHERE 
                    tc.constraint_type = 'FOREIGN KEY'
                    AND tc.table_name = %s
            ) fk ON c.column_name = fk.column_name
            LEFT JOIN (
                SELECT 
                    indexname as index_name
                FROM 
                    pg_indexes
                WHERE 
                    tablename = %s
            ) i ON c.column_name = i.index_name
        WHERE 
            c.table_name = %s;
    """
    cur.execute(query, (table_name, table_name, table_name, table_name))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

@tool
def my_python_tool() -> str:
    tables = ['developer_data']
    db_schema = {}
    db_schema['developer_data'] = get_table_structure('developer_data')
    db_schema['developer_data_rows'] = get_table_rows()
    return db_schema
