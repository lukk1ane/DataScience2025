import pandas as pd

# loc index by label
# iloc index byposition
# fill_value helps replace NaN with a number

# task1
data = [10, 20, 30, 40, 50]
index_labels = ["a", "b", "c", "d", "e"]

series1 = pd.Series(data, index=index_labels)
print(series1)

# task2

series2 = pd.Series([100, 200, 300, 400, 500])
print(series2.iloc[2])

series20 = pd.Series([100, 200, 300, 400, 500], index=["a", "b", "c", "d", "e"])
print(series20.loc["c"])

# task3
series30 = pd.Series([5, 10, 15, 20], index=["w", "x", "y", "z"])
series31 = pd.Series([2, 4, 6, 8], index=["w", "x", "y", "p"])

print(series30.add(series31, fill_value=0))
print(series30.sub(series31, fill_value=0))
print(series30.mul(series31, fill_value=1))
print(series30.div(series31, fill_value=1))


# task4

data4 = {"Name": ["A", "B", "C", "D", "E"], "Score": [85, 90, 78, 92, 88]}
df4 = pd.DataFrame(data4)
print(df4.head(3))
print(df4.tail(2))
print(df4.head(-2))

# task5
series5 = pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(series5.unique())
print(series5.nunique())  # counts
print(series5.value_counts())  # frequency for each value

# task6

data6 = {
    "Item": ["Laptop", "Tablet", "Ipad", "Macbook", "pencil"],
    "Cost": [10, 25, 40, 60, 80],
}

df6 = pd.DataFrame(data6)

df6["Tax"] = df6["Cost"] * 0.10
df6["Total"] = df6["Cost"] + df6["Tax"]

filtered_df6 = df6[df6["Total"] > 50]

print(filtered_df6)

# task 7

# made ai generate this
data7 = {
    "Product": [
        "Phone",
        "Tablet",
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Camera",
        "Headphones",
    ],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Cameras",
        "Accessories",
    ],
    "Price": [800, 500, 1000, 50, 70, 300, 600, 120],
    "Stock": [20, 15, 10, 50, 40, 25, 5, 60],
}

df7 = pd.DataFrame(data7)

print(df7.isnull())
print(df7.notnull())
print(df7["Category"].value_counts())
print(df7.nlargest(3, "Price"))
print(df7.nsmallest(2, "Stock"))
print(df7.shape)
print(df7.ndim)

# task8
import pandas as pd

data8 = {
    "Student": [
        "Nino",
        "Giorgi",
        "Ana",
        "Nino",
        "Luka",
        "Mariam",
        "Dato",
        "Giorgi",
        "Salome",
        "Irakli",
    ],
    "Subject": [
        "Math",
        "Physics",
        "Chemistry",
        "Biology",
        "Math",
        "Chemistry",
        "Biology",
        "Math",
        "Physics",
        "Math",
    ],
    "Score": [95, 82, 78, 88, 70, 92, 85, 65, 80, 90],
    "Attendance": [90, 88, 84, 92, 70, 95, 88, 60, 89, 94],
}

df8 = pd.DataFrame(data8)

print(df8["Student"].duplicated())
df_unique = df8.drop_duplicates(subset="Student", keep="first")
print(df_unique)
df_unique = df_unique.set_index("Student")
print(df_unique)
print(df_unique.loc["Nino"])
print(df_unique.iloc[:3])
print(df8.query("Score > 80 and Attendance > 85"))
print(df8[df8["Score"].between(70, 90)])
