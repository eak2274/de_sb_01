import json
from faker import Faker

faker = Faker()

alldata = {'records': []}

for x in range(30):
    data = {
        'name': faker.name(),
        'age':  faker.random_int(min=20, max=80, step=1),
        'street': faker.street_address(),
        'city': faker.city(),
        'state': faker.state(),
        'zip': faker.zipcode(),
        'longitude': float(faker.longitude()),
        'latitude': float(faker.latitude())
    }
    alldata['records'].append(data)

with open('myJSON1.json', mode='w', newline='', encoding='utf-8') as file:
    json.dump(alldata, file)
