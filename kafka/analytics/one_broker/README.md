# Apache Kafka - 1 Broker

<br>

This section is dedicated to testing the performance of Apache Kafka using:
- **1** Kafka Broker 
- **1** Topic Partition 
- **1** Producer and Consumer

<hr>
<br>

### Test Configuration
All VMs are running in the LRZ Cloud using Ubuntu 20.04.

##### Test Setup 1:
- **2** vCPUs
- **9** GB RAM

##### Test Setup 2:
- **4** vCPUS
- **18** GB RAM

##### Test Setup 3:
- **10** vCPUs
- **45** GB RAM

<br>

## Results
#### Producer Throughput
<img src="./img/producer_throughput.png" width="75%" height="75%" alt="Producer Throughput">

#### Consumer Throughput
<img src="./img/consumer_throughput.png" width="75%" height="75%" alt="Consumer Throughput"/>

#### Latency
##### 2 vCPUs
<img src="./img/consumer_latency_2vCPUs.png" width="75%" height="75%" alt="2 vCPU latency">

##### 4 vCPUs
<img src="./img/consumer_latency_4vCPUs.png" width="75%" height="75%" alt="4 vCPU latency">

##### 10 vCPUs
<img src="./img/consumer_latency_10vCPUs.png" width="75%" height="75%" alt="10 vCPU latency">
