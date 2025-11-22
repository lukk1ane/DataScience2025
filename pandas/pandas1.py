import pandas as pd

#Task 1
# Create a Pandas Series with custom index labels. Use the data [10, 20, 30, 40, 50] and index
# labels ['a', 'b', 'c', 'd', 'e'] and display it.
ds=pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'] )
print(ds)

# Task 2
# Access the element at position 2 from a Series created from the list [100, 200, 300, 400, 500].
# Also give any example of labelled indexing for that list and display it.
llist = [100, 200, 300, 400, 500]
ls= pd.Series(llist, index=["a", "b", "c", "d", "e"])
print(ls.iloc[2])
print(ls.loc["a"])

# Task 3
# Create two Series: Series1 with values [5, 10, 15, 20] and index ['w', 'x', 'y', 'z'], and Series2 with
# values [2, 4, 6, 8] and index ['w', 'x', 'y', 'p']. Add, Subtract, Multiply and divide these two Series
# together. Handle possible NaN values.
Series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
Series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])
print((Series1 + Series2).fillna(0))
print((Series1 - Series2).fillna(0))
print((Series1 * Series2).fillna(1))
print((Series1 / Series2).fillna(1))

# Task 4
# Create a DataFrame with at least 5 rows and use the head() method to display the first 3 rows.
# Then use the tail() method to display the last 2 rows. Also, try experimenting with the default
# value and negative arguments for the these methods.
df = pd.DataFrame({
    "name": ["ani", "nini", "luka", "mari", "gio"],
    "age": [10, 23, 19, 25, 30],
    "hobby": ["paint", "crochet", "gaming", "reading", "coding"],
    "course": ["CS", "Mgmt", "Math", "Bio", "CS"],
    "mangareader?": [True, False, True, False, True]
})

print(f"first 3 rows: {df.head(3)}")
print(f"last 3 rows: {df.tail(3)}")
print(df.head(-2))
print(df.tail(-1))


# Task 5
# Create a Series from [15, 22, 15, 30, 22, 45, 30, 15]. Find the unique values, count how many
# unique values there are using nunique(), and display the frequency of each value using
# value_counts().
se5 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print("unique values: ",se5.unique())
print("count of unique values: ",se5.nunique())
print("frequency of unique values: ",se5.value_counts())


# Task 6
# Create a DataFrame with columns 'Item' and 'Cost' containing at least 5 items. Add a new
# column called 'Tax' that is 10% of the Cost. Add another column called 'Total' which is Cost plus
# Tax. Then filter and display only the rows where Total is greater than 50.
df6 = pd.DataFrame({"Item":["leptop","Charger","cup","bycicle","manga"],
                   "Cost":[3000,100,18,500,20]
})
df6["Tax"]= df6["Cost"] * 0.1
df6["Total"]= df6["Cost"] + df6["Tax"]
print(df6[df6["Total"]>50])

# Task 7
# Create a DataFrame with columns 'Product', 'Category', 'Price', 'Stock' containing at least 8
# products from different categories. Then perform the following operations:
# • Use isnull() and notnull() to check for missing values
# • Use value_counts() on the Category column to count products in each category
# • Use nlargest() to find the top 3 most expensive products
# • Use nsmallest() to find the 2 products with the lowest stock
# • Display the shape and ndim of the DataFrame
df7 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Headphones", "Chair", "Table",
                "T-Shirt", "Jeans", "Shoes"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Furniture", "Furniture",
                 "Clothing", "Clothing", "Clothing"],
    "Price": [1200, 800, 150, 200, 500, 25, 45, 60],
    "Stock": [10, 25, 40, 12, 8, 50, 35, 20]
})

print(df7.isnull())
print(df7.notnull())
print(df7["Category"].value_counts())
print(df7.nlargest(3,"Price"))
print(df7.nsmallest(3, "Price"))
print(f"Shape: {df7.shape}, ndim: {df7.ndim}")


# Task 8
# Create a DataFrame with columns 'Student', 'Subject', 'Score', 'Attendance' containing at least 10
# students with some duplicate student names taking different subjects. Then perform the
# following operations:
# • Use duplicated() to identify duplicate student names
# • Use drop_duplicates() to remove duplicate student names keeping the first occurrence
# • Use set_index() to set Student as the index
# • Use loc[] to retrieve data for a specific student
# • Use iloc[] to retrieve the first 3 rows
# • Use query() method to find students with Score greater than 80 and Attendance greater
# than 85
# • Use between() to find students with scores between 70 and 90

df8 = pd.DataFrame({
    "Student": [
        "Ani", "Cinco", "Nini", "Ani", "Gio",
        "keti", "Nini", "Mari", "Cinco", "Tiko"
    ],
    "Subject": [
        "Math", "Physics", "Chemistry", "History", "Math",
        "CS", "Biology", "Math", "English", "Physics"
    ],
    "Score": [85, 92, 78, 88, 90, 95, 80, 87, 70, 89],
    "Attendance": [90, 85, 88, 92, 94, 98, 80, 86, 75, 93]
})

print(df8.duplicated("Student"))
df8.drop_duplicates(subset="Student", keep="first", inplace=True)
print(df8)
df8.set_index("Student", inplace=True)
print(df8.loc["Cinco"])
print("first 3 rows: ", df8.iloc[0:3])
print("query results: " ,df8.query("Score>80 & Attendance>85"))
print("scores between 70 and 90: ",df8["Score"].between(70,90))

