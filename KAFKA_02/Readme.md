# STEPS

## BASIC RUN

### ACCESS KAFKA_02 FOLDER
```sh
cd KAFKA_02
```
### DOWNLOAD KAFKA
```sh
curl https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz -o kafka.tgz
```

### UNPACKED KAFKA
```sh
tar -xvzf kafka.tgz --strip 1
```

### START KAFKA ZOOKEEPER
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### START KAFKA SERVER
```sh
bin/kafka-server-start.sh config/server.properties
```

### CREATE TOPIC
```sh
bin/kafka-topics.sh --create --boostrap-server localhost:9092 --topics cities
```

### LIST AVAILABLE TOPICS
```sh
bin/kafka-topics.sh --list --boostrap-server localhost:9092
```

### ACCESS INFORMATION ABOUT A TOPIC
```sh
bin/kafka-topics.sh --describe --boostrap-server localhost:9092 --topics cities
```

### PRODUCE CONSOLE MESSAGES
```sh
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic cities
```

### CONSUME CONSOLE MESSAGES
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cities
```

## MULTIPLE PARTITION RUN

### START ZOOKEEPER
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### START KAFKA BROKER
```sh
bin/kafka-server-start.sh config/server.properties
```

### CREATE TOPIC
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --replication-factor 1 --partitions 3 --topic names
```

### LIST TOPICS
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### TOPIC DETAILS
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic names
```

### START CONSOLE PRODUCER
```sh
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic names
```

### START CONSOLE CONSUMER
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test
```

### START CONSOLE CONSUMER AND READ MESSAGES FROM BEGINNING
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic animals --from-beginning
```

### START CONSOLE CONSUMER AND READ MESSAGES FROM BEGINNING FROM SPECIFIC PARTITION
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --partition 2 --topic animals --from-beginning
```

### START CONSOLE CONSUMER AND READ MESSAGES FROM SPECIFIC OFFSET FROM SPECIFIC PARTITION
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --partition 2 --topic animals --offset 0
```

### START CONSOLE CONSUMER WITH SPECIFIC CONSUMER GROUP
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --group test --from-beginning
```

### LIST CONSUMER GROUPS
```sh
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

### CONSUMER GROUP DETAILS
```sh
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group test --describe
```

## MULTIPLE BROOKERS

### START ZOOKEEPER
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### START KAFKA BROKER
```sh
bin/kafka-server-start.sh config/server0.properties
bin/kafka-server-start.sh config/server1.properties
bin/kafka-server-start.sh config/server2.properties
```

### GET INFORMATION FROM ZOOKEEPER ABOUT ACTIVE BROKER IDS
```sh
bin/zookeeper-shell.sh localhost:2181 ls /brokers/ids
```

### GET INFORMATION FROM ZOOKEEPER ABOUT SPECIFIC BROKER BY ID
```sh
bin/zookeeper-shell.sh localhost:2181 get /brokers/ids/0
```

### CREATE TOPIC
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --create --replication-factor 3 --partitions 5 --topic animals
```

### LIST TOPICS
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --list
```

### TOPIC DETAILS
```sh
bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --describe --topic animals
```

### START CONSOLE PRODUCER
```sh
bin/kafka-console-producer.sh --broker-list localhost:9092,localhost:9093,localhost:9094 --topic animals
```

### START CONSOLE CONSUMER
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic animals
```

### START CONSOLE CONSUMER AND READ MESSAGES FROM BEGINNING
```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic test-topic --from-beginning
```