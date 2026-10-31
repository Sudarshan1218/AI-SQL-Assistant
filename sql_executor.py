
import sqlite3
import pandas as pd
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "students.db")




def execute_query(query):
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("PRAGMA query_only = ON")

        cleaned_query = query.strip()

        # Remove one optional trailing semicolon
        cleaned_query = cleaned_query.rstrip(";").strip()

        # Allow only SELECT statements
        if not re.match(r"^SELECT\b", cleaned_query, re.IGNORECASE):
            raise ValueError("Only SELECT queries are allowed!")

        # Reject multiple SQL statements
        if ";" in cleaned_query:
            raise ValueError("Multiple SQL statements are not allowed!")

        result = pd.read_sql_query(cleaned_query, connection)
        return result

    finally:
        connection.close()


def get_table_data():

    query = "SELECT * FROM students"

    return execute_query(query)
