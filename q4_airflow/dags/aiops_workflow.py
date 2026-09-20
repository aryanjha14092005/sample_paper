from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def collect_metrics():
    cpu = 87
    memory = 65
    response_time = 420

    print("===== Metrics Collected =====")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")
    print(f"Response Time: {response_time}ms")


def process_metrics():
    cpu = 87
    memory = 65
    response_time = 420

    print("===== Processing Metrics =====")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")
    print(f"Response Time: {response_time}ms")


def detect_anomaly():
    cpu = 87

    print("===== Anomaly Detection =====")

    if cpu > 80:
        print("Anomaly detected: High CPU usage")
    else:
        print("No anomaly detected")


def generate_report():
    print("===== AIOps Report =====")
    print("Metrics collected successfully")
    print("Metrics processed successfully")
    print("Anomaly detection completed")
    print("========================")


with DAG(
    dag_id="aiops_workflow",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    collect_metrics = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics
    )

    process_metrics = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics
    )

    detect_anomaly = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly
    )

    generate_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    collect_metrics >> process_metrics >> detect_anomaly >> generate_report