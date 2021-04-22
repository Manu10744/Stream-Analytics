from pyflink.common.serialization import JsonRowDeserializationSchema
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.datastream.connectors import FlinkKafkaConsumer

env = StreamExecutionEnvironment.get_execution_environment()
env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
env.set_parallelism(1)

'''
type_info = Types.ROW([Types.ROW([Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]), Types.STRING(), Types.STRING(), Types.STRING(),
                                 Types.STRING(), Types.STRING()]),
                      Types.ROW([Types.ROW([Types.ROW([Types.BOOLEAN(), Types.STRING(), Types.STRING(), Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]),
                                                       Types.STRING()])])]),
                      Types.ROW([Types.ROW([Types.INT(), Types.STRING()])])])
json_row_schema = JsonRowDeserializationSchema.builder().type_info(type_info).build()
'''


def just_print(msg):
    return "Message: {}".format(msg)


kafka_props = {'bootstrap.servers': 'localhost:9092', 'group.id': 'twitter_consumers'}
# kafka_consumer = FlinkKafkaConsumer("twitter-stream", json_row_schema, kafka_props)
kafka_consumer = FlinkKafkaConsumer("twitter-stream", SimpleStringSchema(), kafka_props)

stream = env.add_source(kafka_consumer)
stream_ts = stream.map(lambda x: x.timestamp())
stream_ts.print()
env.execute()


'''
submit job: 
./bin/flink run --python /home/ubuntu/read_kafka.py --jarfile /home/ubuntu/flink-sql-connector-kafka_2.11-1.12.0.jar

Example json: 

{"data":{"text":"text",
         "public_metrics":{"retweet_count":0,"reply_count":0,"like_count":0,"quote_count":0},
         "author_id":"1","id":"1","created_at":"2030-05-11T09:19:08.000Z",
         "source":"Twitter for Android","lang":"in"},
 "includes":{"users":[{"protected":false,"id":"1",
         "name":"A","created_at":"2030-05-11T09:19:08.000Z",
         "public_metrics":{"followers_count":0,"following_count":0,"tweet_count":557,"listed_count":0},"username":"A"}]},
 "matching_rules":[{"id":1,"tag":"A"}]}
'''

'''
Notes: 
- It seems that there can't be Timestamping without Watermarking. We need Timestamping because I'm not sure the timestamp 
  from Kafka can be accessed otherwise. 
'''