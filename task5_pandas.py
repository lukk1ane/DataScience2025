# Data Manipulations with Pandas II
# Task 1
# Given a DataFrame with multiple categorical columns, find all unique combinations of values from
# these columns that occur at least 10 times. This Task involves:
# - Identifying combinations across several columns
# - Counting occurrences efficiently
# - Ensuring optimal performance for large datasets.
# Task 2
# You are provided with a DataFrame containing missing data across many columns. Your task is to:
# - Identify the top 3 columns that have the highest percentage of missing values.
# - Remove rows with missing values in those top 3 columns, but leave the rest of the DataFrame
# intact.
# Task 3
# Given a DataFrame of 100,000 rows with mixed data types, find the most frequent value for each
# column without using the mode function.
# - Focus on alternative Pandas built-in methods.
# Task 4
# In a DataFrame containing employee work hours (with columns 'Employee ID', 'Date', and 'Hours
# Worked'), identify employees who have worked for 5 consecutive days.
# - Consider time series data handling
# - Properly analyze date intervals to ensure accuracy.
# Task 5
# You have a time-series DataFrame indexed by dates. Your task is to:
# - Resample the data to monthly intervals
# - Focus only on the first quarter of each year (Jan, Feb, Mar)
# - Sum the values for each month in the first quarter.
# Task 6
# Given a sales transactions DataFrame, remove the top 5% of transactions by value. Ensure that:
# - The remaining data keeps its original index positions
# - You properly exclude rows based on percentile thresholds without sorting the entire DataFrame.
# Task 7
# Create a moving average calculation for a time series that has irregular time intervals.
# - Ensure the rolling window takes into account the gaps in time
# - Handle any missing values efficiently.
# Task 8
# Given a DataFrame of financial transactions, detect when the cumulative sum of previous
# transactions exceeds a given threshold for the first time.
# - Focus on an efficient way to track this threshold without iterating row by row.
# Task 9
# With a DataFrame containing a 'Category' column and a 'Value' column, your task is to:
# - Group by 'Category'
# - Find the rows where the 'Value' is the maximum for each category.
# - Avoid using lambda or apply functions.
# Task 10
# You have a DataFrame where some columns contain nested JSON-like data (dictionaries). Your
# task is to:
# - Flatten the DataFrame by creating new columns for each key in the nested data
# - Ensure the original data structure remains intact while expanding the JSON fields.

import pandas as pd
import numpy as np
from pandas import json_normalize

# -------------------------
# Create Example DataFrame
# -------------------------
df = pd.DataFrame({
    'Category1': np.random.choice(['X', 'Y', 'Z'], 200),
    'Category2': np.random.choice(['A', 'B'], 200),
    'Category3': np.random.choice(['K', 'L'], 200),
    'TransactionValue': np.random.rand(200) * 1000,
    'EmployeeID': np.random.randint(1, 10, 200),
    'WorkDate': pd.date_range('2025-01-01', periods=200, freq='D'),
    'Amount': np.random.randint(100, 2000, 200),
    'ProductCategory': np.random.choice(['Food', 'Tech', 'Clothes'], 200),
    'ProductValue': np.random.randint(10, 500, 200),
    'JsonData1': [{'a': i, 'b': i**2} for i in range(200)],
    'JsonData2': [{'x': i*2, 'y': i+5} for i in range(200)]
})

# Task 1: Frequent Categorical Combinations
categorical_cols = ['Category1', 'Category2', 'Category3']

# Ensure categories are of type 'category' for efficiency
for col in categorical_cols:
    df[col] = df[col].astype('category')

combination_counts = df.groupby(categorical_cols).size().reset_index(name='Count')
frequent_combinations = combination_counts[combination_counts['Count'] >= 10]

# Task 2: Remove Rows Based on Top 3 Missing Columns
missing_percentage = df.isna().mean()
top3_missing_cols = missing_percentage.nlargest(3).index.tolist()
df_cleaned = df.dropna(subset=top3_missing_cols)

# Task 3: Most Frequent Value per Column (Without mode())
most_common_values = {}
for col in df.columns:
    counts = df[col].value_counts()
    most_common_values[col] = counts.idxmax() if not counts.empty else np.nan
most_common_series = pd.Series(most_common_values)

# Task 4: Employees with 5 Consecutive Workdays
df['WorkDate'] = pd.to_datetime(df['WorkDate'])
df_sorted = df.sort_values(['EmployeeID', 'WorkDate']).drop_duplicates(subset=['EmployeeID','WorkDate'])

df_sorted['PreviousDate'] = df_sorted.groupby('EmployeeID')['WorkDate'].shift(1)
df_sorted['DayGap'] = (df_sorted['WorkDate'] - df_sorted['PreviousDate']).dt.days.fillna(9999)
df_sorted['NewStreak'] = (df_sorted['DayGap'] != 1).astype(int)
df_sorted['StreakID'] = df_sorted.groupby('EmployeeID')['NewStreak'].cumsum()

streak_lengths = df_sorted.groupby(['EmployeeID','StreakID']).size().reset_index(name='StreakLength')
employees_5_day_streak = streak_lengths[streak_lengths['StreakLength'] >= 5]['EmployeeID'].unique()

# Task 5: Monthly Resample for Q1
time_series_df = pd.DataFrame({'Value': np.random.randint(1, 100, 200)},
                              index=pd.date_range('2023-01-01', periods=200, freq='D'))
monthly_sum = time_series_df.resample('M').sum()
q1_sum_per_year = monthly_sum[monthly_sum.index.month.isin([1, 2, 3])].groupby(lambda d: d.year).sum()

# Task 6: Remove Top 5% Transactions by Value
value_threshold = df['TransactionValue'].quantile(0.95)
df_trimmed = df[df['TransactionValue'] <= value_threshold]

# Task 7: Moving Average with Irregular Time Intervals
irregular_time_df = pd.DataFrame({'X': np.random.randn(200)},
                                 index=pd.date_range('2024-01-01', periods=200, freq='2D'))
irregular_time_df = irregular_time_df.sort_index()
rolling_avg_7days = irregular_time_df.rolling('7D').mean().interpolate()

# Task 8: First Time Cumulative Sum Exceeds Threshold
cumsum_threshold = 10000
cumulative_sum = df['Amount'].cumsum()
first_exceed_index = cumulative_sum.gt(cumsum_threshold).idxmax() if (cumulative_sum > cumsum_threshold).any() else None

# Task 9: Max Value per Category
is_max_per_category = df.groupby('ProductCategory')['ProductValue'].transform('max') == df['ProductValue']
max_value_rows = df[is_max_per_category]

# Task 10: Flatten Nested JSON Columns
json_columns = ['JsonData1', 'JsonData2']
for col in json_columns:
    expanded_cols = json_normalize(df[col]).add_prefix(f'{col}_')
    df = pd.concat([df.drop(columns=[col]), expanded_cols], axis=1)
