from datetime import datetime, timedelta

from airflow import DAG
from custom_operators import MyCustomOperator


# Определяем default_args для DAG
default_args = {
    "owner": "eak74",
    "retries": 5,
    "retry_delay": timedelta(minutes=1)
}

# Создаем DAG
dag = DAG(
    'use_custom_operator',
    default_args=default_args,
    schedule_interval='0 23 * * *',
    start_date=datetime(2025, 1, 21, 15),
    catchup=False
)

# Задаем задачи
task_mycustop = MyCustomOperator(
    task_id='task_mycustop',
    param='Johnny Be Good',
    dag=dag
)
# Устанавливаем зависимости между задачами
task_mycustop
