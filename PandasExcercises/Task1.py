import pandas as pd

data = [10,20,30,40,50]
index = ['a','b','c','d','e']
series = pd.Series(data, index = index)
print(series)