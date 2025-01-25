from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from numpy import record
import requests
import pandas as pd
import os


def print_welcome():
    print('And again welcome to Airflow!')

def read_file():
    base_path = os.path.dirname(__file__)  # Путь к текущему файлу
    file_path = os.path.join(base_path, '..', 'files', 'myCSV2.csv')  # Построение пути
    df = pd.read_csv(file_path)  # Считывание файла
    print(df.head(2))
    file_path_2 = os.path.join(base_path, '..', 'files', 'myJSON2.json')  # Построение пути
    df.to_json(file_path_2, orient='records')
                     

default_args = {
    "owner": "eak74",
    "retries": 5,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    'read_file',
    default_args=default_args,
    schedule_interval='0 23 * * *',
    start_date=datetime(2025, 1, 12, 15),
    catchup=False
)


print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

read_file_task = PythonOperator(
    task_id='read_file',
    python_callable=read_file,
    dag=dag
)


# Set the dependencies between the tasks
print_welcome_task >> read_file_task
