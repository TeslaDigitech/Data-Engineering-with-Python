# Import the Elasticsearch library
from elasticsearch import Elasticsearch

# Create an Elasticsearch instance
es = Elasticsearch()

# Execute a search query on the Elasticsearch instance to fetch the first batch of documents
res = es.search(
    index='users',
    doc_type='doc',
    scroll='20m',  # Keep the search context alive for 20 minutes
    size=500,  # Fetch 500 documents per batch
    body={"query": {"match_all": {}}}
)

# Print the '_source' field of the fetched documents
for search_doc in res['hits']['hits']:
    print(search_doc['_source'])

# Store the scroll ID and the total number of documents found
sid = res['_scroll_id']
size = res['hits']['total']['value']

# Start scrolling through the remaining documents
while (size > 0):
    print(size)
    print("--------------------------------------------")

    # Fetch the next batch of documents using the scroll ID
    res = es.scroll(scroll_id=sid, scroll='20m')

    # Update the scroll ID and the number of documents in the current batch
    sid = res['_scroll_id']
    size = len(res['hits']['hits'])

    # Print the '_source' field of the fetched documents in the current batch
    for doc in res['hits']['hits']:
        print(doc['_source'])
