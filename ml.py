import numpy as np
import csv
import pandas as pd

# task 1
df = pd.read_csv("sample_data.csv")
print(df.head())
print(df.describe(include="all"))
print(df.isnull().sum())
print(df["churn"].value_counts())
print((df["churn"].value_counts() / len(df)) * 100)
# 52 percent of customers have churned
