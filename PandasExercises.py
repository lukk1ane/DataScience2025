import numpy as np
import pandas as pd


#Task1
task1 = pd.Series([10, 20, 30, 40, 50],['a', 'b', 'c', 'd', 'e'])

#Task2
task2 = pd.Series([100, 200, 300, 400, 500])
task2.index = 'a b c d e'.split()



#Task3
Series1 = pd.Series([5, 10, 15, 20],['w', 'x', 'y', 'z'])
Series2 = pd.Series([2, 4, 6, 8], ['w', 'x', 'y', 'p'])

addition = Series1.add(Series2, fill_value=0)
subtraction = Series1.sub(Series2, fill_value=0)
multiplication = Series1.mul(Series2, fill_value=1)
division = Series1.div(Series2, fill_value=1)


#Task4
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}
df = pd.DataFrame(data)
df.head(3)
df.tail(2)


#Task5
task5 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
unique_values = task5.unique()
number_of_unique_values = task5.nunique()
frequency = task5.value_counts()


#Task6
data = {
    'Item': ['Pen', 'Notebook', 'Eraser', 'Pencil', 'Marker'],
    'Cost': [40, 60, 5, 35, 10]
}
df = pd.DataFrame(data)
df['Tax'] = df['Cost']/10
df['Total'] = df['Cost'] + df['Tax']
filtered = df[df['Total'] > 50]


#Task7
data = {
    'Product': ['Laptop', 'Smartphone', 'Headphones', 'Desk', 'Chair', 'Monitor', 'Keyboard', 'Mouse'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [1200, 800, 150, 300, 150, 250, 100, 50],
    'Stock': [10, 25, 50, 15, 20, 30, 40, 60]
}

df = pd.DataFrame(data)

df.isnull()
df.notnull()
df['Category'].value_counts()
df.nlargest(3, 'Price')
df.nsmallest(2, 'Stock')


#Task8

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eva', 'Bob', 'Frank', 'Charlie', 'George'],
    'Subject': ['Math', 'Science', 'Math', 'English', 'Math', 'Science', 'Math', 'English', 'Science', 'Math'],
    'Score': [85, 90, 78, 92, 88, 95, 84, 75, 80, 89],
    'Attendance': [90, 95, 85, 92, 88, 97, 90, 80, 87, 93]
}
df = pd.DataFrame(data)

df['Student'].duplicated()
df['Student'].drop_duplicates()
df.set_index(df['Student'], inplace=True)
alice_info = df.loc['Alice']
info = df.iloc[:3]
df.query('Score > 80 and Attendance > 85')
between_scores = df[df['Score'].between(70,80)]




