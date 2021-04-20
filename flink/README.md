### Instructions
1. Setup Flink (requires JDK 8 and Python >= 3.5) - Download and untar Flink:    
`$ wget https://downloads.apache.org/flink/flink-1.12.2/flink-1.12.2-bin-scala_2.11.tgz`  
`$ tar -zxvf flink-1.12.2-bin-scala_2.11.tgz`


2. Install PyFlink:  
`$ python3 -m pip install apache-flink`  
   
   
3. Download python-script:  
`$ wget https://raw.githubusercontent.com/Manu10744/Stream-Analytics/master/flink/read_kafka.py` 
   

4. Download dependency (Kafka-Connector)  
`$ wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka_2.11/1.12.2/flink-sql-connector-kafka_2.11-1.12.2.jar`
   

5. Change to Flink directory and run the application (won't do anything until Kafka has produced data):  
`$ cd flink-1.12.2`  
   `$ ./bin/start-cluster.sh`  
   `$ ./bin/flink run --python /home/ubuntu/read_kafka.py --jarfile /home/ubuntu/flink-sql-connector-kafka_2.11-1.12.2.jar
`

    For a jupyter notebook environment:
    1. If not done yet, setup a Kafka Environment (see details in `../kafka/kafka_setup.ipynb`)
    2. Open `flink_stream.ipynb` and run the cells
    3. Write data to the Kafka topic, e.g. with `../kafka/analytics/one_broker/producer.ipynb`. Flink will then read the data from the topic.