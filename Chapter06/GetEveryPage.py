# Import necessary libraries
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

    # Define the process method which takes an input and output stream
    def process(self, inputStream, outputStream):
        try:
            # Read the input stream and convert it to a string
            text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            # Convert the string to a JSON object
            asjson = json.loads(text)

            # Check if the current page is less than or equal to the total pages
            if asjson['metadata']['pagination']['page'] <= asjson['metadata']['pagination']['pages']:
                # Get the next page URL
                url = asjson['metadata']['pagination']['next_page_url']
                # Request the next page and read the response
                rawreply = urllib2.urlopen(url).read()
                # Load the response as a JSON object
                reply = json.loads(rawreply)
                # Write the JSON object to the output stream
                outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
            else:
                # If the condition is not met, set the errorOccurred flag to True
                global errorOccurred
                errorOccurred = True

                # Write the original JSON object to the output stream
                outputStream.write(bytearray(json.dumps(asjson, indent=4).encode('utf-8')))

        except:
            # If an exception occurs, set the errorOccurred flag to True
            global errorOccurred
            errorOccurred = True

            # Write the original JSON object to the output stream
            outputStream.write(bytearray(json.dumps(asjson, indent=4).encode('utf-8')))

# Set the errorOccurred flag to False
errorOccurred = False
# Get the flow file from the session
flowFile = session.get()

if flowFile is not None:
    # Write the processed data to the flow file
    flowFile = session.write(flowFile, ModJSON())

    # Check if an error occurred during the process
    if errorOccurred:
        # If yes, transfer the flow file to the failure relationship
        session.transfer(flowFile, REL_FAILURE)
    else:
        # Otherwise, transfer the flow file to the success relationship
        session.transfer(flowFile, REL_SUCCESS)

# Commit the session
session.commit()
