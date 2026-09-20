# Apache Airflow Setup in GitHub Codespaces

This guide explains how to install, start, and use Apache Airflow in a GitHub Codespace, including how to create and run DAG (`.py`) files.

---

## 1. Check Python

First, check the installed Python version:

```bash
python3 --version
```

Airflow 3.x works with Python 3.12, so use Python 3.12 if it is available.

Check specifically for Python 3.12:

```bash
python3.12 --version
```

---

## 2. Create a Virtual Environment

Create a Python 3.12 virtual environment:

```bash
python3.12 -m venv airflow-venv
```

Activate the environment:

```bash
source airflow-venv/bin/activate
```

You should now see something similar to:

```text
(airflow-venv)
```

at the beginning of your terminal prompt.

---

## 3. Install Apache Airflow

Set the Airflow version:

```bash
AIRFLOW_VERSION=3.0.6
PYTHON_VERSION=3.12
```

Create the Airflow constraints URL:

```bash
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
```

Install Airflow:

```bash
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Check that Airflow was installed correctly:

```bash
airflow version
```

Expected output will be similar to:

```text
3.0.6
```

---

## 4. Set Airflow Home

Set the Airflow home directory:

```bash
export AIRFLOW_HOME=$HOME/airflow
```

This tells Airflow where to store its database, logs, configuration, and DAGs.

The directory structure will look approximately like:

```text
~/airflow/
├── airflow.cfg
├── airflow.db
├── logs/
└── dags/
```

---

## 5. Create the DAG Folder

Create the DAG directory if it does not already exist:

```bash
mkdir -p $AIRFLOW_HOME/dags
```

Your DAG files will be placed inside:

```text
~/airflow/dags/
```

For example:

```text
~/airflow/
└── dags/
    ├── my_dag.py
    ├── kafka_dag.py
    └── another_dag.py
```

---

# 6. Create a DAG File

Go to the DAG directory:

```bash
cd $AIRFLOW_HOME/dags
```

Create a Python file:

```bash
touch my_dag.py
```

You can also create/edit the file directly using the Codespaces VS Code editor.

Example DAG:

```python
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2026, 9, 21),
    schedule=None,
    catchup=False,
) as dag:

    task = BashOperator(
        task_id="hello",
        bash_command="echo Hello Airflow!",
    )
```

Save the file inside:

```text
~/airflow/dags/my_dag.py
```

---

# 7. Start Airflow

Make sure the virtual environment is activated:

```bash
source airflow-venv/bin/activate
```

Make sure `AIRFLOW_HOME` is set:

```bash
export AIRFLOW_HOME=$HOME/airflow
```

Then start Airflow:

```bash
airflow standalone
```

Airflow will initialize its database and start the required services.

**Keep this terminal running while you use Airflow.**

---

# 8. Open Airflow in GitHub Codespaces

After running:

```bash
airflow standalone
```

Airflow will run on port `8080`.

In GitHub Codespaces:

```text
Ports
   ↓
Port 8080
   ↓
Open in Browser
```

This will open the Airflow web interface.

---

# 9. Create/Edit DAGs While Airflow Is Running

You can use a second terminal in Codespaces to create or edit your DAG.

For example:

```text
Terminal 1
────────────────────────
airflow standalone
        ↓
Airflow running on 8080


Terminal 2
────────────────────────
source airflow-venv/bin/activate
cd ~/airflow/dags
        ↓
Create/edit my_dag.py
```

You **do not need to start Airflow again** in Terminal 2.

Airflow's scheduler will automatically detect DAG files placed in the configured `dags` directory.

---

# 10. Stop Airflow

To stop Airflow, go to the terminal where:

```bash
airflow standalone
```

is running.

Press:

```text
CTRL + C
```

---

# 11. Start Airflow Again

When you return to the Codespace later, activate the environment:

```bash
source airflow-venv/bin/activate
```

Set the Airflow home:

```bash
export AIRFLOW_HOME=$HOME/airflow
```

Then start Airflow:

```bash
airflow standalone
```

Open:

```text
Ports → 8080 → Open in Browser
```

Your existing DAG files inside:

```text
~/airflow/dags/
```

will still be available.

---

# 12. Complete Workflow

The complete workflow can be remembered as:

```text
Start GitHub Codespace
        ↓
Check Python 3.12
        ↓
Create virtual environment
        ↓
Activate virtual environment
        ↓
Install Airflow
        ↓
Set AIRFLOW_HOME
        ↓
Create ~/airflow/dags
        ↓
Create DAG .py file
        ↓
Start Airflow
        ↓
airflow standalone
        ↓
Open Port 8080
        ↓
Airflow Web UI
        ↓
Check / Run DAG
```

---

# 13. Important Commands Cheat Sheet

### Check Python

```bash
python3 --version
python3.12 --version
```

### Create environment

```bash
python3.12 -m venv airflow-venv
```

### Activate environment

```bash
source airflow-venv/bin/activate
```

### Set Airflow Home

```bash
export AIRFLOW_HOME=$HOME/airflow
```

### Create DAG folder

```bash
mkdir -p $AIRFLOW_HOME/dags
```

### Go to DAG folder

```bash
cd $AIRFLOW_HOME/dags
```

### Create DAG

```bash
touch my_dag.py
```

### Check Airflow

```bash
airflow version
```

### Start Airflow

```bash
airflow standalone
```

### Stop Airflow

```text
CTRL + C
```

---

# 14. Important Concept

The most important thing to remember is:

```text
AIRFLOW_HOME
      │
      └── dags/
            │
            ├── dag1.py
            ├── dag2.py
            └── dag3.py
```

**Airflow watches the `dags` folder for DAG Python files.**

You can therefore:

1. Start Airflow in one terminal.
2. Open another terminal.
3. Create/edit your `.py` DAG file.
4. Save it inside `$AIRFLOW_HOME/dags/`.
5. Airflow detects the DAG.
6. Open the Airflow UI through port `8080`.
7. Run the DAG from the UI.
