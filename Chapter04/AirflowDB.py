# This Python code is designed to work with the Apache Airflow framework, a platform for programmatically authoring, scheduling, and monitoring workflows.
The code defines a Directed Acyclic Graph (DAG) called MyDBdag that retrieves data from a PostgreSQL database and inserts it into Elasticsearch.
The DAG consists of two tasks:

# QueryPostgreSQL: A PythonOperator task that calls the queryPostgresql function, which queries data from a PostgreSQL database and saves it to a CSV
file named 'postgresqldata.csv'.
# InsertDataElasticsearch: A PythonOperator task that calls the insertElasticsearch function, which reads data from the 'postgresqldata.csv' file and
inserts it into an Elasticsearch index named "frompostgresql".
# The DAG is configured with default arguments, such as owner, start date, number of retries, and retry delay. The schedule interval is set to run every 5 minutes.
# This Python code is designed to work with the Apache Airflow framework, a platform for programmatically authoring, scheduling, and monitoring workflows. 

# Import necessary libraries

import datetime as dt
from datetime import timedelta

# Import Apache Airflow libraries
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Import Pandas for data manipulation
import pandas as pd

# Import libraries for database operations
import psycopg2 as db
from elasticsearch import Elasticsearch

# Define the function to query data from a PostgreSQL database
def queryPostgresql():
    # Define connection string for PostgreSQL database
    conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
    
    # Connect to the PostgreSQL database
    conn = db.connect(conn_string)
    
    # Read data from the 'users' table and save it to a DataFrame
    df = pd.read_sql("select name, city from users", conn)
    
    # Write the DataFrame to a CSV file
    df.to_csv('postgresqldata.csv')
    
    # Print a message to indicate that data has been saved
    print("-------Data Saved------")

# Define the function to insert data into Elasticsearch
def insertElasticsearch():
    # Create an Elasticsearch client
    es = Elasticsearch()
    
    # Read data from the CSV file into a DataFrame
    df = pd.read_csv('postgresqldata.csv')
    
    # Iterate through each row in the DataFrame and insert it into Elasticsearch
    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="frompostgresql", doc_type="doc", body=doc)
        print(res)

# Set default arguments for the DAG
default_args = {
    'owner': 'paulcrickard',
    'start_date': dt.datetime(2020, 4, 2),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# Define the DAG with the specified configuration
with DAG('MyDBdag',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         ) as dag:

    # Create a PythonOperator to call the 'queryPostgresql' function
    getData = PythonOperator(task_id='QueryPostgreSQL',
                             python_callable=queryPostgresql)
    
    # Create a PythonOperator to call the 'insertElasticsearch' function
    insertData = PythonOperator(task_id='InsertDataElasticsearch',
                                python_callable=insertElasticsearch)

# Define the order in which the tasks should be executed
getData >> insertData
