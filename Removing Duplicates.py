import pandas as pd

df = pd.read_csv('newdata.csv')

print(df.duplicated())

df.drop_duplicates(inplace=True)

print(df)