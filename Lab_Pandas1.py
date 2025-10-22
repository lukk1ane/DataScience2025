import pandas as pd
import numpy as np

# Task 1
data = [10, 20, 30, 40, 50]
custom_index = ['a', 'b', 'c', 'd', 'e']
data_with_indices = pd.Series(data, index = custom_index)
print(data_with_indices)

# Task 2
series = [100, 200,300, 400, 500]
pd_series = pd.Series(series)
print(pd_series.iloc[2])

# Task 3
series1 = [5, 10, 15, 20, np.nan]
series2 = [2, 4, 6, 8, np.nan]
index1 = ['w', 'x', 'y', 'z', 'nan']
index2 = ['w', 'x', 'y', 'p', 'nan']
series_a = pd.Series(series1, index = index1)
series_b = pd.Series(series2, index = index2)
addition = series_a.add(series_b, fill_value=0)
substraction = series_a.sub(series_b, fill_value=0)
multiplication = series_a.mul(series_b, fill_value=0)
print(f"addition: {addition}, substraction:{substraction}, multiplication: {multiplication}")

# Task 4
data = {
    'Name': ['Ana', 'Eka', 'Mariami', 'Giokezo'],
    'Age': [25, 30, 22, 35],
    'City': ['budapest', 'kutaisi', 'tbilisi', 'blabla']
}
df = pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))

# Task 5
task_5 = [15, 22,15, 30, 22, 45, 30, 15]
task_5_pd = pd.Series(task_5)
unique_amt = task_5_pd.nunique()
values = task_5_pd.value_counts()
print((unique_amt, values))

# Task 6
data1 = {
    'items': ['Ana', 'Eka', 'Mariami', 'Giokezo', 'Semi'],
    'cost': [25, 30, 22, 35, 130],
}
df_1 = pd.DataFrame(data1)
df_1['Tax'] = df_1['cost'] / 10
df_1['Total'] = df_1['cost'] + df_1['Tax']
filter_df_1 = df_1[df_1['Total']>50]
print(filter_df_1)

# Task 7
data2 = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse", "Speaker", "Smartwatch"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [1200, 800, 150, 300, 50, 40, 200, 250],
    "Stock": [15, 30, 50, 20, 100, 80, 25, 10]
}

df2 = pd.DataFrame(data2)

missing_vals = df2.isnull()
print(missing_vals)
category_amt = df2['Category'].value_counts()
print(category_amt)
most_expensive = df2['Price'].nlargest(3)
print(most_expensive)
lowest_stock = df2['Stock'].nsmallest(2)
print(lowest_stock)
print(df2.shape)
print(df2.ndim)

# Task 8
data3 = {
    "student": ["Alice", "Bob", "Charlie", "Alice", "Bob",
                "David", "Emma", "Charlie", "Fiona", "George", "Emma", "David"],
    "subject": ["Math", "Science", "English", "Science", "Math",
                "English", "Math", "Science", "English", "Math", "English", "Science"],
    "score": [85, 78, 92, 88, 74, 81, 90, 89, 76, 67, 93, 82],
    "attendance": [92, 88, 95, 91, 85, 87, 97, 94, 83, 80, 96, 88]
}

df3 = pd.DataFrame(data3)
print(df3)

duplicates = df3.duplicated(subset='student')
print(duplicates)

df3_cleaned = df3.drop_duplicates(subset='student')
print(df3_cleaned)

df3_indexed = df3.set_index('student')
print(df3_indexed)

print(df3_indexed.loc['Bob'])

print(df3.iloc[2,2])

query_use = df3.query('score > 80 and attendance > 85')
print(query_use)

between_use = df3[df3['score'].between(70, 90, inclusive= 'neither')]['student']
print(between_use)