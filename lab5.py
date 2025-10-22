import pandas as pd

# Task 1
print("===Task 1===")

data1 = [10, 20, 30, 40, 50]
index_labels = ['a', 'b', 'c', 'd', 'e']

series_t1 = pd.Series(data1, index=index_labels)

print(series_t1)

# Task 2
print("===Task 2===")

data2 = [100, 200, 300, 400, 500]
series_t2 = pd.Series(data2)

element_pos2 = series_t2.iloc[2]
print("Element at position 2:", element_pos2)

labels = ['a', 'b', 'c', 'd', 'e']
series_labelled = pd.Series(data2, index=labels)

element_label_c = series_labelled['c']  # using label
print("Element with label 'c':", element_label_c)
print()

print("Labelled Series:")
print(series_labelled)

# Task 3
print("===Task 3===")

series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])

# Addition (fill NaN with 0 to avoid NaN in result)
add_result = series1.add(series2, fill_value=0)

# Subtraction (fill NaN with 0 to avoid NaN in result)
sub_result = series1.sub(series2, fill_value=0)

# Multiplication (fill NaN with 0 to avoid NaN in result)
mul_result = series1.mul(series2, fill_value=0)

# Division (fill NaN with 1 to avoid Nan in result and division by 0)
div_result = series1.div(series2, fill_value=1)

# Display results
print("Addition:\n", add_result)
print("\nSubtraction:\n", sub_result)
print("\nMultiplication:\n", mul_result)
print("\nDivision:\n", div_result)

# Task 4
print("===Task 4===")

data4 = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [22, 30, 35, 40, 28],
    'Country': ['Georgia', 'Germany', 'Italy', 'Portugal', 'Austria']
}

df4 = pd.DataFrame(data4)

# Display first 3 rows using head()
print("First 3 rows using head(3):")
print(df4.head(3))
print()

# Display last 2 rows using tail()
print("Last 2 rows using tail(2):")
print(df4.tail(2))
print()

# Using head() with default value (default is 5)
print("First rows using head() with default:")
print(df4.head())
print()

# Using tail() with default value (default is 5)
print("Last rows using tail() with default:")
print(df4.tail())
print()

# Using negative arguments
print("Using head(-2) to exclude last 2 rows:")
print(df4.head(-2))
print()

print("Using tail(-3) to exclude first 3 rows:")
print(df4.tail(-3))
print()

# task 5
print("===Task 5===")

data5 = [15, 22, 15, 30, 22, 45, 30, 15]
series5 = pd.Series(data5)

# Find unique values
unique_values = series5.unique()
print("Unique values:", unique_values)

# Count number of unique values
num_unique = series5.nunique()
print("Number of unique values:", num_unique)

# Frequency of each value
value_frequencies = series5.value_counts()
print("\nFrequency of each value:")
print(value_frequencies)

# task 6
print("===Task 6===")

data6 = {
    'Item': ['A', 'B', 'C', 'D', 'E'],
    'Cost': [30, 55, 40, 5, 60]
}

df6 = pd.DataFrame(data6)

# Add Tax column (10% of Cost)
df6['Tax'] = df6['Cost'] * 0.10

# Add Total column (Cost + Tax)
df6['Total'] = df6['Cost'] + df6['Tax']

# Filter rows where Total > 50
filtered_df = df6[df6['Total'] > 50]

# Display results
print("Complete DataFrame:\n", df6)
print("\nRows where Total > 50:\n", filtered_df)

# task 7
print("===Task 7===")

data7 = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer', 'Desk', 'Chair', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'Price': [1200, 25, 45, 300, 150, 200, 120, 80],
    'Stock': [10, 50, 30, 15, 5, 8, 12, 25]
}

df7 = pd.DataFrame(data7)

# Check for missing values
print("Check for missing values using isnull():\n", df7.isnull())
print("\nCheck for not null values using notnull():\n", df7.notnull())

# Count products in each category
category_counts = df7['Category'].value_counts()
print("\nNumber of products in each category:\n", category_counts)

# Top 3 most expensive products
top3_expensive = df7.nlargest(3, 'Price')
print("\nTop 3 most expensive products:\n", top3_expensive)

# 2 products with the lowest stock
lowest2_stock = df7.nsmallest(2, 'Stock')
print("\n2 products with lowest stock:\n", lowest2_stock)

# Display shape and ndim
print("\nShape of DataFrame:", df7.shape)
print("Number of dimensions (ndim):", df7.ndim)

# task 8
print("===Task 8===")

data8 = {
    'Student': ['A', 'B', 'C', 'A', 'E', 'B', 'F', 'G', 'H', 'I'],
    'Subject': ['Math', 'Math', 'Math', 'English', 'Math', 'English', 'Math', 'Math', 'English', 'Math'],
    'Score': [85, 78, 92, 88, 95, 82, 67, 74, 89, 91],
    'Attendance': [90, 80, 95, 88, 92, 85, 75, 70, 87, 93]
}

df8 = pd.DataFrame(data8)
print("Original DataFrame:\n", df8)

# Identify duplicate student names
duplicates = df8['Student'].duplicated()
print("\nDuplicate student names:\n", duplicates)

# Remove duplicate student names (keep first occurrence)
df_no_duplicates = df8.drop_duplicates(subset='Student', keep='first')
print("\nDataFrame after removing duplicate student names:\n", df_no_duplicates)

# Set 'Student' as index
df_indexed = df8.set_index('Student')
print("\nDataFrame with 'Student' as index:\n", df_indexed)

# Retrieve data for a specific student using loc[]
student_data = df_indexed.loc['A']
print("\nData for student A:\n", student_data)

# Retrieve first 3 rows using iloc[]
first3_rows = df8.iloc[:3]
print("\nFirst 3 rows using iloc:\n", first3_rows)

# Use query() to find students with Score > 80 and Attendance > 85
high_perf_students = df8.query('Score > 80 & Attendance > 85')
print("\nStudents with Score > 80 and Attendance > 85:\n", high_perf_students)

# Use between() to find students with scores between 70 and 90
score_between = df8[df8['Score'].between(70, 90)]
print("\nStudents with scores between 70 and 90:\n", score_between)
