import airflow
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    "3_5_aiflow_import",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "retries": 3,
        "retry_delay": timedelta(minutes=1),
    },
    description="import_connections_and_variables",
    schedule="@once",
    start_date=datetime(2023, 12, 03),
    catchup=False,
    tags=["aieflow_2"],
)

t1 = BashOperator(
    task_id="import_connections_and_variables",
    bash_command="airflow connections import /opt/airflow/dags/connections.json && airflow variables import /opt/airflow/dags/variables.json",
    dag=dag,
)

t1