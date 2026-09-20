import pandas as pd
import matplotlib.pyplot as plt


# Create sample server metrics
data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],

    "CPU_Usage": [
        45, 50, 55, 60, 65,
        95, 58, 62, 67, 70,
        72, 75, 97, 68, 71,
        74, 78, 80, 92, 76
    ],

    "Memory_Usage": [
        50, 52, 55, 57, 60,
        65, 62, 63, 64, 66,
        67, 68, 70, 69, 71,
        72, 73, 74, 75, 76
    ],

    "Response_Time": [
        200, 210, 220, 230, 240,
        450, 250, 260, 270, 280,
        290, 300, 480, 310, 320,
        330, 340, 350, 500, 360
    ]
}

df = pd.DataFrame(data)


# Basic statistics
print("\n===== BASIC STATISTICS =====")

print(
    df[
        ["CPU_Usage", "Memory_Usage", "Response_Time"]
    ].describe()
)


# Thresholds
CPU_THRESHOLD = 90
MEMORY_THRESHOLD = 90
RESPONSE_THRESHOLD = 400


# Detect anomalies
df["Anomaly"] = (
    (df["CPU_Usage"] > CPU_THRESHOLD)
    | (df["Memory_Usage"] > MEMORY_THRESHOLD)
    | (df["Response_Time"] > RESPONSE_THRESHOLD)
)


# Print anomalies
anomalies = df[df["Anomaly"]]

print("\n===== ANOMALOUS RECORDS =====")
print(anomalies)

print("\nTotal records:", len(df))
print("Anomalies detected:", len(anomalies))


# Plot CPU usage
plt.figure(figsize=(12, 6))

plt.plot(
    df["Timestamp"],
    df["CPU_Usage"],
    marker="o",
    label="CPU Usage"
)

plt.axhline(
    CPU_THRESHOLD,
    linestyle="--",
    label="CPU Threshold"
)

plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU_Usage"],
    marker="x",
    s=100,
    label="Anomaly"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Usage and Anomalies")

plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()

plt.show()