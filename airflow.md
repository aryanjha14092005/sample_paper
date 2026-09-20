# Apache Airflow — GitHub Codespaces

## 1. Check Python

```bash
python3 --version
```

Airflow 3.x works with Python 3.12, so use Python 3.12 if available.

## 2. Create Virtual Environment

```bash
python3.12 -m venv airflow-venv
```

Activate it:

```bash
source airflow-venv/bin/activate
```

## 3. Install Airflow

```bash
AIRFLOW_VERSION=3.0.6
PYTHON_VERSION=3.12
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Check installation:

```bash
airflow version
```

## 4. Set Airflow Home

```bash
export AIRFLOW_HOME=$HOME/airflow
```

## 5. Start Airflow

```bash
airflow standalone
```

Airflow will initialize its database and start the webserver and scheduler.

## 6. Open Airflow

In GitHub Codespaces:

**Ports → Port 8080 → Open in Browser**

## 7. Create DAG Folder

If needed:

```bash
mkdir -p $AIRFLOW_HOME/dags
```

Put your DAG Python files inside:

```text
~/airflow/dags/
```

## 8. Stop Airflow

Press:

```text
CTRL + C
```

## 9. Start Airflow Again

Activate the environment:

```bash
source airflow-venv/bin/activate
```

Then:

```bash
export AIRFLOW_HOME=$HOME/airflow
airflow standalone
```
