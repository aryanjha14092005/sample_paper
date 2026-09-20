from kafka import KafkaConsumer
import json


# Connect to Kafka and subscribe to server_metrics
consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="aiops-consumer-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)


print("Consumer started...")
print("Waiting for server metrics...\n")


# Continuously receive messages
for message in consumer:

    data = message.value

    server_id = data["server_id"]
    cpu_usage = data["cpu_usage"]
    memory_usage = data["memory_usage"]

    print("Received:")
    print(f"Server: {server_id}")
    print(f"CPU: {cpu_usage}%")
    print(f"Memory: {memory_usage}%")

    # Check CPU usage
    if cpu_usage > 80:
        print(f"ALERT: High CPU detected on {server_id}")
    else:
        print("Normal")

    print("-" * 40)