# This Python code uses the psycopg2 library to interact with a PostgreSQL database and the Faker library to generate fake data. The code follows these steps:

# Import the psycopg2 library for PostgreSQL interaction
# Import the Faker library for generating fake data
# Create a Faker instance
# Initialize an empty list to store generated data and a counter variable
# Generate 1000 records of fake data and store them in the 'data' list
# Convert the data list into a tuple
# Print the data tuple
# Define the connection string for the PostgreSQL database
# Connect to the PostgreSQL database
# Create a cursor object for database operations
# Define the SQL query to insert data into the 'users' table
# Print the SQL query with the first record from the data tuple
# Execute the SQL query for all the records in the data tuple
# Commit the transaction to the database
# Define another SQL query to fetch all records from the 'users' table
# Execute the SQL query to fetch all records
# Print the fetched records

# Import the psycopg2 library for PostgreSQL interaction
import psycopg2 as db
# Import the Faker library for generating fake data
from faker import Faker

# Create a Faker instance
fake = Faker()

# Initialize an empty list to store generated data
data = []
i = 2  # Initialize a counter variable

# Generate 1000 records of fake data and store them in the 'data' list
for r in range(1000):
    data.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))
    i += 1

# Convert the data list into a tuple
data_for_db = tuple(data)
# Print the data tuple
print(data_for_db)

# Define the connection string for the PostgreSQL database
conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
# Connect to the PostgreSQL database
conn = db.connect(conn_string)

# Create a cursor object for database operations
cur = conn.cursor()

# Define the SQL query to insert data into the 'users' table
query = "insert into users (id, name, street, city, zip) values(%s, %s, %s, %s, %s)"

# Print the SQL query with the first record from the data tuple
print(cur.mogrify(query, data_for_db[1]))

# Execute the SQL query for all the records in the data tuple
cur.executemany(query, data_for_db)
# Commit the transaction to the database
conn.commit()

# Define another SQL query to fetch all records from the 'users' table
query2 = "select * from users"

# Execute the SQL query to fetch all records
cur.execute(query2)
# Print the fetched records
print(cur.fetchall())
