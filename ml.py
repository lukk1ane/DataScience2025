import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# task 1
df = pd.read_csv("sample_data.csv")
print(df.head())
print(df.describe(include="all"))
print(df.isnull().sum())
print(df["churn"].value_counts())
print((df["churn"].value_counts() / len(df)) * 100)
# 52 percent of customers have churned

# task 2

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="annual_income",
    bins=30,
    kde=True,
    hue="churn",
    palette="Set1",
    element="step",
)
plt.title("Distribution of Annual Income by Churn Status")
plt.xlabel("Annual Income")
plt.ylabel("Count")
plt.show()


# task3

df["customer_value_score"] = df["spending_score"] * df["membership_years"]
top10 = df.sort_values(by="customer_value_score", ascending=False).head(10)

print(top10)


# task 4
X = df[["spending_score", "annual_income"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

m4 = DecisionTreeClassifier(random_state=42)
m4.fit(X_train, y_train)

y_pred = m4.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"accuracy{accuracy}")


# task5

X = df[["age", "annual_income", "spending_score", "membership_years"]]
y = df["churn"]

m5 = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
}


results = {}

for name, model in m5.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    results[name] = scores
    print(f"name is {name}, accuracy is {scores.mean()} and std is {scores.std()}")
