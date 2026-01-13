import os
import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host=os.environ["MYSQLHOST"],
        port=os.environ["MYSQLPORT"],
        user=os.environ["MYSQLUSER"],
        password=os.environ["MYSQLPASSWORD"],
        database=os.environ["MYSQLDATABASE"]
    )
