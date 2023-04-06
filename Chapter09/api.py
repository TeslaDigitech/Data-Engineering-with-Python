# Purpose:
# The script retrieves information from an Apache NiFi instance using its REST API.
# It fetches data about system diagnostics, processor groups, processors, flowfile queues, bulletins, and counters.import requests


#System Diagnostics
# Retrieve system diagnostics
r=requests.get('http://localhost:9300/nifi-api/system-diagnostics')
data=r.json()
print(data)

# Access specific data from the system diagnostics
data['systemDiagnostics']['aggregateSnapshot']['maxHeap']
#'512 MB'
data['systemDiagnostics']['aggregateSnapshot']['totalThreads']
#108
data['systemDiagnostics']['aggregateSnapshot']['heapUtilization']
#'81.0%'

# Processor Group
# Retrieve information about a processor group
pg=requests.get('http://localhost:9300/nifi-api/process-groups/9466c3ca-4c6d-3884-ac72-af4a27919fb0')
pgdata=pg.json()
pgdata['component']['name']
#'SCF'
pgdata['status']


# A single processor
# Retrieve information about a single processor
p=requests.get('http://localhost:9300/nifi-api/processors/8b63e4d0-eff2-3093-f4ad-0f1581e56674')
pdata=p.json()
pdata['component']['name']
#'Query SCF - Archive'
pdata['status']

# Retrieve queue data

q=requests.post('http://localhost:9300/nifi-api/flowfile-queues/295fc119-0172-1000-3949-54311cdb478e/listing-requests')
qdata=q.json()
listid=qdata['listingRequest']['id']  # '0172100b-179f-195f-b95c-63ea96d151a3'
url="http://localhost:9300/nifi-api/flowfile-queues/295fc119-0172-1000-3949-54311cdb478e/listing-requests/"+listid
ff=requests.get(url)
ffdata=ff.json()
ffid=ffdata['listingRequest']['flowFileSummaries'][0]['uuid']
#'3b2dd0fa-dfbe-458b-83e9-ea5f9dbb578f'
ffurl="http://localhost:9300/nifi-api/flowfile-queues/295fc119-0172-1000-3949-54311cdb478e/flowfiles/"+ffid+"/content"
download=requests.get(ffurl)
download.json()

# Empty Queue
e=requests.post('http://localhost:9300/nifi-api/flowfile-queues/295fc119-0172-1000-3949-54311cdb478e/drop-requests')
edata=e.json()

# Read bulletin board data
b=requests.get('http://localhost:9300/nifi-api/flow/bulletin-board')
bdata=b.json()
bdata


# Retrieve counters data
b=requests.get('http://localhost:9300/nifi-api/flow/bulletin-board')
bdata=b.json()
bdata





