import pandas as pd
# #Task 1
# data = [10,20,30,40,50]
# index_label = ['A','B','C','D','E']
# series = pd.Series(data, index=index_label)
# print(series)

# #Task2
# data = [100, 200, 300, 400, 500]
# df = pd.DataFrame({"column1": data, "column2": data})
# print(df)

# #Task 3
# Series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
# Series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])

# print("Series 1:")
# print(Series1)
# print("Series 2:")
# print(Series2)

# Addition = Series1 + Series2
# Subtraction = Series1 - Series2
# Multiplication = Series1 * Series2
# Division = Series1 / Series2

# Addition_Handled = Series1.add(Series2, fill_value=0)
# Subtraction_Handled = Series1.sub(Series2, fill_value=0)
# Multiplication_Handled = Series1.mul(Series2, fill_value=1)
# Division_Handled = Series1.div(Series2, fill_value=1)

# print("\n--- Arithmetic with NaN Handled ---")
# print("Addition (fill_value=0):\n", Addition_Handled)
# print("Subtraction (fill_value=0):\n", Subtraction_Handled)
# print("Multiplication (fill_value=1):\n", Multiplication_Handled)
# print("Division (fill_value=1):\n", Division_Handled)

# #Task 4
# data = {
#     'Product': ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Speaker'],
#     'Sales': [15000, 7500, 2000, 1500, 3000, 4500],
#     'Region': ['North', 'South', 'East', 'West', 'Central', 'North']
# }
# df = pd.DataFrame(data)

# print("Original DataFrame")
# print(df)

# print("First 3 rows")
# print(df.head(3))

# print(" Last 2 rows")
# print(df.tail(2))

# print(" Default (First 5 rows)")
# print(df.head())

# print("Default (Last 5 rows)")
# print(df.tail())

# print(" All rows EXCEPT the last 2 ")
# print(df.head(-2))

# print("All rows EXCEPT the first 4 ")
# print(df.tail(-4))

# #Task 5
# data = [15, 22, 15, 30, 22, 45, 30, 15]
# s = pd.Series(data)

# print("Unique Values ")
# print(s.unique())

# print("Count of Unique Values ")
# print(s.nunique())

# print("Frequency of Each Value")
# print(s.value_counts())

# #Task 6
# data = {
#     'Item': ['Book', 'Laptop', 'Coffee Maker', 'Headphones', 'Jacket', 'Monitor'],
#     'Cost': [25.00, 1200.00, 45.00, 80.00, 55.00, 350.00]
# }
# df = pd.DataFrame(data)

# print("Initial DataFrame")
# print(df)

# df['Tax'] = df['Cost'] * 0.10

# df['Total'] = df['Cost'] + df['Tax']

# print(" DataFrame with Tax and Total Columns")
# print(df)

# filtered_df = df[df['Total'] > 50]

# print(" Rows where Total is Greater than 50 ")
# print(filtered_df)

# #Task 7
# data = {
#     'Product': ['T-Shirt', 'Jeans', 'Sneakers', 'Blender', 'Microwave', 'Book', 'Pencil', 'Mug', 'Sofa', 'Lamp'],
#     'Category': ['Apparel', 'Apparel', 'Apparel', 'Kitchen', 'Kitchen', 'Media', 'Media', 'Home', 'Home', 'Home'],
#     'Price': [25.99, 59.99, 79.99, 49.99, 129.99, 15.50, 2.00, 10.00, 750.00, 35.00],
#     'Stock': [150, 80, 45, 120, 30, 200, 500, 90, 10, 65]
# }
# df = pd.DataFrame(data)

# df.loc[3, 'Price'] = np.nan
# df.loc[6, 'Stock'] = np.nan

# print("Original DataFrame")
# print(df)

# print("Check for missing values ")
# print(df.isnull())

# print("\n--- notnull(): Check for non-missing values ")
# print(df.notnull())

# print("\n--- value_counts() on Category ---")
# print(df['Category'].value_counts())

# print("\n--- nlargest(3) - Top 3 most expensive products ---")
# print(df.nlargest(3, 'Price'))

# print("\n--- nsmallest(2) - 2 products with lowest stock ---")
# print(df.nsmallest(2, 'Stock'))

# print("\n--- DataFrame Shape (Rows, Columns) ---")
# print(df.shape)

# print("\n--- DataFrame ndim (Number of Dimensions) ---")
# print(df.ndim)

