'''
Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
'''

import pandas as pd

df = pd.read_csv('friends.csv')

# print(df.to_string())  # use to_string() to print the entire DataFrame.


print(df)

pd.options.display.max_rows = 9999

df = pd.read_csv('friends.csv')