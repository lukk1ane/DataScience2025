import numpy as np
import pandas as pd

# Task 1: Data Summary and Initial Observations
# Conduct an initial analysis to understand the dataset's structure and patterns.

read_data = pd.read_csv("DAVALEBEBI/task6/sample_data.csv")  # Load dataset

first_5_rows = read_data.head()  # display first 5 rows

summary_statistics = read_data.describe(include='all')  # summary statistics for each feature

churn_distribution = round(read_data['churn'].value_counts(normalize=True)[1]*100, 2)  # percentage of customers who churn

#  Observations:
# The dataset has 500 customers, each with 9 features (age, income, spending score, etc.).
# The churn rate is around 47%, which is nearly balanced — good for classification.
# Some numeric columns like annual_income and spending_score have very wide ranges, suggesting strong variation among customer groups.

# ---------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram for annual income
plt.figure(figsize=(8,5))
plt.hist(read_data['annual_income'], bins=25)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Frequency")
plt.show()

# COMMENT:
print("Histogram Comment: Income is widely spread, with many customers between 50k–110k. A few low-income groups exist.")

# Boxplot: spending score vs category
plt.figure(figsize=(8,5))
sns.boxplot(data=read_data, x='category', y='spending_score')
plt.title("Spending Score by Category")
plt.show()

print("Boxplot Comment: Some categories (like D) have higher spending-score ranges. Categories have different median spending.")

# Scatter plot: Income vs Spending score (colored by churn)
plt.figure(figsize=(8,5))
sns.scatterplot(data=read_data, x='annual_income', y='spending_score', hue='churn')
plt.title("Income vs Spending Score by Churn")
plt.show()

print("Scatter Comment: High spending-score customers churn more often. Non-churn customers appear clustered in lower-score areas.")


# --------------------------------------------------------------------------------------------------------------------------------------

# Create new feature
read_data['customer_value_score'] = read_data['spending_score'] * read_data['membership_years']

# Top 10 most valuable customers
top10 = read_data.sort_values(by='customer_value_score', ascending=False).head(10)

print("TOP 10 HIGH-VALUE CUSTOMERS:")
print(top10[['customer_id', 'spending_score', 'membership_years', 'customer_value_score']], "\n")

print("""
Business Interpretation:
Customers with high spending and long membership are most valuable.
These customers should receive loyalty programs, discounts, and 
personalized recommendations to keep retention high.
""")


# --------------------------------------------------------------------------------------------------------------------------------------


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Features and target
X = read_data[['spending_score', 'annual_income']]
y = read_data['churn']

# Split: 80% training, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Prediction
y_pred = dt.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Baseline Accuracy:", accuracy)

print("""
Comment:
This accuracy provides a basic baseline. Since we only used 2 features,
the model cannot capture all churn behavior, so accuracy around 60–75%
is expected. A more advanced model would use more features.
""")


# --------------------------------------------------------------------------------------------------------------------------------------


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Features chosen
X = read_data[['age', 'annual_income', 'spending_score', 'membership_years']]
y = read_data['churn']

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier()
}

print("CROSS-VALIDATION ACCURACIES:\n")

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name}: Mean Accuracy = {scores.mean():.4f}")

print("""
Recommendation:
Choose the model with the highest mean cross-validation accuracy.
Logistic Regression is best for linear patterns, Decision Tree for
non-linear behavior, and KNN works well when similar customers share patterns.
""")

