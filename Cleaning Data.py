'''
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''

import pandas as pd

df = pd.read_csv('newdata.csv')

new_df = df.dropna() 

# df.dropna(inplace=True) # the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

'''

Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.
'''

df.fillna(130, inplace=True) # all Na present in data

df['Calorie'].fillna(130, inplace=True)

print(df)


