# Streaming Analytics for Apache Kafka and Apache Flink
Streaming Analytics Project for the Course "Advanced Analytics and Machine Learning"
- Summer Term 2021 | Ludwig-Maximilians-Universität München

#### Collaborators:
- Giacomo May
- Manuel Neumayer

#### Dataset:
- ~14.500 Tweets from the Twitter Streaming API

##### LRZ Cloud:
Apache Kafka and Flink are evaluated using VMs on the LRZ Cloud:
-  https://cc.lrz.de/auth/login/?next=/

<hr>

The purpose of this project is to analyze and compare two famous Streaming Platforms, **Apache Kafka** and **Apache Flink**, regarding metrics like Throughput, Latency, Processing Speed and Scalability in a both Non-Parallel and Parallel Streaming Scenario.

The results are documented in a conference paper.

#### Terminology
- **Throughput**: Amount of MBs sent per unit time (e.g. second)
- **Latency**: Amount of elapsed time between the point of sending a stream object and receiving it

#### Useful reads
- [Apache Kafka Confluent Benchmark report](https://www.confluent.de/blog/kafka-fastest-messaging-system/)
- [LinkedIn Kafka Benchmark Report](https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines)
