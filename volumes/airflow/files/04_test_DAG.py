from datetime import datetime, timedelta
import os
import sys
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch, helpers

# Абсолютный путь к каталогу plugins/helpers
base_path = os.path.dirname(os.path.abspath(__file__))
helpers_path = os.path.abspath(os.path.join(base_path, '..', 'plugins', 'helpers'))
sys.path.append(helpers_path)

# Добавляем отладочные принты
print(f"Base path: {base_path}")
print(f"Helpers path: {helpers_path}")
print(f"sys.path: {sys.path}")

try:
    from get_env_values import get_env_value_dict
    print("Импорт прошел успешно!")
except ImportError as e:
    print(f"Ошибка импорта: {e}")

# Функция для загрузки переменных окружения
def load_db_params():
    return get_env_value_dict()

# Функция для чтения данных из Postgresql и записи в CSV
def get_from_pg_and_write_to_csv(db_params, **kwargs):
    conn_string = f"dbname='{db_params['DB_NAME']}' host='{db_params['DB_HOST']}' user='{db_params['DB_USER']}' password='{db_params['DB_PASSWORD']}'"
    conn = db.connect(conn_string)
    cur = conn.cursor()

    query = "COPY (SELECT * FROM users WHERE id > 138) TO STDOUT WITH CSV HEADER DELIMITER ','"

    base_path = os.path.dirname(os.path.abspath(__file__))  # Абсолютный путь к текущему файлу
    file_path = os.path.join(base_path, '..', 'files', 'tmp_from_db.csv')  # Построение пути

    with open(file_path, 'w') as f:
        cur.copy_expert(query, f)

# Функция для чтения данных из CSV и записи в Elasticsearch
def get_from_csv_and_write_to_es(db_params, **kwargs):
    es = Elasticsearch(
        hosts=[{"host": db_params['ES_HOST'], "port": db_params['ES_PORT']}]
    )

    base_path = os.path.dirname(os.path.abspath(__file__))  # Абсолютный путь к текущему файлу
    file_path = os.path.join(base_path, '..', 'files', 'tmp_from_db.csv')  # Построение пути

    df = pd.read_csv(file_path)  # Считывание файла
    
    # Bulk-adding docs to the 'users' index
    try:
        actions = [
            {
                "_index": "users",
                "_source": record
            }
            for record in df.to_dict(orient='records')
        ]
        success, failed = helpers.bulk(es, actions)
        print(f"Результат индексации: {success} документов успешно добавлено, {failed} неудачных операций.")
    except Exception as e:
        print(f"Ошибка индексации: {e}")

# Определяем default_args для DAG
default_args = {
    "owner": "eak74",
    "retries": 5,
    "retry_delay": timedelta(minutes=1)
}

# Создаем DAG
dag = DAG(
    'get_data_from_pg_and_put_to_es',
    default_args=default_args,
    schedule_interval='0 23 * * *',
    start_date=datetime(2025, 1, 21, 15),
    catchup=False
)

# Загружаем параметры подключения
db_params = load_db_params()

# Задаем задачи
task_get_from_pg_and_write_to_csv = PythonOperator(
    task_id='get_from_pg_and_write_to_csv',
    python_callable=get_from_pg_and_write_to_csv,
    op_kwargs={'db_params': db_params},
    dag=dag
)

task_get_from_csv_and_write_to_es = PythonOperator(
    task_id='get_from_csv_and_write_to_es',
    python_callable=get_from_csv_and_write_to_es,
    op_kwargs={'db_params': db_params},
    dag=dag
)

# Устанавливаем зависимости между задачами
task_get_from_pg_and_write_to_csv >> task_get_from_csv_and_write_to_es