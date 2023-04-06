# Purpose:
# The script is designed to be used in an Apache NiFi ExecuteScript processor.
# It makes an API call to the SeeClickFix API to retrieve issues related to Bernalillo County. 
# The JSON response is then written to a flowFile. If any error occurs during the process, it transfers the flowFile to the 
# 'REL_FAILURE' relationship, otherwise to the 'REL_SUCCESS' relationship.

import urllib
import urllib2
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

# Define the ModJSON class that implements the StreamCallback interface
class ModJSON(StreamCallback):
    def __init__(self):
        pass

    # Define the process method that takes inputStream and outputStream as arguments
    def process(self, inputStream, outputStream):
        try:
            # Prepare request parameters for the API call
            param = {'place_url': 'bernalillo-county', 'per_page': '100'}
            # Create the API URL using the request parameters
            url = 'https://seeclickfix.com/api/v2/issues?' + urllib.urlencode(param)
            # Send the API request and read the response
            rawreply = urllib2.urlopen(url).read()
            # Parse the response as a JSON object
            reply = json.loads(rawreply)

            # Write the JSON object to the output stream
            outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
        except:
            global errorOccurred
            errorOccurred = True

            # Write the JSON object to the output stream if an exception occurs
            outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))

errorOccurred = False
flowFile = session.get()

# Check if the flowFile is not None
if (flowFile != None):
    # Write the flowFile using the ModJSON class
    flowFile = session.write(flowFile, ModJSON())

    # Check if an error occurred during processing
    if(errorOccurred):
        # Transfer the flowFile to the REL_FAILURE relationship
        session.transfer(flowFile, REL_FAILURE)
    else:
        # Transfer the flowFile to the REL_SUCCESS relationship
        session.transfer(flowFile, REL_SUCCESS)

# Commit the NiFi session
session.commit()
