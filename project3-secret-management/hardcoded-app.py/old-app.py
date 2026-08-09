import mysql.connector

DB_HOST = "your-database-host"
DB_USER = "admin"
DB_PASSWORD = "MyPassword123"
DB_NAME = "applicationdb"

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

print("Database connection successful!")
