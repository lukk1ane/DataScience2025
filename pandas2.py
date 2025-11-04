import pandas as pd
import numpy as np

# task 1

data = {
    "Name": ["Mariami", "Adnria", "goga", "dachi", "nika", "luka"],
    "Age": [20, 19, 20, np.nan, 23, 22],
    "Gender": ["F", "M", "M", "M", "M", "M"],
    "Score": [85, np.nan, 78, 92, np.nan, 76],
    "City": ["Tbilisi", "Batumi", np.nan, "Kutaisi", "Tbilisi", "Batumi"],
    "Study_Hours": [31, 32, np.nan, 30, 40, 45],
}

df = pd.DataFrame(data)
print(df)

df1 = df.groupby(["Name", "Age", "Gender"]).size().reset_index(name="Count")
print(df1[df1["Count"] > 10])

# task 2

data = {
    "Name": ["Mariami", "Adnria", "goga", "dachi", "nika", "luka"],
    "Age": [20, 19, 20, np.nan, 23, 22],
    "Gender": ["F", "M", "M", "M", "M", "M"],
    "Score": [85, np.nan, 78, 92, np.nan, 76],
    "City": ["Tbilisi", "Batumi", np.nan, "Kutaisi", "Tbilisi", "Batumi"],
    "Study_Hours": [31, 32, np.nan, 30, 40, 45],
}

missing_percent = df.isna().mean().sort_values(ascending=False) * 100
print(missing_percent.head(3))
missing_percent_list = missing_percent.head(3).index.tolist()
df2 = df.dropna(subset=missing_percent_list)
print(df2)

# task 3

df = pd.DataFrame(
    {
        "City": np.random.choice(
            ["New York", "London", "Tokyo", "Paris", np.nan], size=100000
        ),
        "Age": np.random.randint(18, 70, size=100000),
        "Gender": np.random.choice(["Male", "Female", np.nan], size=100000),
        "Department": np.random.choice(["HR", "IT", np.nan, "Finance"], size=100000),
    }
)

most_frequent_values = {}
for col in df.columns:
    counts = {}

    for value in df[col]:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    max_count = max(counts.values())

    for key, value in counts.items():
        if value == max_count:
            most_frequent_values[col] = key
            break

print(most_frequent_values)

# task 4

data = {
    "Employee ID": [
        "E001",
        "E001",
        "E001",
        "E001",
        "E001",
        "E002",
        "E002",
        "E002",
        "E003",
        "E003",
        "E003",
        "E003",
        "E003",
    ],
    "Date": [
        "2025-10-01",
        "2025-10-02",
        "2025-10-03",
        "2025-10-04",
        "2025-10-05",  # E001 (5 consecutive)
        "2025-10-01",
        "2025-10-03",
        "2025-10-04",  # E002 (gap)
        "2025-10-02",
        "2025-10-03",
        "2025-10-04",
        "2025-10-05",
        "2025-10-06",  # E003 (5 consecutive)
    ],
    "Hours Worked": [8, 7, 8, 9, 8, 8, 7, 8, 8, 8, 7, 9, 8],
}

result = []
df4 = pd.DataFrame(data)
df4["Date"] = pd.to_datetime(df4["Date"])

for emp, group in df4.groupby("Employee ID"):
    group = group.sort_values("Date")
    dates = group["Date"].tolist()

    streak = 1
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
            if streak >= 5:
                result.append(emp)
                break
        else:
            streak = 1

print(result)


# task 5

dates = pd.date_range(start="2024-01-01", end="2025-12-31", freq="D")
data = np.random.randint(1, 10, size=len(dates))

df = pd.DataFrame({"Value": data}, index=dates)
df.index.name = "Date"

print(df)

montly_sum = df.resample("ME").sum()

first_quarter = montly_sum[montly_sum.index.month.isin([1, 2, 3])]
print(first_quarter)

# task 6

data = {"TransactionID": range(1, 21), "Value": np.random.randint(100, 1000, 20)}
df = pd.DataFrame(data)
percentage = df["Value"].quantile(0.95)
df_filtered = df[df["Value"] <= percentage]
print(df_filtered)

# task 7

dates = pd.to_datetime(
    ["2025-01-01", "2025-01-03", "2025-01-04", "2025-01-07", "2025-01-08", "2025-01-12"]
)

values = [10, 20, 30, 40, 50, 60]

df = pd.DataFrame({"Value": values}, index=dates)
df.index.name = "Date"
df["Moving_Avg"] = df["Value"].rolling("3D", min_periods=1).mean()
print(df)


# task 8

data = {
    "TransactionID": range(1, 11),
    "Amount": [100, 150, 200, 50, 300, 400, 250, 100, 150, 200],
}

df = pd.DataFrame(data)
df["CumSum"] = df["Amount"].cumsum()
threshold = 500
mask = df["CumSum"] > threshold
exceeded = df[mask].head(1)
print(exceeded)

# task 9


data = {
    "Category": ["A", "A", "A", "B", "B", "C", "C", "C"],
    "Value": [10, 25, 15, 5, 20, 30, 25, 40],
}

df = pd.DataFrame(data)
df_max = df[df["Value"] == df.groupby("Category")["Value"].transform("max")]
print(df_max)


# task 10
data = {
    "ID": [1, 2, 3],
    "Info": [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
        {"Name": "Charlie", "Age": 35},
    ],
    "Department": ["HR", "Finance", "IT"],
}

df = pd.DataFrame(data)
info_df = pd.json_normalize(df["Info"])
df_flat = df.drop(columns=["Info"]).join(info_df)
print(df_flat)
