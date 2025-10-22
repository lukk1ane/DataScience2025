import pandas as pd

data = [10, 20, 30, 40, 50]
indices = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame({'data': data, 'Indices': indices}).set_index('Indices')

print(df)

series = pd.Series([100, 200, 300, 400, 500])
print(series.get(1))


series1 = pd.Series([5, 10, 15, 20])
series2 = pd.Series([2, 4, 6, 8])

series1.index = ['w', 'x', 'y', 'z']
series2.index = ['w', 'x', 'y', 'p']
print(series1.mul(series2, fill_value=1))

print(df.head(3))
print(df.tail(2))

series = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(series.unique())
print(series.value_counts())

df = pd.DataFrame({
    'Item': ['Apple', 'Banana', 'Milk', 'Bread', 'Eggs'],
    'Cost': [100, 50, 20, 15, 30]
})

df['Tax'] = df['Cost'] * 0.1
df['Total'] = df['Cost'] + df['Tax']

print(df[df['Total'] > 50])

df = pd.DataFrame({
    'Product': ['Laptop', 'Headphones', 'Bananas', 'Milk', 'Desk', 'Chair', 'Shampoo', 'Notebook'],
    'Category': ['Electronics', 'Electronics', 'Groceries', 'Groceries', 'Furniture', 'Furniture', 'Personal Care', 'Stationery'],
    'Price': [1200, 150, 1.2, 2.0, 250, 100, 5.5, 3.0],
    'Stock': [10, 50, 200, 150, 5, 20, 100, 300]
})

print(df.isnull())
print(df.notnull())

print(df['Category'].value_counts())

print(df.nlargest(3, 'Price'))
print(df.nsmallest(3, 'Stock'))

print(df.ndim)

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', 'Bob', 'Frank', 'Grace', 'Charlie', 'Alice'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Science', 'Math'],
    'Score': [85, 90, 78, 85, 88, 95, 85, 80, 91, 83, 85],
    'Attendance': [90, 85, 88, 90, 92, 100, 87, 85, 93, 90, 90]
})

duplicated = df.duplicated()
df = df.drop_duplicates()
df.set_index('Student', inplace=True)

print()
print()
print(df.loc['Alice'])
print()
print(df.iloc[[0, 1, 2], 0])

print()
print(df.query('Score > 80 and Attendance > 85'))

print()
print(df[df['Score'].between(70, 90)])