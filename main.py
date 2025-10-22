import pandas as pd


#task 1

data1 = [10, 20, 30, 40, 50]
index_labels = ['a', 'b', 'c', 'd', 'e']
series1 = pd.Series(data1, index=index_labels)
print(series1)


#task 2
data2 = [100, 200, 300, 400, 500]
series2 = pd.Series(data2)

# Access the element at position 2 (which is the third element)
access_element= series2[2]

print("Original Series:")
print(series2)
print(f"\nelement at position 2: {access_element}")

example_label = ['Dean', 'Sam', 'Castiel', 'Crowley', 'Kevin']
series2_label = pd.Series(data2, index = example_label)
elements_with_label = series2_label['Crowley']
print("Labeled Series: ")
print(series2_label)
print(f"\nelement with label 'Crowley': {elements_with_label}")

#task 3

data1_1 = [5, 10, 15, 20]
index_labels1_1 = ['w', 'x', 'y', 'z']
series11 = pd.Series(data1_1, index = index_labels1_1)

data2_2 = [2, 4, 6, 8]
index_labels2_2 = ['w', 'x', 'y', 'p']
series22 = pd.Series(data2_2,  index = index_labels2_2)


print(series11 + series22)
print(series11 - series22)
print(series11*series22)
print(series11/series22)



add_series = series11.add(series22, fill_value=0)
print(add_series)

import pandas as pd
import numpy as np

data = {'col1': range(10, 80, 10),
        'col2': list('abcdefg')}
df4 = pd.DataFrame(data)

print("Original DataFrame (Task 4):")
print(df4)
print("\n" + "="*40 + "\n")

print("Displaying the first 3 rows with head(3):")
print(df4.head(3))
print("\n" + "="*40 + "\n")

print("Displaying the last 2 rows with tail(2):")
print(df4.tail(2))
print("\n" + "="*40 + "\n")

print("Displaying the first 5 rows with head() (default):")
print(df4.head())
print("\n" + "="*40 + "\n")

print("Using a negative argument: head(-3) shows all rows EXCEPT the last 3:")
print(df4.head(-3))

#task 5

data = [15, 22, 15, 30, 22, 45, 30, 15]
s5 = pd.Series(data)

print("Original Series (Task 5):")
print(s5)
print("\n" + "="*40 + "\n")

unique_vals = s5.unique()
print(f"Unique values: {unique_vals}")
print("\n" + "="*40 + "\n")
num_unique = s5.nunique()
print(f"Number of unique values: {num_unique}")
print("\n" + "="*40 + "\n")
value_freq = s5.value_counts()
print("Frequency of each value (using value_counts()):")
print(value_freq)

#task6

data = {'Item': ['Keyboard', 'Mouse', 'Monitor', 'Webcam', 'Headset', 'Mousepad'],
        'Cost': [45, 25, 150, 70, 60, 15]}
df6 = pd.DataFrame(data)
print("Original DataFrame (Task 6):")
print(df6)
print("\n" + "="*40 + "\n")
df6['Tax'] = df6['Cost'] * 0.10
df6['Total'] = df6['Cost'] + df6['Tax']
print("DataFrame with 'Tax' and 'Total' columns:")
print(df6)
print("\n" + "="*40 + "\n")
filtered_df6 = df6[df6['Total'] > 50]
print("Filtered DataFrame (Total > 50):")
print(filtered_df6)

#task 7
data = {
    'Product': ['Laptop', 'Tablet', 'Keyboard', 'Monitor', 'Desk Chair', 'Printer', 'External HDD', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Furniture', 'Office', 'Accessories', 'Electronics'],
    'Price': [1200, 450, 75, 300, 150, 200, np.nan, 250],
    'Stock': [30, 50, 120, 40, 25, 15, 80, 5]
}
df7 = pd.DataFrame(data)
print("Original DataFrame (Task 7):")
print(df7)
print("\n" + "="*40 + "\n")

print("Count of missing values per column (isnull().sum()):")
print(df7.isnull().sum())
print("\nCount of non-missing values per column (notnull().sum()):")
print(df7.notnull().sum())
print("\n" + "="*40 + "\n")

print("Count of products in each category:")
print(df7['Category'].value_counts())
print("\n" + "="*40 + "\n")

print("Top 3 most expensive products:")
print(df7.nlargest(3, 'Price'))
print("\n" + "="*40 + "\n")

print("2 products with the lowest stock:")
print(df7.nsmallest(2, 'Stock'))


