import pandas as pd
 
# Create a Pandas Series from a list of data with custom labels
data = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=labels)
print("Pandas Series:")
print(series)

# Accessing elements using both integer index and label-based index
data=[100, 200, 300, 400, 500]
series_el2=pd.Series(data).iloc[1]
print("\nElement at index 2 of the Series: ", series_el2)

series_el2_with_labled_index=pd.Series(data, index=['a', 'b', 'c', 'd', 'e']).loc['b']
print("\nElement with label 'b' of the Series:", series_el2_with_labled_index)    

# Performing arithmetic operations between two Series with different indices, handling missing data
Series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
Series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])

add = Series1.add(Series2, fill_value=0)
sub = Series1.sub(Series2, fill_value=0)
mul = Series1.mul(Series2, fill_value=0)
div = Series1.div(Series2, fill_value=1)

print("Addition:\n", add)
print("\nSubtraction:\n", sub)
print("\nMultiplication:\n", mul)
print("\nDivision:\n", div)

# Create a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
}

dataframe=pd.DataFrame(data)

first3row=dataframe.head(3)
print("\nFirst 3 rows of the DataFrame:\n", first3row)

last2row=dataframe.tail(2)
print("\nLast 2 rows of the DataFrame:\n", last2row)

default=dataframe.head()
print("\nDataFrame with default index:\n", default)

negativeindx=dataframe.head(-1)
print("\nDataFrame with negative index:\n", negativeindx) #shows all rows except the last one


#unique values and their counts in a Series
Series=pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
unique_values=Series.unique()
print("\nUnique values in the Series:\n", unique_values)

count_freq=Series.value_counts()
print("\nCount of unique values in the Series:\n", count_freq)



# DataFrame Manipulation: Adding new columns, performing calculations, and filtering data
data={
    'item':['Apple', 'Banana', 'Orange', 'strawberry', 'Banana'],
    'cost':[15, 150, 4, 5, 24]
}

df=pd.DataFrame(data)

df['tax']=df['cost']*0.1
df['total']=df['cost']+df['tax']
filtered_data=df[df['total']>50]
print("\nFiltered DataFrame with total cost greater than 50:\n", filtered_data)


data={
    'product':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'category':['Electronics', 'Furniture', 'Garden', 'Clothing', 'Gadgets', 'Gaming', 'Stationery', 'Travel'],
    'price':[250, 450, 150, 80, 300, 60, 400, 500],
    'stock':[50, 20, 80, 100, 30, 150, 40, 10],
}

df=pd.DataFrame(data)
# Use isnull() and notnull() to check for missing values
print("Missing values:\n", df.isnull())
print("\nNon-missing values:\n", df.notnull())

# • Use value_counts() on the Category column to count products in each category
categorycount =df['category'].value_counts()
print("\nProduct count in each category:\n", categorycount)

# • Use nlargest() to find the top 3 most expensive products
most_expensive=df.nlargest(3, 'price')
print("\nTop 3 most expensive products:\n", most_expensive)

# • Use nsmallest() to find the 2 products with the lowest stock
lowest_stock=df.nsmallest(2, 'stock')
print("\n2 products with the lowest stock:\n", lowest_stock)

# • Display the shape and ndim of the DataFrame
print("\nDataFrame Shape:", df.shape)
print("DataFrame Dimensions:", df.ndim)



# Create a DataFrame from a dictionary of lists
data = {
    'Student': ['Ana', 'Luka', 'Nino', 'Ana', 'Saba', 'Nika', 'Luka', 'Gio', 'Nino', 'Tako'],
    'Subject': ['Math', 'Science', 'History', 'English', 'Math', 'Art', 'History', 'Science', 'Math', 'PE'],
    'Score': [85, 90, 75, 88, 60, 95, 70, 82, 78, 65],
    'Attendance': [90, 95, 80, 92, 70, 98, 85, 88, 84, 60]
}
df=pd.DataFrame(data)

# Use duplicated() to identify duplicate student names
print("Duplicate student names:\n", df[df.duplicated('Student')]['Student'])
    
# • Use drop_duplicates() to remove duplicate student names keeping the first occurrence
unique_students = df.drop_duplicates('Student', keep='first')
print("\nDataFrame after removing duplicate student names:\n", unique_students)

# • Use set_index() to set Student as the index
df_indexed = df.set_index('Student')

# • Use loc[] to retrieve data for a specific student
print("\nData for student 'Ana':\n", df_indexed.loc['Ana'])

# • Use iloc[] to retrieve the first 3 rows
print("\nFirst 3 rows of the DataFrame:\n", df_indexed.iloc[:3])

# • Use query() method to find students with Score greater than 80 and Attendance greater than 85
high_score=df.query('Score > 80 and Attendance > 85')

# • Use between() to find students with scores between 70 and 90
score_between = df[df['Score'].between(70, 90)]