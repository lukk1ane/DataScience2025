import numpy as np
import pandas as pd
from faker import Faker
import random

'''
Task 1
Given a DataFrame with multiple categorical columns, find all unique combinations of values from
these columns that occur at least 10 times. This Task involves:
- Identifying combinations across several columns
- Counting occurrences efficiently
- Ensuring optimal performance for large datasets.
'''

num_rows = 500
cities = ['New York', 'Paris', 'Tokyo', 'London']
products = ['A', 'B', 'C','D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'pink']

product_data = {
    'City' : [random.choice(cities) for _ in range(num_rows)],
    'Product' : [random.choice(products) for _ in range(num_rows)],
    'Color' : [random.choice(colors) for _ in range(num_rows)]
}

products_df = pd.DataFrame(product_data)
combination_count = products_df.groupby(['City', 'Product', 'Color']).size().reset_index(name = 'Count')
freq_combinations = combination_count[combination_count['Count'] >= 10]
freq_combinations = freq_combinations.sort_values(by = 'Count', ascending= False)
#print(freq_combinations)

'''
Task 2
You are provided with a DataFrame containing missing data across many columns. Your task is to:
- Identify the top 3 columns that have the highest percentage of missing values.
- Remove rows with missing values in those top 3 columns, but leave the rest of the DataFrame
intact.
'''

fake = Faker()

person_data = {
    'City': [fake.city() for _ in range(num_rows)],
    'Name': [fake.name() for _ in range(num_rows)],
    'job': [fake.job() for _ in range(num_rows)],
    'Age': [fake.random_int(min = 0, max = 90) for _ in range(num_rows)],
    'Phone Number': [fake.phone_number() for _ in range(num_rows)]

}

person_df = pd.DataFrame(person_data)

nan_prob = 0.15

mask = np.random.rand(*person_df.shape) < nan_prob
person_df = person_df.mask(mask)

#print(person_df.head(10))


missing_value_count = person_df.isna().sum().sort_values(ascending = False)
missing_summary = missing_value_count.reset_index()
missing_summary.columns = ['Column', 'MissingValues']
#print(missing_summary.head(3))
top3_cols = ['Name', 'Phone Number', 'Age']
person_df = person_df.dropna(subset = top3_cols)
#print(person_df.tail(10))
print(person_df.columns)
print(person_df.head(10).to_string())

'''
Task 3
Given a DataFrame of 100,000 rows with mixed data types, find the most frequent value for each
column without using the mode function.
- Focus on alternative Pandas built-in methods.
'''
rows = 100000
Faker.seed(0)
np.random.seed(0)

data = {
    'City': [fake.city() for _ in range(num_rows)],
    'Name': [fake.name() for _ in range(num_rows)],
    'Job': [fake.job() for _ in range(num_rows)],
    'Age': [fake.random_int(min=0, max=90) for _ in range(num_rows)],
    'Salary': [fake.random_int(min=30_000, max=200_000) for _ in range(num_rows)],
    'Phone': [fake.phone_number() for _ in range(num_rows)],
    'IsManager': [fake.boolean(chance_of_getting_true=30) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

most_frequent = {col: df[col].value_counts().idxmax() for col in df.columns}
most_frequent_series = pd.Series(most_frequent)

print(most_frequent_series)
'''
Task 4
In a DataFrame containing employee work hours (with columns 'Employee ID', 'Date', and 'Hours
Worked'), identify employees who have worked for 5 consecutive days.
- Consider time series data handling
- Properly analyze date intervals to ensure accuracy.
'''

employee_data = {
    'Employee Name' :[fake.name() for _ in range(1000)],
    'Employee ID' :[fake.unique.random_int(min = 10000, max = 999999) for _ in range(1000)],
    'Date': [fake.date() for _ in range(1000)],
    'Hours Worked': [fake.random_int( 1, 12 ) for _ in range(1000)]


}

employee_df = pd.DataFrame(employee_data)
employee_df['Date'] = pd.to_datetime(employee_df['Date'])
employee_df = employee_df.sort_values(['Employee ID', 'Date'])

consecutive_employees = []

for emp_id, group in employee_df.groupby('Employee ID'):
    group = group.sort_values('Date')
    dates = group['Date'].to_list()

    streak = 1
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
            if streak >= 5:
                consecutive_employees.append(emp_id)
                break
        else:
            streak = 1  # reset streak if not consecutive

consecutive_employees = list(set(consecutive_employees))  # remove duplicates

print("Employees who worked 5+ consecutive days:")
print(consecutive_employees)



'''
Task 5
You have a time-series DataFrame indexed by dates. Your task is to:
- Resample the data to monthly intervals
- Focus only on the first quarter of each year (Jan, Feb, Mar)
- Sum the values for each month in the first quarter.
'''
date_range = pd.date_range(start='2022-01-01', end='2025-12-31', freq='D')
np.random.seed(42)
data = {'Value': np.random.randint(10, 200, size=len(date_range))}
ts_df = pd.DataFrame(data, index=date_range)
ts_df.index.name = 'Date'

monthly_sum = ts_df.resample('ME').sum()
first_quarter = monthly_sum[monthly_sum.index.month.isin([1, 2, 3])]
first_quarter_summary = first_quarter.groupby(first_quarter.index.year).sum()

print(first_quarter)
print(first_quarter_summary)
'''
Task 6
Given a sales transactions DataFrame, remove the top 5% of transactions by value. Ensure that:
- The remaining data keeps its original index positions
- You properly exclude rows based on percentile thresholds without sorting the entire DataFrame.
'''
data = {
    'Transaction ID': [fake.unique.random_int(min=10000, max=999999) for _ in range(num_rows)],
    'Customer Name': [fake.name() for _ in range(num_rows)],
    'Transaction Value': np.random.randint(50, 5000, size=num_rows)
}

sales_df = pd.DataFrame(data)

threshold = np.percentile(sales_df['Transaction Value'], 95)
filtered_df = sales_df[sales_df['Transaction Value'] <= threshold]

#print(filtered_df)
'''
Task 7
Create a moving average calculation for a time series that has irregular time intervals.
- Ensure the rolling window takes into account the gaps in time
- Handle any missing values efficiently.
'''
dates = [fake.date_between(start_date='-3mo', end_date='today') for _ in range(100)]
values = np.random.randint(10, 200, size=len(dates))
ts_df = pd.DataFrame({'Value': values}, index=pd.to_datetime(dates))

ts_df = ts_df.groupby(ts_df.index).mean()
ts_df = ts_df.sort_index()

full_index = pd.date_range(start=ts_df.index.min(), end=ts_df.index.max())
ts_df = ts_df.reindex(full_index)
ts_df['Value'] = ts_df['Value'].interpolate(method='time')

ts_df['7D_MA'] = ts_df['Value'].rolling('7D').mean()

print(ts_df)

'''
Task 8
Given a DataFrame of financial transactions, detect when the cumulative sum of previous
transactions exceeds a given threshold for the first time.
- Focus on an efficient way to track this threshold without iterating row by row
'''
threshold = 5000

data = {
    'Transaction ID': [fake.unique.random_int(min=10000, max=999999) for _ in range(num_rows)],
    'Transaction Value': np.random.randint(50, 1000, size=num_rows)
}

df = pd.DataFrame(data)

df['Cumulative Sum'] = df['Transaction Value'].cumsum()

first_exceed_idx = df.index[df['Cumulative Sum'] > threshold][0]
first_exceed_transaction = df.loc[first_exceed_idx]

print("First transaction exceeding threshold:")
print(first_exceed_transaction)

'''
Task 9
With a DataFrame containing a 'Category' column and a 'Value' column, your task is to:
- Group by 'Category'
- Find the rows where the 'Value' is the maximum for each category.
- Avoid using lambda or apply functions.
'''
categories = ['A', 'B', 'C', 'D']
data = {
    'Category': np.random.choice(categories, size=num_rows),
    'Value': np.random.randint(1, 500, size=num_rows)
}

df = pd.DataFrame(data)

df['MaxValue'] = df.groupby('Category')['Value'].transform('max')

max_rows = df[df['Value'] == df['MaxValue']].drop(columns='MaxValue')

print(max_rows)
'''
Task 10
You have a DataFrame where some columns contain nested JSON-like data (dictionaries). Your
task is to:
- Flatten the DataFrame by creating new columns for each key in the nested data
- Ensure the original data structure remains intact while expanding the JSON fields.
'''

data = {
    'Transaction ID': [fake.unique.random_int(min=1000, max=9999) for _ in range(5)],
    'Customer': [fake.name() for _ in range(5)],
    'Details': [
        {'Item': fake.word(), 'Price': np.random.randint(10, 500), 'Quantity': np.random.randint(1, 10)}
        for _ in range(5)
    ]
}

df = pd.DataFrame(data)

details_df = pd.json_normalize(df['Details'])
details_df.columns = [f"Details_{col}" for col in details_df.columns]

flattened_df = pd.concat([df.drop(columns='Details'), details_df], axis=1)

print(flattened_df)
