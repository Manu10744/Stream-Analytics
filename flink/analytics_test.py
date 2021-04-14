from pyflink.dataset import ExecutionEnvironment
from pyflink.table import TableConfig, DataTypes, BatchTableEnvironment
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
from pyflink.table.expressions import lit

exec_env = ExecutionEnvironment.get_execution_environment()
exec_env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(exec_env, t_config)

# specify input format as table rows
twitter_source_ddl = """
    create table tweets (
        data ROW<text STRING, pub_met ROW<rtc INT, rpc INT, lc INT, qc INT>, a_ID STRING, ID STRING, c_at STRING, source STRING, lang STRING>,
        includes ROW<users ARRAY<ROW<protected BOOLEAN, ID STRING, name STRING, c_at STRING, pub_met ROW<fc INT, fng_c INT, tc INT, lc INT>, un STRING>>>,
        matching_rules ARRAY<ROW<ID STRING, tag STRING>>
        
    ) with (
        'connector' = 'filesystem',
        'format' = 'json',
        'path' = '/home/snoops/AAML/Stream-Analytics/data'
    )
"""

t_env.execute_sql(twitter_source_ddl)

tab = t_env.from_path("tweets")



'''
Exemplary Tweet Format: 
{"data": {"text": "Polsek Kakas Cegah Covid-19 https://t.co/ADjEgpt7bC",
          "public_metrics": {"retweet_count": 0, "reply_count": 0, "like_count": 0, "quote_count": 0},
          "author_id": "1367839185764151302", "id": "1378275866279469059", "created_at": "2021-04-03T09:19:08.000Z",
          "source": "Twitter for Android", "lang": "in"},
 "includes": {"users": [{"protected": false, "id": "1367839185764151302", "name": "Nathan Pareda",
                         "created_at": "2021-03-05T14:07:56.000Z",
                         "public_metrics": {"followers_count": 0, "following_count": 0, "tweet_count": 557,
                                            "listed_count": 0}, "username": "NathanPareda"}]},
 "matching_rules": [{"id": 1378112825051246596, "tag": "coronavirus"}]}
'''