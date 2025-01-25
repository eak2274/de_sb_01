import json

with open('myJSON.json', encoding='utf-8') as file:
    data = json.load(file)

print(data)
print()
print(data['records'])
print()
print(data['records'][0]['name'])