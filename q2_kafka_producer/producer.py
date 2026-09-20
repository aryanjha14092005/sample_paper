from kafka import KafkaProducer
import json
import time


# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


# Server metric messages
messages = [
    {
        "server_id": "server01",
        "cpu_usage": 82,
        "memory_usage": 65
    },
    {
        "server_id": "server02",
        "cpu_usage": 45,
        "memory_usage": 55
    },
    {
        "server_id": "server03",
        "cpu_usage": 91,
        "memory_usage": 72
    },
    {
        "server_id": "server04",
        "cpu_usage": 67,
        "memory_usage": 60
    },
    {
        "server_id": "server05",
        "cpu_usage": 76,
        "memory_usage": 68
    },
    {
        "server_id": "server06",
        "cpu_usage": 88,
        "memory_usage": 75
    },
    {
        "server_id": "server07",
        "cpu_usage": 52,
        "memory_usage": 50
    },
    {
        "server_id": "server08",
        "cpu_usage": 95,
        "memory_usage": 80
    },
    {
        "server_id": "server09",
        "cpu_usage": 63,
        "memory_usage": 58
    },
    {
        "server_id": "server10",
        "cpu_usage": 79,
        "memory_usage": 64
    }
]


# Send messages to server_metrics
for message in messages:

    producer.send(
        "server_metrics",
        value=message
    )

    print("Message sent:", message)

    time.sleep(1)


# Ensure all messages are delivered
producer.flush()

print("\nAll messages sent successfully!")

producer.close()