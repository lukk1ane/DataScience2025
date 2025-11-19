import pandas as pd

series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])

add = series1.add(series2, fill_value=0)
sub = series1.sub(series2, fill_value=0)
mul = series1.mul(series2, fill_value=1)
div = series1.div(series2, fill_value=1)

print("Addition:\n", add)
print("Subtraction:\n", sub)
print("Multiplication:\n", mul)
print("Division:\n", div)
