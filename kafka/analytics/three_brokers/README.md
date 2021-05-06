# Apache Kafka - 3 Brokers

<br>

This section is dedicated to testing the performance of Apache Kafka using:
- **3** Kafka Brokers 
- **3** Topic Partitions
- **3** Producers and Consumers

<hr>
<br>

### Test Configuration
All VMs are running in the LRZ Cloud using Ubuntu 20.04.

##### Test Setup:
For each Broker we are using:
- **10** vCPUS
- **45** GB RAM

<br>

## Results
####  Throughput
<img src="./img/3_broker_throughputs.png" width="75%" height="75%" alt="Producer Throughput">

#### Latency
##### Consumer 1
<img src="./img/consumer1_latencies.png" width="75%" height="75%" alt="consumer 1 latency">

##### Consumer 2
<img src="./img/consumer2_latencies.png" width="75%" height="75%" alt="consumer 2 latency">

##### Consumer 3
<img src="./img/consumer3_latencies.png" width="75%" height="75%" alt="consumer 3 latency">