# Kafka KRaft with Docker

## 1. `kafka.yml`

```yaml
services:
  kafka:
    image: apache/kafka:4.0.1
    container_name: kafka-kraft
    ports:
      - "9092:9092"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093

      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"

      CLUSTER_ID: MkU3OEVBNTcwNTJENDM2Qk
```

## 2. Create and Start Kafka Container

```bash
docker compose -f kafka.yml up -d
```

Check:

```bash
docker compose -f kafka.yml ps
```

## 3. Create Topic

```bash
docker exec -it kafka-kraft \
kafka-topics.sh \
--create \
--topic test \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

List topics:

```bash
docker exec -it kafka-kraft \
kafka-topics.sh \
--list \
--bootstrap-server localhost:9092
```

## 4. Start Producer

```bash
docker exec -it kafka-kraft \
kafka-console-producer.sh \
--topic test \
--bootstrap-server localhost:9092
```

Type messages and press Enter:

```text
Hello Kafka
Message 2
Message 3
```

## 5. Start Consumer

Open another terminal:

```bash
docker exec -it kafka-kraft \
kafka-console-consumer.sh \
--topic test \
--bootstrap-server localhost:9092 \
--from-beginning
```

## 6. Stop Kafka

```bash
docker compose -f kafka.yml down
```
