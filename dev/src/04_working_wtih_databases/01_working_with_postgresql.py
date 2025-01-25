import psycopg2 as db
from faker import Faker
import pandas as pd
import json

conn_string="dbname='de_sandbox_db' host='158.178.129.197' user='de_sandbox_user' password='desb180125'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "insert into users (name,street,city,zip) values('{}','{}','{}','{}')" \
        .format('Big Bird','Sesame Street','Fakeville','12345')
print(cur.mogrify(query).decode())
cur.execute(query)

query2 = "insert into users (name,street,city,zip) values(%s,%s,%s,%s)"
data2=('Big Bird','Sesame Street','Fakeville','12345')
print('\n' + cur.mogrify(query2,data2).decode())
cur.execute(query2, data2)
print()

query3 = "insert into users (name,street,city,zip) values(%s,%s,%s,%s)"
fake=Faker()
data3=[]
for _ in range(5):
   data3.append((fake.name(),fake.street_address(),fake.city(),fake.zipcode()))
data_for_db=tuple(data3)
print(data3)
print()
print(data_for_db)
print()
print(data_for_db[1])
print()
print('\n' + cur.mogrify(query3,data_for_db[1]).decode())
cur.executemany(query3,data_for_db)
print()

conn.commit()

query4 = "select * from users"
cur.execute(query4)
for record in cur:
    print(record)
print()

query5 = "select * from users"
cur.execute(query5)
records = cur.fetchall()
print(cur.rownumber)
print()
for record in records:
    print(record)
print()

query7 = "select * from users"
cur.execute(query7)
record = cur.fetchone()
print(record)
print()
print(cur.rowcount)
print()
print(cur.rownumber)
print()

query8 = "select * from users"
cur.execute(query8)
records = cur.fetchall()
f = open('fromdb.csv', 'w')
cur.copy_to(f,'users',sep=',')
f.close()
print()

query9 = "select * from users"
cur.execute(query9)
records = cur.fetchall()
# Извлечение названий столбцов
column_names = [desc[0] for desc in cur.description]
f = open('fromdb.csv', 'w')
# Записываем названия столбцов в первую строку
f.write(','.join(column_names) + '\n')
cur.copy_to(f,'users',sep=',')
f.close()
print()

query10 = "select * from users"
df = pd.read_sql(query10, conn)
print(df)
print()
json_data = df.to_json(orient='records')
print(json_data)
with open('myJSON1.json', mode='w', newline='', encoding='utf-8') as file:
    file.write(json_data)

# Закрытие соединения
cur.close()
conn.close()