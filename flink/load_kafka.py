from pyflink.common.serialization import JsonRowDeserializationSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

type_info = Types.ROW([Types.ROW([Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]), Types.STRING(), Types.STRING(), Types.STRING(),
                                 Types.STRING(), Types.STRING()]),
                      Types.ROW([Types.ROW([Types.ROW([Types.BOOLEAN(), Types.STRING(), Types.STRING(), Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]),
                                                       Types.STRING()])])]),
                      Types.ROW([Types.ROW([Types.STRING(), Types.STRING()])])])
json_row_schema = JsonRowDeserializationSchema.builder().type_info(type_info).build()
kafka_props = {'bootstrap.servers': 'localhost:9092', 'group.id': 'twitter_consumers'}
kafka_consumer = FlinkKafkaConsumer("twitter-stream", json_row_schema, kafka_props)

ds = env.add_source(kafka_consumer)
ds.print()
env.execute()


'''
submit job: 
./bin/flink run --python /home/ubuntu/load_kafka.py --jarfile /home/ubuntu/flink-sql-connector-kafka_2.11-1.12.0.jar

'''



