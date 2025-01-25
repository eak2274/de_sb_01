import pandas as pd

df = pd.read_csv('myCSV.csv')
print(df)
print()
df = pd.read_csv('myCSV.csv',header=None,names=['little_name','little_age'],skiprows=1)
print(df)
print()

#df1 = pd.read_csv('myCSV2.csv')
#print(df1.head(10))