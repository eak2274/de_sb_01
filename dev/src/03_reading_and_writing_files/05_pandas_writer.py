import pandas as pd

df = pd.DataFrame(columns=['big_name', 'big_age'], data=[['Ivan', 40], ['Piotr', 50]])
print(df)
print()

df = pd.DataFrame({'big_name': ['Ivan', 'Piotr'], 'big_age': [40, 50]})
print(df)

df.to_csv('myCSV3.csv', index=False)