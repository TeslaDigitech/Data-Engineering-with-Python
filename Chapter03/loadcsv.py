# This Python code generates a CSV file named 'data.csv' with 1000 rows of fake data using the Faker library. The fake data includes information such as name, age, street address, city, state, zip code, longitude, and latitude. The code follows these steps:

# Import necessary libraries (Faker and CSV)
# Open 'data.csv' in write mode
# Create an instance of the Faker class
# Define the header for the CSV file
# Create a CSV writer object to write data to the output file
# Write the header row to the output file
# Generate and write 1000 rows of fake data to the output file using a for loop
# Close the output file
# Here is the logical execution order in a table format:

# Order	Method/Statement	Description
# 1	from faker import Faker	Import the Faker library
# 2	import csv	Import the CSV library
# 3	output = open('data.csv', 'w')	Open 'data.csv' in write mode
# 4	fake = Faker()	


from faker import Faker
import csv
output=open('data.csv','w')
fake=Faker()
header=['name','age','street','city','state','zip','lng','lat']
mywriter=csv.writer(output)
mywriter.writerow(header)
for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18, max=80, step=1), fake.street_address(), fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
output.close()
