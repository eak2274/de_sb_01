from elasticsearch import Elasticsearch
import pandas as pd
from pandas import json_normalize
import pandas.io.json as pd_json
import json

es = Elasticsearch(
    hosts=["http://localhost:9200"]
)

# 01. select all
doc = {
        "size": 10,
        "query": {"match_all": {}}
}
res = es.search(index="users",body=doc)

print(res['hits']['hits'])
print()

# 02. select all, print out nicely
for doc in res['hits']['hits']:
    print(doc['_source'])
print()

# 03. select all through pandas
df = json_normalize(res['hits']['hits'])
print(df)
print()

# 04. select one by name
doc = {
        "size": 10,
        "query": {"match":
                      {
                        "name": "Robert Lawrence"
                      }
        }
}
res=es.search(index="users",body=doc)
print(res['hits']['hits'][0]['_source'])
print()

# 05. select one by name, another way
res=es.search(index="users", q="name:Megan Mercado", size=10)
print(res['hits']['hits'][0]['_source'])
print()

# 06. select two by criteria
doc = {
        "size": 10,
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "city": "Lake"
                    }
                }
            }
        }
}
res = es.search(index="users", body=doc)
for rec in res['hits']['hits']:
    print(rec['_source'])
print()

# 07. select one by adjusted criteria
doc = {
        "size": 10,
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "city": "Lake"
                    }
                },
                "filter": {
                    "term": {
                        "zip": "78914"
                    }
                }
            }
        }
}
res = es.search(index="users", body=doc)
for rec in res['hits']['hits']:
    print(rec['_source'])
print()