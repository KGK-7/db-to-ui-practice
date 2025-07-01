import psycopg2

conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="9786",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()


# This code connects to a PostgreSQL database, retrieves all rows from the "users" table, and prints each row.
# It uses the psycopg2 library to handle the database connection and query execution.
# Note: Make sure to replace the connection parameters with your actual database credentials.
# Also, ensure that the "users" table exists in your database.
