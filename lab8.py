import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


# task 1

df = pd.read_csv("sample_data.csv")

print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Display summary statistics
print("Summary statistics:")
print(df.describe(include='all'), "\n")

print("Missing values per column:")
print(df.isnull().sum(), "\n")

if 'churn' in df.columns:
    churn_counts = df['churn'].value_counts()
    churn_percentage = (churn_counts / len(df)) * 100
    print("churn distribution (count and %):")
    print(pd.DataFrame({'Count': churn_counts, 'Percentage': churn_percentage.round(2)}))
else:
    print("Column 'churn' not found in the dataset.")


# task 2

# Histogram for Annual Income
plt.figure(figsize=(8,5))
sns.histplot(df['annual_income'], kde=True, bins=30, color='skyblue')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()

""" Comment:
Most customers seem to fall within a mid-income range.
There might be a few high-income outliers that create a long right tail.
"""

# Boxplot: Spending Score vs. Category
plt.figure(figsize=(8,5))
sns.boxplot(x='category', y='spending_score', data=df, color='skyblue')
plt.title('Spending Score Across Categories')
plt.xlabel('Category')
plt.ylabel('Spending Score')
plt.show()

"""Comment:
Some categories show higher median spending scores,
suggesting those groups tend to spend more.
Outliers may represent high-value customers or special cases.
"""

# Scatter Plot: Annual Income vs. Spending Score (colored by churn)
plt.figure(figsize=(8,6))
sns.scatterplot(x='annual_income', y='spending_score', hue='churn', data=df, palette='coolwarm', alpha=0.7)
plt.title('Annual Income vs. Spending Score (by churn Status)')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend(title='churn')
plt.show()

""" Comment:
Customers with low income and low spending seem more likely to churn.
High-income, high-spending customers appear to stay longer (lower churn rate).
The plot may indicate a cluster of loyal high spenders versus at-risk low spenders.
"""


# task 3
# Create a new feature: customer_value_score
# Formula: spending_score * membership_years
df['customer_value_score'] = df['spending_score'] * df['membership_years']

# Sort and display top 10 highest-value customers
top_customers = df.sort_values(by='customer_value_score', ascending=False).head(10)

print("Top 10 Highest-Value Customers:")
print(top_customers[['customer_id', 'spending_score', 'membership_years', 'customer_value_score']])


# task 4

# Select features and target
X = df[['spending_score', 'annual_income']]
y = df['churn']

# Split data into training and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.2f}")

# task 5
# Select features and target
X = df[['age', 'annual_income', 'spending_score', 'membership_years']]
y = df['churn']

# Define models to compare
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

# Perform 5-fold cross-validation and store results
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()
    print(f"{name} Mean CV Accuracy: {scores.mean():.4f}")

# Identify best-performing model
best_model = max(cv_results, key=cv_results.get)
print(f"\nBest Model: {best_model} with Mean Accuracy = {cv_results[best_model]:.4f}")