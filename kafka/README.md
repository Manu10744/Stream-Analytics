# Apache Kafka

<br>

<img src="./img/kafka.jpg" alt="Kafka Infrastructure"/>

<br>

### General Architecture
In Apache Kafka data streams are created from so-called **Topics** that are stored inside the Kafka Cluster. Kafka Servers, which are also called **Brokers**, stream the data from a topic to consumers that are subscribed to this topic. 

At any time only **one** of the Brokers is the active coordinator and the client only needs to connect to one broker in order to be connected to the whole Kafka cluster.

So, in short, an Apache Kafka Streaming Environment has three main components:

- **Producers**: They **produce** the data and send them to the Kafka Cluster
- **Broker**: Stores the arriving new data in the corresponding Topic and sends data to the Consumers
- **Consumers**: Subscribes to a topic and thus **receives** a stream of the data

### Useful Commands and Settings

#### Settings

```bash
# ./config/server.properties

# Number of partitions per topic and thus a factor for possible parallelism.
# Common rule of thumb: Partitions = Desired Throughput / Partition Speed
# (Estimation of speed for one partition: 10 MB/s)
num.partitions=1
```

#### Commands 
###### List all registered Kafka Topics

```bash 
bin/kafka-topics.sh --list --zookeeper localhost:2181
```

###### Delete a specific topic (twitter-stream in this case)
```bash
bin/zookeeper-shell.sh localhost:2181 deleteall /brokers/topics/twitter-stream
```
