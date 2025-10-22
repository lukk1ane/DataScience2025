import pandas as pd

# Task 1
print("Task 1")
data = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']
series_1 = pd.Series(data, labels)
print(series_1)
print("-"*30, "\n")


# Task 2
print("Task 2")
data2 = [100, 200, 300, 400, 500]
series_2 = pd.Series(data2)
print(series_2)
print("At position 2:", series_2.iloc[2],"\n")
labelled = pd.Series(data2, labels)
print(labelled)
print("Element with label 'c':", labelled['c'])
print("-"*30, "\n")


# Task 3
print("Task 3")
Series1 = pd.Series([5, 10, 15, 20], ['w', 'x', 'y', 'z'])
Series2 = pd.Series([2, 4, 6, 8], ['w', 'x', 'y', 'p'])

print("Addition:", "\n")
print(Series1.add(Series2, fill_value=0), "\n")
print("Subtraction:", "\n")
print(Series1.sub(Series2, fill_value=0), "\n")
print("Multiplication:", "\n")
print(Series1.mul(Series2, fill_value=1), "\n")
print("Division:", "\n")
print(Series1.div(Series2, fill_value=1))
print("-"*30, "\n")


# Task 4
print("Task 4")
df1 = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 4, 6, 8, 10]
})
print("First 3 rows:\n")
print(df1.head(3))
print("\nLast 2 rows:\n")
print(df1.tail(2))
print("\nUsing head(-3):\n")
print(df1.head(-2))
print("-"*30, "\n")


# Task 5
print("Task 5")
series_3 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print("Unique values:", series_3.unique())
print("Number of unique values:", series_3.nunique())
print("Value counts:")
print(series_3.value_counts())
print("-"*30, "\n")


# Task 6
print("Task 6")
df2 = pd.DataFrame({
    'Item': ['A', 'B', 'C', 'D', 'E'],
    'Cost': [30, 60, 45, 20, 80]
})
df2['Tax'] = df2['Cost'] * 0.10
df2['Total'] = df2['Cost'] + df2['Tax']
filtered = df2[df2['Total'] > 50]
print("Filtered where Total > 50:\n", filtered)
print("-"*30, "\n")


# Task 7
print("Task 7")
df3 = pd.DataFrame({
    'Product': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Price': [100, 200, 150, 300, 250, 180, 90, 400],
    'Stock': [5, 2, 10, 1, 3, 8, 4, 6]
})

print("Missing values:\n", df3.isnull())
print("\nNumber of products in each category:\n", df3['Category'].value_counts())
print("\nTop 3 most expensive products:\n", df3.nlargest(3, 'Price'))
print("\n2 products with lowest stock:\n", df3.nsmallest(2, 'Stock'))
print("\nShape:", df3.shape)
print("Number of dimensions:", df3.ndim)
print("-"*30, "\n")


# Task 8
print("Task 8")
df4 = pd.DataFrame({
    'Student': ['sandy', 'sponge', 'crab', 'patric', 'squid', 'gary', 'plankton', 'sandy', 'plankton', 'gary'],
    'Subject': ['Math', 'Physics', 'Chemistry', 'Biology', 'Math', 'Chemistry', 'Physics', 'Biology', 'Math', 'Physics'],
    'Score': [85, 90, 75, 88, 92, 70, 80, 78, 89, 60],
    'Attendance': [90, 85, 80, 95, 88, 75, 82, 84, 96, 65]
})

print("Duplicate student names:\n", df4['Student'].duplicated())
print("\nAfter removing duplicates:\n", df4.drop_duplicates(subset='Student', keep='first'))
print("\nSet index to Student:\n", df4.set_index('Student'))

print("\nData for sandy:\n", df4.loc[df4['Student'] == 'sandy'])
print("\nFirst 3 rows:\n", df4.iloc[:3])
print("\nStudents with Score > 80 and Attendance > 85:\n",
      df4.query('Score > 80 and Attendance > 85'))
print("\nStudents with scores between 70 and 90:\n",
      df4[df4['Score'].between(70, 90)])
print("-"*30, "\n")
