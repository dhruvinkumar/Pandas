'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
'''

import pandas as pd

df = pd.read_csv('newdata.csv')


df['Date'] = pd.to_datetime(df['Date']) # formating data

df.dropna(subset=['Date'], inplace = True) # dropping NULL values

print(df)

