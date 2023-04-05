# Purpose:
# This Python script is used for validating the data in a CSV file using the Great Expectations library. 
# It configures a DataContext with a provided Great Expectations configuration, gets an expectation suite, 
# and sets up batch_kwargs for reading the CSV file. The script then gets a batch to validate, runs the validation operator on the batch, 
# and checks the success status of the validation results. Finally, the script prints the appropriate JSON response (pass or fail) based on the success status.

import sys
from great_expectations import DataContext

# Initialize the DataContext with the provided Great Expectations configuration
context = DataContext("/home/paulcrickard/peoplepipeline/great_expectations")

# Get the expectation suite with the name "people.validate"
suite = context.get_expectation_suite("people.validate")

# Configure batch_kwargs with the path to the CSV file, datasource, and reader method
batch_kwargs = {
    "path": "/home/paulcrickard/peoplepipeline/people.csv",
    "datasource": "files_datasource",
    "reader_method": "read_csv",
}

# Get the batch to validate based on the batch_kwargs and expectation suite
batch = context.get_batch(batch_kwargs, suite)

# Run the validation operator on the batch and store the results
results = context.run_validation_operator("action_list_operator", [batch])

# Check the success status of the validation results and print the appropriate JSON response
if not results["success"]:
    print('{"result":"fail"}')
    sys.exit(0)

print('{"result":"pass"}')
sys.exit(0)
