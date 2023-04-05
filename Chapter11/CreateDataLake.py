from faker import Faker
import json
import os
# This Python script generates 1000 JSON files containing randomly generated user data using the Faker library.
# The generated data includes user ID, name, age, street, city, state, and zip code. The script writes each JSON object to a separate file, 
# with the filename derived from the user's name, and stores the files in the specified directory.

# Change the current working directory to the specified path
os.chdir("/home/paulcrickard/datalake")

fake = Faker()
userid = 1

# Loop through 1000 iterations
for i in range(1000):
    # Generate a fake name
    name = fake.name()
    
    # Replace spaces with hyphens in the name and add .json extension to create the filename
    fname = name.replace(" ", "-") + ".json"
    
    # Create a dictionary containing the randomly generated user data
    data = {
        "userid": userid,
        "name": name,
        "age": fake.random_int(min=18, max=101, step=1),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip": fake.zipcode(),
    }
    
    # Convert the dictionary to a JSON string
    datajson = json.dumps(data)

    # Open the file in write mode, increment the user ID, write the JSON string, and close the file
    output = open(fname, "w")
    userid += 1
    output.write(datajson)
    output.close()
