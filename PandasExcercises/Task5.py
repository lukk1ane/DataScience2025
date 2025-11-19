import pandas as pd

s = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])

print("Unique values:", s.unique())
print("Number of unique values:", s.nunique())
print("Value counts:\n", s.value_counts())
