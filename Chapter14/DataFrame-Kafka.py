# Purpose:
# This script demonstrates various operations on DataFrames using PySpark.
# It reads a CSV file into a DataFrame, performs various filtering, transformation, and aggregation operations, 
# and also executes SQL queries on the DataFrame.

#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
import os
os.chdir('/home/paulcrickard')

# Create a Spark session
spark = SparkSession.builder.master("spark://pop-os.localdomain:7077").appName('DataFrame-Kafka').getOrCreate()

# Read the CSV file
os.chdir('/home/paulcrickard')
df = spark.read.csv('data.csv')
df.show(5)

# Print the schema of the DataFrame
df.printSchema()

# Read the CSV file with header and infer schema
df = spark.read.csv('data.csv', header=True, inferSchema=True)
df.show(5)

# Print the schema of the DataFrame with the header
df.printSchema()

# Select the 'name' column from the DataFrame
df.select('name').show()

# Perform operations on the DataFrame
u40 = df.filter("age<40").collect()
u40[0].asDict()['name']

# Print each row in the filtered DataFrame as a dictionary
for x in u40:
    print(x.asDict())

# Create a temporary view named 'people' and perform SQL queries on it
df.createOrReplaceTempView('people')
df_over40 = spark.sql("select * from people where age > 40")
df_over40.show()

# Describe the 'age' column for the DataFrame with people over 40
df_over40.describe('age').show()

# Group by 'state' column and count the number of occurrences
df.groupBy('state').count().show()

# Calculate the mean of the 'age' column
df.agg({'age': 'mean'}).show()

# Import pyspark.sql.functions
import pyspark.sql.functions as f

# Perform various DataFrame transformations
df.select(f.collect_set(df['state'])).collect()
df.select(f.countDistinct('state').alias('states')).show()
df.select(f.md5('street').alias('hash')).collect()
df.select(f.reverse(df.state).alias('state-reverse')).collect()
df.select(f.soundex(df.name).alias('soundex')).collect()

# Stop the Spark session
spark.stop()
