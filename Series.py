import pandas as pd

a = [i*2 for i in range(1,4)]

b = pd.Series(a, index = ["x", "y", "z"]) # Series with label

print(a)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

'''
To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
'''
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
