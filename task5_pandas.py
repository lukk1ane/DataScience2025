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
import pandas as pd, numpy as np
from pandas import json_normalize

data = pd.DataFrame({
    'colA': np.random.choice(['X','Y','Z'], 200),
    'colB': np.random.choice(['A','B'], 200),
    'colC': np.random.choice(['K','L'], 200),
    'value': np.random.rand(200) * 1000,
    'Employee ID': np.random.randint(1, 10, 200),
    'Date': pd.date_range('2025-01-01', periods=200, freq='D'),
    'amount': np.random.randint(100, 2000, 200),
    'Category': np.random.choice(['Food','Tech','Clothes'], 200),
    'Value': np.random.randint(10, 500, 200),
    'json_col1': [{'a': i, 'b': i**2} for i in range(200)],
    'json_col2': [{'x': i*2, 'y': i+5} for i in range(200)]
})

# Task 1
cols = ['colA','colB','colC']
for c in cols:
    if data[c].dtype == object:
        data[c] = data[c].astype('category')
combo_counts = data.groupby(cols, sort=False).size().reset_index(name='count')
popular_combos = combo_counts[combo_counts['count'] >= 10]

# Task 2
missing_pct = data.isna().mean()
top3_cols = missing_pct.nlargest(3).index.tolist()
data_cleaned = data.dropna(subset=top3_cols)

# Task 3
most_freq = {}
for col in data.columns:
    vc = data[col].value_counts(dropna=True)
    most_freq[col] = vc.index[0] if len(vc) else np.nan
most_freq_series = pd.Series(most_freq)

# Task 4
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(['Employee ID','Date'])
data_unique = data.drop_duplicates(subset=['Employee ID','Date'])
d = data_unique.copy()
d['prev_date'] = d.groupby('Employee ID')['Date'].shift(1)
d['gap_days'] = (d['Date'] - d['prev_date']).dt.days.fillna(9999)
d['new_group'] = (d['gap_days'] != 1).astype(int)
d['group_id'] = d.groupby('Employee ID')['new_group'].cumsum()
streaks = d.groupby(['Employee ID','group_id']).size().reset_index(name='streak_len')
employees_with_5_consecutive = streaks[streaks['streak_len'] >= 5]['Employee ID'].unique()

# Task 5
data_ts = pd.DataFrame({
    'value': np.random.randint(1, 100, 200)
}, index=pd.date_range('2023-01-01', periods=200, freq='D'))
data_ts.index = pd.to_datetime(data_ts.index)
monthly = data_ts.resample('M').sum()
q1 = monthly[monthly.index.month.isin([1,2,3])]
q1_per_year = q1.groupby(q1.index.year).apply(lambda g: g)

# Task 6
threshold = data['value'].quantile(0.95)
data_trimmed = data[data['value'] <= threshold]

# Task 7
data_time = pd.DataFrame({
    'x': np.random.randn(200)
}, index=pd.to_datetime(pd.date_range('2024-01-01', periods=200, freq='2D')))
data_time = data_time.sort_index()
rolling_avg = data_time.rolling('7D').mean().interpolate()

# Task 8
threshold_val = 10000
cumsum = data['amount'].cumsum()
first_exceed_idx = cumsum.gt(threshold_val).idxmax() if (cumsum > threshold_val).any() else None

# Task 9
idx = data.groupby('Category')['Value'].transform('max') == data['Value']
max_rows = data[idx]

# Task 10
json_cols = ['json_col1','json_col2']
for col in json_cols:
    expanded = json_normalize(data[col]).add_prefix(f'{col}_')
    data = pd.concat([data.drop(columns=[col]), expanded], axis=1)

