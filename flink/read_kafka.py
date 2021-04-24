from pyflink.datastream.functions import ProcessFunction
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.datastream.connectors import FlinkKafkaConsumer
import time
import sys
from matplotlib import pyplot as plt

# Number of tweets in the dataset (10 MB)
NUMBER_OF_TWEETS = 14484
# Number of times the dataset is produced by Kafka
NUMBER_OF_PRODUCTIONS = 10

latencies = []
records_received = 0
kafka_props = {'bootstrap.servers': 'localhost:9092', 'group.id': 'twitter_consumers'}


def collect_stats():
    plt.plot(latencies)
    plt.show()
    sys.exit()


class MyProcessFunction(ProcessFunction):

    def process_element(self, value, ctx: 'ProcessFunction.Context'):
        latency = (time.time() * 1000) - ctx.timestamp()
        result = str(latency)
        yield result
        latencies.append(latency)
        # global might not be ideal here (parallelism possible?) but currently nothing else comes to mind
        global records_received
        records_received += 1
        if records_received >= NUMBER_OF_TWEETS * NUMBER_OF_PRODUCTIONS:
            collect_stats()


env = StreamExecutionEnvironment.get_execution_environment()
env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
env.set_parallelism(2)

kafka_consumer = FlinkKafkaConsumer("twitter-stream", SimpleStringSchema(), kafka_props)

stream = env.add_source(kafka_consumer)
stream.process(MyProcessFunction(), output_type=Types.STRING()).print()
env.execute()

# TODO: Write function for plotting and call it from process-function

'''
Notes: 
- Using EventTime here to get Kafka Timestamp. 


type_info = Types.ROW([Types.ROW([Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]), Types.STRING(), Types.STRING(), Types.STRING(),
                                 Types.STRING(), Types.STRING()]),
                      Types.ROW([Types.ROW([Types.ROW([Types.BOOLEAN(), Types.STRING(), Types.STRING(), Types.STRING(), Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()]),
                                                       Types.STRING()])])]),
                      Types.ROW([Types.ROW([Types.INT(), Types.STRING()])])])
json_row_schema = JsonRowDeserializationSchema.builder().type_info(type_info).build()
'''
