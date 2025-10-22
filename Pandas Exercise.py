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
print("Value counts:\n", series_3.value_counts(), "\n")
