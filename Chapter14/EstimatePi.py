# Purpose:
# This script demonstrates estimating the value of Pi using the Monte Carlo method in PySpark.
#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import findspark
findspark.init()

# Import the pyspark library and create a Spark session
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("spark://pop-os.localdomain:7077").appName('Pi-Estimation').getOrCreate()

# Import the random module
import random

# Define the number of samples
NUM_SAMPLES = 1

# Define a function that returns True if a random point falls inside a unit circle
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

# Estimate the value of Pi using the Monte Carlo method
count = spark.sparkContext('Pi-Example').parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
print("Pi is roughly {}".format(4.0 * count / NUM_SAMPLES))

# Stop the Spark session
spark.stop()
