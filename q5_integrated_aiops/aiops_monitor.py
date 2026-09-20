from kafka import KafkaConsumer
import json


# Connect to Kafka
consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="aiops-monitor-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)


# Counter for detected anomalies
anomaly_count = 0

print("===== AIOps Monitoring Started =====")
print("Listening for server metrics...\n")


# Continuously consume messages
for message in consumer:

    data = message.value

    server_id = data["server_id"]
    cpu_usage = data["cpu_usage"]
    memory_usage = data["memory_usage"]

    print(
        f"Message received: {server_id} | "
        f"CPU: {cpu_usage}%"
    )

    # Check CPU
    if cpu_usage > 80:

        anomaly_count += 1

        print("ALERT: High CPU detected")

    else:

        print("Normal")

    print(f"Total anomalies detected: {anomaly_count}")
    print("-" * 40)