import pandas as pd

# Task 1

df = pd.DataFrame(
    [10, 20, 30, 40, 50],
    index = ['a', 'b', 'c', 'd', 'e']
)

print(df)

# Task 2

df = pd.DataFrame(
    {
        '1': 100,
        '2': 200,
        '3': 300,
        '4': 400,
        '5': 500
     },
    index = ['a', 'b', 'c', 'd', 'e']
)

print(df.loc['b'])

df.index = ['a', 'b', 'c', 'd', 'e']

print(df)

# Task 3

series1 = pd.Series([5, 10, 15, 20], index = ['w', 'x', 'y', 'z'])
series2 = pd.Series([2, 4, 6, 8], index = ['w', 'x', 'y', 'p'])

series_sum = series1 + series2
series_sum = series_sum.dropna()
print(series_sum)

series_sub = series1 - series2
series_sub = series_sub.dropna()
print(series_sub)

series_mult = series1 * series2
series_mult = series_mult.dropna()
print(series_mult)

series_div = series1 / series2
series_div = series_div.dropna()
print(series_div)

# Task 4

df = pd.DataFrame(
    [10, 20, 30, 40, 50],
    index = ['a', 'b', 'c', 'd', 'e']
)

print(df.head(3))
print(df.tail(2))

# Task 5

series = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
ans = series.nunique()
print(ans)

val_counts = series.value_counts()
print(val_counts)

# Task 6

df = pd.DataFrame(
    [[1, 20], [3, 40], [5, 60], [7, 80], [9, 100]],
    index = ['a', 'b', 'c', 'd', 'e'],
    columns = ['Items', 'Cost']
)

print(df)

df = df.assign(Tax = lambda df: df.Cost * 0.1)
df = df.assign(Total = lambda df: df.Tax + df.Cost)
print(df)

# Task 7

df = pd.DataFrame(
    [
        [1, 1, 100, 20],
        [2, 2, 200, 10],
        [3, 3, 300, 50],
        [4, 4, 400, 30],
        [5, 5, 600, 50],
        [6, 6, 800, 50],
        [7, 7, 800, 50],
        [8, 8, 900, 50],
    ],
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['Product', 'Category', 'Price', 'Stock']
)

df.isnull()
df.notnull()
df = df.dropna()

print(df.value_counts())

print(df.nlargest(3, columns=['Product', 'Category', 'Price']))
print(df.nsmallest(2, columns=['Product', 'Category', 'Stock']))

print(df)
print(df.shape)
print(df.ndim)

# Task 8

students = pd.DataFrame(
    [
        [1, 1, 100, 70],
        [2, 2, 200, 50],
        [3, 3, 300, 100],
        [4, 4, 400, 80],
        [5, 5, 600, 80],
        [6, 6, 800, 80],
        [7, 7, 800, 80],
        [8, 8, 900, 80],
        [2, 2, 200, 40],
        [1, 1, 100, 20]
    ],
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    columns = ['Student', 'Subject', 'Score', 'Attendance']
)

students.duplicated(subset=['Student', 'Subject'], keep=False)
students = students.drop_duplicates()

print(students.set_index('Student', inplace=True))
print(students.loc[:, ['Subject']])
print(students.iloc[:3])
print(students.query("Score >= 80 & Attendance > 85"))
print(students[students['Score'].between(70, 90)])

print(students)

