# This Python code is designed to work with the Apache Airflow framework, a platform for programmatically authoring, scheduling, and monitoring workflows. The code defines a Directed Acyclic Graph (DAG) called MyCSVDAG that reads a CSV file, prints the 'name' column values, and converts the CSV file to a JSON file. The DAG consists of two tasks:

# print_starting: A BashOperator task that prints a message when the DAG starts.
# csvJson: A PythonOperator task that calls the csvToJson function, which reads the CSV file and converts it to a JSON file.
# The DAG is configured with default arguments, such as owner, start date, number of retries, and retry delay. The schedule interval is set to run every 5 minutes.
# Import necessary libraries
import datetime as dt
from datetime import timedelta

# Import Apache Airflow libraries
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Import Pandas for data manipulation
import pandas as pd

# Define the function to read a CSV file and convert it to JSON
def csvToJson():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('/home/paulcrickard/data.csv')
    
    # Iterate through each row in the DataFrame and print the 'name' column value
    for i, r in df.iterrows():
        print(r['name'])
    
    # Convert the DataFrame to a JSON file with the specified format
    df.to_json('fromAirflow.json', orient='records')

# Set default arguments for the DAG
default_args = {
    'owner': 'paulcrickard',
    'start_date': dt.datetime(2020, 3, 18),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# Define the DAG with the specified configuration
with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),      # '0 * * * *',
         ) as dag:

    # Create a BashOperator to print a message when the DAG starts
    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')
    
    # Create a PythonOperator to call the 'csvToJson' function
    csvJson = PythonOperator(task_id='convertCSVtoJson',
                             python_callable=csvToJson)

# Define the order in which the tasks should be executed
print_starting >> csvJson
