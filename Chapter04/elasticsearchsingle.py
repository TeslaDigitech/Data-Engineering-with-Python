# This Python code uses the Elasticsearch library to index a document with randomly generated data into an Elasticsearch index called 'users' and then performs a search query to retrieve a document with a specific '_id'. The code follows these steps:

# Import the Elasticsearch library and helpers module
# Import the Faker library for generating fake data
# Create a Faker instance
# Create an Elasticsearch client
# Generate a document with random data using the Faker instance
# Index the generated document into the 'users' index with the document type 'doc'
# Print the response from the indexing operation
# Define a query to retrieve a document with a specific '_id'
# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents
# Print the search results

# Import the Elasticsearch library
from elasticsearch import Elasticsearch
# Import the helpers module from the Elasticsearch library
from elasticsearch import helpers
# Import the Faker library for generating fake data
from faker import Faker

# Create a Faker instance
fake = Faker()

# Create an Elasticsearch client, connecting to the default address (localhost) and port (9200)
es = Elasticsearch()

# Generate a document with random data using the Faker instance
doc = {
    "name": fake.name(),
    "street": fake.street_address(),
    "city": fake.city(),
    "zip": fake.zipcode()
}

# Index the generated document into the 'users' index with the document type 'doc'
res = es.index(index="users", doc_type="doc", body=doc)
# Print the response from the indexing operation
print(res)

# Define a query to retrieve a document with a specific '_id'
doc = {"query": {"match": {"_id": "pDYlOHEBxMEH3Xr-2QPk"}}}
# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents

res = es.search(index="users", body=doc, size=10)
# Print the search results
print(res)

