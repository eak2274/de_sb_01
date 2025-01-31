from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.hooks.base import BaseHook


# Функция для чтения данных из Postgresql и записи в CSV
def get_conn_params():
    # conn_string = f"dbname='{db_params['PG_DB_NAME']}' host='{db_params['PG_DB_HOST']}' user='{db_params['PG_DB_USER']}' password='{db_params['PG_DB_PASSWORD']}'"
    # conn = db.connect(conn_string)
    # cur = conn.cursor()

    # query = "COPY (SELECT * FROM users WHERE id > 138) TO STDOUT WITH CSV HEADER DELIMITER ','"

    # base_path = os.path.dirname(os.path.abspath(__file__))  # Абсолютный путь к текущему файлу
    # file_path = os.path.join(base_path, '..', '..', '..', 'files', 'tmp_from_db.csv')  # Построение пути

    # with open(file_path, 'w') as f:
    #     cur.copy_expert(query, f)

    conn = BaseHook.get_connection('oci_cloud_pg_conn')
    print(f'host: {conn.host}')
    print(f'port: {conn.port}')
    print(f'schema: {conn.schema}')
    print(f'login: {conn.login}')
    print(f'password: {conn.password}')


def fetch_data_thru_hook():
    hook = PostgresHook(postgres_conn_id="oci_cloud_pg_conn")
    with hook.get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM public.users LIMIT 10")
            records = cursor.fetchall()
            for record in records:
                print(record)

# Определяем default_args для DAG
default_args = {
    "owner": "eak74",
    "retries": 5,
    "retry_delay": timedelta(minutes=1)
}

# Создаем DAG
dag = DAG(
    'get_data_from_pg_thru_configured_conn',
    default_args=default_args,
    schedule_interval='0 23 * * *',
    start_date=datetime(2025, 1, 21, 15),
    catchup=False
)

# Задаем задачи
task_get_conn_params = PythonOperator(
    task_id='get_conn_params',
    python_callable=get_conn_params,
    dag=dag
)

# Option 1 PostgresOperator for SELECT, stroing result in xcom
task_select_and_log_data = PostgresOperator(
        task_id="select_and_log_data_task",
        postgres_conn_id="oci_cloud_pg_conn",
        sql="SELECT * FROM public.users LIMIT 10",
        do_xcom_push=True,
        dag=dag
    )

# Option 2 Fetching data from PG through PostgresHook
task_fetch_data_thru_hook = PythonOperator(
    dag=dag,
    task_id='fetch_data_thru_hook',
    python_callable=fetch_data_thru_hook
)

task_print_params_from_cmd_line = BashOperator(
    dag=dag,
    task_id="print_params_from_cli",
    bash_command="python3 /opt/airflow/dags/eak74/scripts/task_04/script_01.py --name Alice --age 24 --city NYC"
)

# Устанавливаем зависимости между задачами
task_get_conn_params >> task_select_and_log_data >> task_fetch_data_thru_hook >> task_print_params_from_cmd_line
