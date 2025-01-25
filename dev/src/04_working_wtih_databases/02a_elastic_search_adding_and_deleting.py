from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

faker = Faker()

es = Elasticsearch(
    hosts=["http://localhost:9200"]#,  # Без аутентификации
    # request_timeout=30  # Новый параметр для установки таймаута
)

# 01. Creating index 'users' and adding single doc
doc = {"name": "John Doe", "age": 30, "job": "developer"}

try:
    response = es.index(index="users", document=doc)
    print("Результат индексации:", response)
except Exception as e:
    print(f"Ошибка индексации: {e}")
print()

# 02. Deleting index 'users'
try:
    response = es.indices.delete(index="users")
    print("Индекс удален:", response)
except Exception as e:
    print(f"Ошибка при удалении индекса: {e}")
print()


# 03. Bulk-adding docs to the 'users' index
try:
    actions = [
        {
            "_index": "users",
            # "_type": "doc",
            "_source": {
                "name": faker.name(),
                "street": faker.street_address(),
                "city": faker.city(),
                "zip": faker.zipcode()
            }
        }
        for _ in range(9)  # or for i,r in df.iterrows()
    ]
    res = helpers.bulk(es, actions)
    print("Результат индексации:", response)
except Exception as e:
    print(f"Ошибка индексации: {e}")
print()


