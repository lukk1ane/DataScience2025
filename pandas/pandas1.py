import pandas as pd

#Task 1
ds=pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'] )
print(ds)

# Task 2
llist = [100, 200, 300, 400, 500]
ls= pd.Series(llist, index=["a", "b", "c", "d", "e"])
print(ls.iloc[2])
print(ls.loc["a"])

# Task 3
Series1 = pd.Series([5, 10, 15, 20], index=['w', 'x', 'y', 'z'])
Series2 = pd.Series([2, 4, 6, 8], index=['w', 'x', 'y', 'p'])
print((Series1 + Series2).fillna(0))
print((Series1 - Series2).fillna(0))
print((Series1 * Series2).fillna(1))
print((Series1 / Series2).fillna(1))

# Task 4
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
se5 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print("unique values: ",se5.unique())
print("count of unique values: ",se5.nunique())
print("frequency of unique values: ",se5.value_counts())


# Task 6
df6 = pd.DataFrame({"Item":["leptop","Charger","cup","bycicle","manga"],
                   "Cost":[3000,100,18,500,20]
})
df6["Tax"]= df6["Cost"] * 0.1
df6["Total"]= df6["Cost"] + df6["Tax"]
print(df6[df6["Total"]>50])

# Task 7
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

