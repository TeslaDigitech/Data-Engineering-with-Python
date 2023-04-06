# Purpose:
# The script creates a Kafka consumer that subscribes to the 'users' topic, listens for messages, 
# and prints them to the console as they are received. The consumer is configured with three bootstrap servers and
# an 'earliest' offset reset policy.
from confluent_kafka import Consumer

# Create a Kafka consumer with the given configuration
c = Consumer({
    'bootstrap.servers': 'localhost:9092,localhost:9093,localhost9093',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
})

# List all topics and their metadata
t = c.list_topics()
t.topics

# Output example:
# {'people': TopicMetadata(people, 1 partitions), '__transaction_state': TopicMetadata(__transaction_state, 50 partitions), 'users': TopicMetadata(users, 3 partitions), 'dataengineering': TopicMetadata(dataengineering, 1 partitions), '__consumer_offsets': TopicMetadata(__consumer_offsets, 50 partitions)}

# Get the partitions of the 'users' topic
t.topics['users'].partitions
# {0: PartitionMetadata(0), 1: PartitionMetadata(1), 2: PartitionMetadata(2)}

# Subscribe the consumer to the 'users' topic
c.subscribe(['users'])

# Poll for messages in an infinite loop
while True:
    msg = c.poll(1.0)  # Timeout of 1.0 seconds

    if msg is None:
        # If no message received, continue polling
        continue

    if msg.error():
        # If there is an error, print it and continue polling
        print("Error: {}".format(msg.error()))
        continue

    # Decode the message value and print it
    data = msg.value().decode('utf-8')
    print(data)

# Close the consumer
c.close()
