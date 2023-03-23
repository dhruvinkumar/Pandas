'''
A great aspect of the Pandas module is the corr() method.

The corr() method calculates the relationship between each column in your data set.
'''
import pandas as pd

df = pd.read_csv('newdata.csv')

print(df.corr())

