import pandas as pd

# Task 1
s1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s1)

# Task 2
s2 = pd.Series([100, 200, 300, 400, 500])
print(s2.iloc[2])
print(s1.loc['c'])

# Task 3
series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])
add_res = series1.add(series2, fill_value=0)
sub_res = series1.sub(series2, fill_value=0)
mul_res = series1.mul(series2, fill_value=0)
div_res = series1.div(series2, fill_value=0)
print(add_res)
print(sub_res)
print(mul_res)
print(div_res)

# Task 4
_df4 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6],
    'B': [10, 20, 30, 40, 50, 60],
    'C': list('abcdef')
})
print(_df4.head(3))
print(_df4.tail(2))
print(_df4.head())
print(_df4.head(-2))
print(_df4.tail())
print(_df4.tail(-3))

# Task 5
s5 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(s5.unique())
print(s5.nunique())
print(s5.value_counts())

# Task 6
_df6 = pd.DataFrame({
    'Item': ['Pen', 'Notebook', 'Bottle', 'Bag', 'Calculator'],
    'Cost': [12.5, 35.0, 22.0, 55.0, 48.0]
})
_df6['Tax'] = _df6['Cost'] * 0.10
_df6['Total'] = _df6['Cost'] + _df6['Tax']
print(_df6)
print(_df6[_df6['Total'] > 50])

# Task 7
_df7 = pd.DataFrame({
    'Product': ['Phone', 'Laptop', 'Tablet', 'Mouse', 'Keyboard', 'Monitor', 'Charger', 'Headset'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Accessories'],
    'Price': [699, 1299, 399, 25, 49, 219, 19, 89],
    'Stock': [50, 20, 35, 200, 150, 40, 300, 80]
})
print(_df7.isnull())
print(_df7.notnull())
print(_df7['Category'].value_counts())
print(_df7.nlargest(3, 'Price'))
print(_df7.nsmallest(2, 'Stock'))
print(_df7.shape)
print(_df7.ndim)

# Task 8
_df8 = pd.DataFrame({
    'Student': ['Ana', 'Nika', 'Ana', 'Luka', 'Saba', 'Mariam', 'Nika', 'Dato', 'Sandro', 'Ana'],
    'Subject': ['Math', 'Physics', 'Chemistry', 'Math', 'Biology', 'Physics', 'Math', 'Chemistry', 'Biology', 'Physics'],
    'Score': [92, 76, 85, 88, 67, 91, 82, 73, 89, 95],
    'Attendance': [90, 84, 88, 92, 75, 95, 86, 80, 93, 97]
})
print(_df8.duplicated(subset=['Student']))
print(_df8.drop_duplicates(subset=['Student'], keep='first'))
_df8_indexed = _df8.set_index('Student')
print(_df8_indexed)
print(_df8_indexed.loc['Ana'])
print(_df8_indexed.iloc[:3])
print(_df8.query('Score > 80 and Attendance > 85'))
print(_df8[_df8['Score'].between(70, 90)])
