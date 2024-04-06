# STEPS

## ACCESS KAFKA_02 FOLDER

```sh
cd KAFKA_02
```
## DOWNLOAD KAFKA
```sh
curl https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz -o kafka.tgz
```

## UNPACKED KAFKA
```sh
tar -xvzf kafka.tgz --strip 1
```

## START KAFKA ZOOKEEPER
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## START KAFKA SERVER
```sh
bin/kafka-server-start.sh config/server.properties
```

## CREATE TOPIC
```sh
bin/kafka-topics.sh --create --boostrap-server localhost:9092 --topics cities
```

## LIST AVAILABLE TOPICS
```sh
bin/kafka-topics.sh --list --boostrap-server localhost:9092
```

## ACCESS INFORMATION ABOUT A TOPIC
```sh
bin/kafka-topics.sh --describe --boostrap-server localhost:9092 --topics cities
```

## PRODUCE CONSOLE MESSAGES
```sh
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic cities
```

## CONSUME CONSOLE MESSAGES
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cities
```