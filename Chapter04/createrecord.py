# Import the psycopg2 library for working with PostgreSQL databases
import psycopg2 as db

# Define the connection string for the PostgreSQL database
conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

# Connect to the PostgreSQL database
conn = db.connect(conn_string)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Define an SQL query string to insert data into the 'users' table using Python string formatting
query = "insert into users (id, name, street, city, zip) values({}, '{}', '{}', '{}', '{}')".format(1, 'Big Bird', 'Sesame Street', 'Fakeville', '12345')

# Print the SQL query string after the formatting is applied
print(cur.mogrify(query))

# Define an SQL query string with placeholders for the values to be inserted
query2 = "insert into users (id, name, street, city, zip) values(%s, %s, %s, %s, %s)"

# Define a tuple containing the data to be inserted
data = (1, 'Big Bird', 'Sesame Street', 'Fakeville', '12345')

# Print the SQL query string with the data provided
print(cur.mogrify(query2, data))

# Execute the SQL query to insert the data into the 'users' table
cur.execute(query2, data)

# Commit the transaction to the database
conn.commit()



