'''
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column
'''

import pandas as pd

df = pd.read_csv('newdata.csv')

x = df['Calories'].mean()
df['Calories'].fillna(x)

y = df['Calories'].median()
df['Calories'].fillna(y)

z = df['Calories'].mode()[0]
df['Calories'].fillna(z,inplace=True)
print(df)
