import pandas as pd

a = [i*2 for i in range(1,4)]

a = pd.Series(a, index = ["x", "y", "z"])

print(a)