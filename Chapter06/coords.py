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
            # Read the input stream and convert it to a string
            text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            # Parse the string to a JSON object
            reply = json.loads(text)
            
            # Modify the JSON object by adding 'coords' and 'opendate' fields
            reply['coords'] = str(reply['lat']) + "," + str(reply['lng'])
            d = reply['created_at'].split("T")
            reply['opendate'] = d[0]
            
            # Write the modified JSON object to the output stream
            outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
        except:
            global errorOccurred
            errorOccurred = True
            # Write the original JSON object to the output stream if an exception occurs
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
