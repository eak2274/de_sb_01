import os
import sys

# Абсолютный путь к каталогу plugins/helpers
base_path = os.path.dirname(os.path.abspath(__file__))
plugins_path = os.path.abspath(os.path.join(base_path, '..', 'plugins', 'helpers'))
sys.path.append(plugins_path)

print(f"Base path: {base_path}")
print(f"Plugins path: {plugins_path}")
print(f"sys.path: {sys.path}")

try:
    from get_env_values import get_env_value_dict
    print("Импорт прошел успешно!")
except ImportError as e:
    print(f"Ошибка импорта: {e}")

import json

env_value_dict = get_env_value_dict()
print(json.dumps(env_value_dict, indent=4))
