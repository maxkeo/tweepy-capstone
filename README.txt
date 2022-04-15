
0. Start Hadoop

start-dfs.sh
start-yarn.sh

1. Kafka             

sudo service zookeeper stop
bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties



bin/kafka-topics.sh --list --bootstrap-server localhost:9092

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tweets




2. Hive

iffy@iffy-VirtualBox:~/softwares/apache-hive-2.3.5-bin/bin$ hive --service metastore

$ hive 



3. Spark 

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.8.jar tweet_consumer.py

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.8.jar tweet_producer..py

– display the size of tweets dir
hdfs dfs -du -s -h /user/hive/warehouse/tweets





