### Instructions
1. Set up Flink (requires JDK 8 and Python >= 3.5) - Download and untar Flink:    
`$ wget https://downloads.apache.org/flink/flink-1.12.2/flink-1.12.2-bin-scala_2.11.tgz`  
`$ tar -zxvf flink-1.12.2-bin-scala_2.11.tgz`


2. Install PyFlink:  
`$ python3 -m pip install apache-flink`  
     

3. Download dependency (Kafka-Connector)  
`$ wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka_2.11/1.12.2/flink-sql-connector-kafka_2.11-1.12.2.jar`
   

4. Start Flink cluster:  
`$ cd flink-1.12.2`  
   `$ ./bin/start-cluster.sh`   
   

5. Open `flink_stream.ipynb` and run the cells  


6. Set up Kakfka cluster see details in `../kafka/kafka_setup.ipynb`)  


7. Open `setup_kafka.ipynb` and run the cells (= write data to Kafka topic from which Flink will read it)  


8. Open `kafka_consumer.ipynb` and run the cells (= read latencies Flink wrote to Kafka topic)
