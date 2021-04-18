# Load dependencies and set constants
from confluent_kafka import Producer

# DATA_GENERATION_IN_MB = 1000 # ~ 1GB
DATA_GENERATION_IN_MB = 100
DATASET_SIZE_IN_MB = 10

TWITTER_DATA_PATH = "/home/ubuntu/dataset.json"
KAFKA_TOPIC_TWITTER = "twitter-stream"
# Produce the data / write it to the Kafka Cluster
producer_config = {
    "bootstrap.servers": "localhost:9092",
}
p = Producer(producer_config)

# Fill the topic with the specified amount of data
generation_steps = int(DATA_GENERATION_IN_MB / DATASET_SIZE_IN_MB)
with open(TWITTER_DATA_PATH, "r") as dataset:
    for step in range(generation_steps):
        print(f"Executing data generation step {step}...")
        dataset.seek(0)  # Jump back to first line

        for tweet in dataset:
            try:
                # print("IN QUEUE: {}".format(len(p)))
                p.produce(KAFKA_TOPIC_TWITTER, value=tweet)
                p.poll(0)
            except BufferError:
                print('[INFO] Local producer queue is full (%d messages awaiting delivery): Trying again after flushing...\n' % len(p))
                p.poll(1)

                # Retry sending tweet
                p.produce(KAFKA_TOPIC_TWITTER, value=tweet)

p.flush(30)
print("Data generation done!" + "\n")