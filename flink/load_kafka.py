from pyflink.common.serialization import SimpleStringSchema, JsonRowDeserializationSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
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
kafka_consumer = FlinkKafkaConsumer("twitter-stream-source", json_row_schema, kafka_props)
# research this
kafka_consumer.set_start_from_earliest()

ds = env.add_source(kafka_consumer)
ds.print()
ds.execute()



