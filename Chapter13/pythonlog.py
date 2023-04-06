# Purpose:
# The script demonstrates how to set up and use the logging module in Python. 
# It shows two different configurations, one without a timestamp and one with a timestamp. 
# The script logs various messages with different logging levels, such as debug, warning, error, and info.
import logging

# Set up the basic logging configuration with level, filename, filemode, and format
logging.basicConfig(level=0, filename='python-log.log', filemode='w', format='%(levelname)s - %(message)s')

# Log a debug message
logging.debug('Attempted to divide by zero')
# Log a warning message
logging.warning('User left field blank in the form')
# Log an error message
logging.error("Couldn't find specified file")

# Reconfigure the logging setup to include a timestamp in the log format
logging.basicConfig(level=0, filename='python-log.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# Log two info messages with the new configuration
logging.info('Something happened')
logging.info('Something else happened, and it was bad')
