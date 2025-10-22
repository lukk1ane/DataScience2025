import pandas as pd

s = pd.Series([100,200,300,400,500])
print(s.iloc[2])

s2 = pd.Series([100,200,300,400,500], index=['p', 'q', 'r', 's', 't'])
print(s2['r'])