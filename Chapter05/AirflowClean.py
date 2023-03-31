# Import necessary libraries
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

# Define the cleanScooter function
def cleanScooter():
    # Read scooter.csv into a DataFrame
    df = pd.read_csv('scooter.csv')
    # Drop the 'region_id' column
    df.drop(columns=['region_id'], inplace=True)
    # Set column names to lowercase
    df.columns = [x.lower() for x in df.columns]
    # Convert the 'started_at' column to a datetime object
    df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('cleanscooter.csv')

# Define the filterData function
def filterData():
    # Read cleanscooter.csv into a DataFrame
    df = pd.read_csv('cleanscooter.csv')
    # Define the date range to filter on
    fromd = '2019-05-23'
    tod = '2019-06-03'
    # Filter the DataFrame based on the date range
    tofrom = df[(df['started_at'] > fromd) & (df['started_at'] < tod)]
    # Save the filtered DataFrame to a new CSV file
    tofrom.to_csv('may23-june3.csv')

# Set default arguments for the DAG
default_args = {
    'owner': 'paulcrickard',
    'start_date': dt.datetime(2020, 4, 13),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# Create the DAG
with DAG('CleanData',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         ) as dag:

    # Define the cleanData task
    cleanData = PythonOperator(task_id='clean',
                               python_callable=cleanScooter)
    
    # Define the selectData task
    selectData = PythonOperator(task_id='filter',
                                python_callable=filterData)

    # Define the moveFile task
    moveFile = BashOperator(task_id='move',
                            bash_command='mv /home/paulcrickard/may23-june3.csv /home/paulcrickard/Desktop')

# Set task dependencies
cleanData >> selectData >> moveFile
