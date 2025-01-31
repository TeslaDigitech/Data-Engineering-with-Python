# Purpose:
# The script creates a Kafka producer that generates 10 messages with random user data using the Faker library and sends them to the 'users' topic. 
# The producer is configured with three bootstrap servers. The script also defines a callback function to handle message delivery reports.
from confluent_kafka import Producer
from faker import Faker
import json
import time

# Initialize the Faker library for generating random data
fake = Faker()

# Create a Kafka producer with the given configuration
p = Producer({'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094'})

# Define a callback function to handle message delivery reports
def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        print("{} : Message on topic {} on partition {} with value of {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(msg.timestamp()[1] / 1000)), msg.topic(), msg.partition(), msg.value().decode('utf-8')))

# Produce 10 messages with random data
for i in range(10):
    data = {
        "name": fake.name(),
        "age": fake.random_int(min=18, max=80, step=1),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip": fake.zipcode()
    }
    m = json.dumps(data)
    p.poll(0)
    p.produce('users', m.encode('utf-8'), callback=receipt)

# Flush the producer to ensure all messages are sent
p.flush()
