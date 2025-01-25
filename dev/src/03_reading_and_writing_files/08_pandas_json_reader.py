import pandas as pd
from pandas import json_normalize
import pandas.io.json as pd_json
import json

df = pd.read_json('myJSON2.json')
print(df)
print()

df = pd_json.read_json('myJSON2.json')
print(df)
print()

with open('myJSON.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print()
    df = json_normalize(data,record_path='records')
    print(df)
    print()

print(df.head(3).to_json())
print()

print(df.head(3).to_json(orient='records'))


