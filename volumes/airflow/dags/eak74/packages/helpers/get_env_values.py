import os
from dotenv import load_dotenv
import json

def get_dot_env_path():
    base_path = os.path.dirname(__file__)  # Путь к текущему файлу
    return os.path.normpath(os.path.join(base_path, '..', '..', '..', '.env'))

def cast_value(value):
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value

def load_env_to_dict(env_file_path=None):

    if env_file_path and os.path.exists(env_file_path):
        # Загрузите переменные из .env файла
        load_dotenv(dotenv_path=env_file_path)
    
    # Создайте словарь с переменными окружения и их приведенными значениями
    env_vars = {
        key: cast_value(os.getenv(key)) for key in os.environ if key.startswith('PG_DB') or key.startswith('ES_')
    }
    
    return env_vars

def get_env_value_dict():

    dot_env_path = get_dot_env_path()
    env_value_dict = load_env_to_dict(dot_env_path)
    # print(json.dumps(env_value_dict, indent=4))
    return env_value_dict