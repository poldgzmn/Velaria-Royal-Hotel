import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="hotel_db",
            port=3306
        )
        if connection.is_connected():
            print("✅ Connected to MySQL successfully!")
            return connection
    except Error as e:
        print(f"❌ Database Error: {e}")
        return None
