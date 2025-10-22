import pandas as pd

# Task 1

data = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, labels)
print(series)

# Task 2

series_2 = pd.Series([100, 200, 300, 400, 500])
second = series_2[1]
series_2.index = ['x1', 'x2', 'x3', 'x4', 'x5' ]
print(series_2)

# Task 3

series_1_v = [5, 10, 15, 20]
labels_1 = ['w', 'x', 'y', 'z']
series_1 = pd.Series(series_1_v, labels_1)
series_2_v = [2, 4, 6, 8]
labels_2 = ['w', 'x', 'y', 'p']
series_2 = pd.Series(series_2_v, labels_2)
sum_of_series = series_1 + series_2
diff = series_1 - series_2
product = series_1 * series_2
division = (series_1 / series_2).fillna(0)
print(division)

# Task 4

data = {
    'name': ['anita', 'tatuli', 'guga', 'cucqa', 'rezi'],
    'gpa': [10,10,10,10,10,]
}

dataframe = pd.DataFrame(data)
print(dataframe.head(3))
print(dataframe.tail(2))

# Task 5
series = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(series.unique())
print(series.nunique())
print(series.value_counts())

# Task 6

data = {
    'item': ['anita', 'tatuli', 'guga', 'cucqa', 'rezi'],
    'cost': [10, 10, 10, 10, 10]
}

dataframe = pd.DataFrame(data)
dataframe['tax'] = dataframe['cost'] * 0.1
dataframe['total'] = dataframe['cost'] + dataframe['tax']
mask = dataframe['total'] > 10
print(dataframe[mask])

# Task 7

data = {
    'Product': ['anita', 'tatuli', 'guga', 'cucqa', 'rezi', 'fxaka', 'davita', 'toko'],
    'Category': ['top','top','top', 'mid','mid','mid','low', 'low'],
    'Price': [100, 103, 30, 20, 140, 34, 32, 43],
    'Stock': [10, 10, 10, 10, 10, 8, 9, 19]
}

dataframe = pd.DataFrame(data)
print(dataframe.notnull)
print(dataframe.isnull)
print(
    dataframe.value_counts('Category')
)
print(
    dataframe.nlargest(1, 'Price')
)
print(
    dataframe.nsmallest(2, 'Stock')
)
print(dataframe.ndim, dataframe.shape)

# Task 8

data = {
    'Student': ['anita', 'tatuli', 'guga', 'cucqa', 'rezi', 'fxaka', 'davita', 'toko', 'anita', 'tatuli'],
    'Subject': ['math', 'law', 'cs', 'business', 'math','math','math','math', 'cs', 'cs'],
    'Score':  [10, 10, 10, 10, 10, 8, 9, 19,10,10],
    'Attendance': [100, 103, 30, 20, 140, 34, 32, 43, 100, 100],
}

df = pd.DataFrame(data)
print(df)

print(df.duplicated(subset='Student', keep=False))

df_unique = df.drop_duplicates(subset='Student', keep='first')
print(df_unique)

df_indexed = df_unique.set_index('Student')
print(df_indexed)

print(df_indexed.loc['Alice'])

print(df_indexed.iloc[:3])

print("\nStudents with Score > 80 and Attendance > 85:")
print(df_indexed.query("Score > 80 and Attendance > 85"))

print("\nStudents with Score between 70 and 90:")
print(df_indexed[df_indexed['Score'].between(70, 90)])
