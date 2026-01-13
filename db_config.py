import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=int(os.environ["DB_PORT"])
    )
    if connection.is_connected():
        print("✅ Successfully connected to Railway MySQL!")
except Error as e:
    print(f"❌ Database Error: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

