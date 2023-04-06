# Import required libraries
import urllib
import urllib2
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

# Define a custom class ModJSON that inherits from StreamCallback
class ModJSON(StreamCallback):
  def __init__(self):
        pass

  # Define the process method for the ModJSON class
  def process(self, inputStream, outputStream):
    try:
        # Set parameters for the API request
        param = {'place_url': 'bernalillo-county', 'per_page': '100', 'status': 'Archived'}
        # Create the API URL
        url = 'https://seeclickfix.com/api/v2/issues?' + urllib.urlencode(param)
        # Fetch data from the API
        rawreply = urllib2.urlopen(url).read()
        # Parse the JSON response
        reply = json.loads(rawreply)

        # Write the JSON data to the outputStream
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
    except:
        # If an exception occurs, set errorOccurred to True
        global errorOccurred
        errorOccurred = True
        
        # Write the JSON data to the outputStream
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
        
# Initialize errorOccurred as False
errorOccurred = False
# Get the current flowFile from the NiFi session
flowFile = session.get()
if (flowFile != None):
  # Write the flowFile using the ModJSON class
  flowFile = session.write(flowFile, ModJSON())

  # If an error occurred during processing, transfer the flowFile to the REL_FAILURE relationship
  if(errorOccurred):
    session.transfer(flowFile, REL_FAILURE)
  else:
    # If no error occurred, transfer the flowFile to the REL_SUCCESS relationship
    session.transfer(flowFile, REL_SUCCESS)
  
# Commit the NiFi session
session.commit()
