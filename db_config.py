import os
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT"))  
        )

        if connection.is_connected():
            print("✅ Connected to MySQL successfully!")
            return connection

    except Error as e:
        print(f"❌ Database Error: {e}")
        return None
