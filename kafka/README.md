# Apache Kafka

<img src="./img/kafka.jpg" width="250px" height="350px" alt="Scanned" />

<br>

In Apache Kafka data streams are created from so-called **Topics** that are stored inside the Kafka Cluster. Kafka Servers, which are also called **Brokers**, stream the data from a topic to consumers that are subscribed to this topic. At any time only **one** of the Brokers is the active coordinator and the client only needs to connect to one broker in order to be connected to the whole Kafka cluster.

So, an Apache Kafka Streaming Environment has three main components:

- **Producers**: They **produce** the data and send them to the Kafka Cluster
- **Broker**: Stores the arriving new data in the corresponding Topic and sends data to the Consumers
- **Consumers**: Subscribes to a topic and thus **receives** a stream of the data


