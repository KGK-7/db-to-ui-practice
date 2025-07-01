import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="9786",  
    host="localhost",
    port="5432"
)

cur = conn.cursor(cursor_factory=DictCursor)
cur.execute("SELECT * FROM users;")

data = [dict(row) for row in cur.fetchall()]
print(data)

cur.close()
conn.close()

# This code connects to a PostgreSQL database, retrieves all rows from the "users" table,
# and converts each row into a dictionary. The dictionaries are stored in a list called `data
#`. The `DictCursor` from `psycopg2.extras` allows fetching rows as dictionaries.
# Make sure to replace the connection parameters with your actual database credentials.
# Also, ensure that the "users" table exists in your database.
# Note: The `DictCursor` is used to fetch rows as dictionaries, which allows accessing columns by name.
# This is useful for converting SQL query results into a more Pythonic format.
# The final output will be a list of dictionaries, where each dictionary represents a row from the "users" table.
# This approach is particularly useful when you want to work with SQL data in a more structured way,
# such as when passing data to APIs or processing it in Python applications.
# The `data` variable will contain the SQL data in a dictionary format, making it easy to manipulate or use in your application.
# This code is useful for applications that need to interact with a PostgreSQL database and require