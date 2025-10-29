import pandas as pd, numpy as np
from pandas import json_normalize

df = pd.DataFrame({
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
    if df[c].dtype == object:
        df[c] = df[c].astype('category')
combo_counts = df.groupby(cols, sort=False).size().reset_index(name='count')
popular_combos = combo_counts[combo_counts['count'] >= 10]

# Task 2
missing_pct = df.isna().mean()
top3_cols = missing_pct.nlargest(3).index.tolist()
df_cleaned = df.dropna(subset=top3_cols)

# Task 3
most_freq = {}
for col in df.columns:
    vc = df[col].value_counts(dropna=True)
    most_freq[col] = vc.index[0] if len(vc) else np.nan
most_freq_series = pd.Series(most_freq)

# Task 4
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(['Employee ID','Date'])
df_unique = df.drop_duplicates(subset=['Employee ID','Date'])
d = df_unique.copy()
d['prev_date'] = d.groupby('Employee ID')['Date'].shift(1)
d['gap_days'] = (d['Date'] - d['prev_date']).dt.days.fillna(9999)
d['new_group'] = (d['gap_days'] != 1).astype(int)
d['group_id'] = d.groupby('Employee ID')['new_group'].cumsum()
streaks = d.groupby(['Employee ID','group_id']).size().reset_index(name='streak_len')
employees_with_5_consecutive = streaks[streaks['streak_len'] >= 5]['Employee ID'].unique()

# Task 5
df_ts = pd.DataFrame({
    'value': np.random.randint(1, 100, 200)
}, index=pd.date_range('2023-01-01', periods=200, freq='D'))
df_ts.index = pd.to_datetime(df_ts.index)
monthly = df_ts.resample('M').sum()
q1 = monthly[monthly.index.month.isin([1,2,3])]
q1_per_year = q1.groupby(q1.index.year).apply(lambda g: g)

# Task 6
threshold = df['value'].quantile(0.95)
df_trimmed = df[df['value'] <= threshold]

# Task 7
df_time = pd.DataFrame({
    'x': np.random.randn(200)
}, index=pd.to_datetime(pd.date_range('2024-01-01', periods=200, freq='2D')))
df_time = df_time.sort_index()
rolling_avg = df_time.rolling('7D').mean().interpolate()

# Task 8
threshold_val = 10000
cumsum = df['amount'].cumsum()
first_exceed_idx = cumsum.gt(threshold_val).idxmax() if (cumsum > threshold_val).any() else None

# Task 9
idx = df.groupby('Category')['Value'].transform('max') == df['Value']
max_rows = df[idx]

# Task 10
json_cols = ['json_col1','json_col2']
for col in json_cols:
    expanded = json_normalize(df[col]).add_prefix(f'{col}_')
    df = pd.concat([df.drop(columns=[col]), expanded], axis=1)
