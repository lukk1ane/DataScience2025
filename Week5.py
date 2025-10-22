#Task 1
import pandas as pn
data = [10, 20, 30, 40, 50]
index_labels = ['a', 'b', 'c', 'd', 'e']

series = pn.Series(data, index_labels)
print(series)

#Task 2
list = [100, 200, 300, 400, 500]
series = pn.Series(list)
print(series)
print("Element at position 2: ", series[2])

#Task 3
first = pn.Series([5, 10, 15, 20], index = ['w', 'x', 'y', 'Z'])
second = pn.Series([2, 4, 6, 8], index = ['w', 'x', 'y', 'p'])

add_res = first.add(second, fill_value = 0)
sub_res = first.sub(second, fill_value = 0)
mul_res = first.mul(second, fill_value = 0)
div_res = first.div(second, fill_value = 1)

print("\nAddition:\n", add_res)
print("\nSubtraction:\n", sub_res)
print("\nMultiplication:\n", mul_res)
print("\nDivision:\n", div_res)

#Task 4
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
print("\n")
df = pn.DataFrame(data)

print(df.head(3))
print("\n")
print(df.tail(2))

print("\nhead() default (first 5 rows):\n", df.head())
print("\ntail() default (last 5 rows):\n", df.tail())

print("\nhead(-2) returns all except last 2 rows:\n", df.head(-2))
print("\ntail(-3) returns all except first 3 rows:\n", df.tail(-3))

#Task 5
list = [15, 22, 15, 30, 22, 45, 30, 15]
series = pn.Series(list)

print("Unique: ", series.unique())
print("Number of uniques: ", series.nunique())
print("Frequency: ", series.value_counts())

#Task 6
data = {
    'Item': ['Book', 'Pen', 'Notebook', 'Bag', 'Calculator'],
    'Cost': [40, 5, 15, 60, 50]
}

df = pn.DataFrame(data)
df['Tax'] = df['Cost'] * 0.10
df['Total'] = df['Cost'] + df['Tax']
filtered = df[df['Total'] > 50]
print("\nRows with Total > 50:\n", filtered)

#Task 7
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Chair', 'Desk', 'Printer', 'Webcam'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics', 'Electronics'],
    'Price': [1200, 25, 45, 300, 150, 200, 180, 75],
    'Stock': [10, 150, 100, 20, 50, 30, 15, 60]
}
df = pn.DataFrame(data)

print("\nCheck for missing values using isnull():\n", df.isnull())
print("\nCheck for non-missing values using notnull():\n", df.notnull())

category_counts = df['Category'].value_counts()
top_expensive = df.nlargest(3, 'Price')
lowest_stock = df.nsmallest(2, 'Stock')
df = pn.DataFrame(data)

#Task 8
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eva', 'David', 'Bob', 'Frank', 'Grace', 'Henry'],
    'Subject': ['Math', 'Science', 'English', 'History', 'Math', 'Science', 'Math', 'English', 'History', 'Math'],
    'Score': [85, 92, 78, 88, 95, 67, 80, 74, 89, 90],
    'Attendance': [90, 85, 88, 92, 95, 80, 87, 75, 93, 88]
}

df = pn.DataFrame(data)

duplicates = df.duplicated(subset='Student', keep=False)
df_no_duplicates = df.drop_duplicates(subset='Student', keep='first')
df_indexed = df.set_index('Student')
alice_data = df_indexed.loc['Alice']
first_three = df.iloc[:3]
high_performers = df.query('Score > 80 and Attendance > 85')
scores_70_90 = df[df['Score'].between(70, 90)]