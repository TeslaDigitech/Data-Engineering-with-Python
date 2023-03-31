# Import the Elasticsearch library
from elasticsearch import Elasticsearch

# Create an Elasticsearch client, connecting to the default address (localhost) and port (9200)
es = Elasticsearch()

# Define a query to retrieve all documents
doc = {"query": {"match_all": {}}}
# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents

res = es.search(index="users", body=doc, size=10)

# Print the source of the 10th document in the search results
print(res['hits']['hits'][9]['_source'])

# Define a query to retrieve documents with the name 'Ronald Goodman'
doc = {"query": {"match": {"name": "Ronald Goodman"}}}

# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents
res = es.search(index="users", body=doc, size=10)

# Print the source of the first document in the search results
print(res['hits']['hits'][0]['_source'])

# Execute a search query using Lucene syntax to find documents with the name 'Ronald Goodman'
res = es.search(index="users", q="name:Ronald Goodman", size=10)

# Print the source of the first document in the search results
print(res['hits']['hits'][0]['_source'])

# Define a query to retrieve documents with the city 'Jamesberg'
doc = {"query": {"match": {"city": "Jamesberg"}}}

# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents
res = es.search(index="users", body=doc, size=10)

# Print all the documents in the search results
print(res['hits']['hits'])

# Define a query to retrieve documents with the city 'Jamesberg' and filter by the zip code '63792'

doc = {"query": {"bool": {"must": {"match": {"city": "Jamesberg"}}, "filter": {"term": {"zip": "63792"}}}}}
# Execute the search query on the 'users' index with the specified query, limiting the results to 10 documents

res = es.search(index="users", body=doc, size=10)
# Print all the documents in the search results
print(res['hits']['hits'])
