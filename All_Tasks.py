import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame

#task1
data=[10, 20, 30, 40, 50]

indexes=['a', 'b', 'c', 'd', 'e']

ser=pd.Series(data,indexes)

print(ser)

#task2
ser=pd.Series([100, 200, 300, 400, 500],['mixa','nika','luka','gio','sandro'])

print(ser.iloc[2])

#task3
Series1=pd.Series( [5, 10, 15, 20] , ['w', 'x', 'y', 'z'])
Series2=pd.Series([2, 4, 6, 8], ['w', 'x', 'y', 'p'])

print(Series1.add(Series2).dropna())
print(Series1.sub(Series2).dropna())
print(Series1.multiply(Series2).dropna())
print(Series1.divide(Series2).dropna())

#task4
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 28, 40, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami']
}

df=pd.DataFrame(data)

print(df.head(3))
print(df.tail(2))

print(df.head())
print(df.tail())

print(df.head(-2))
print(df.tail(-3))

#task5

Series1=pd.Series([15, 22, 15, 30, 22, 45, 30, 15])
print(f"unique values: {Series1.unique()}\nnumber of unique values {Series1.nunique()}")
print(Series1.value_counts())

#task6

data = {
    'Item': ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam', 'Headphones'],
    'Cost': [1200.00, 75.50, 350.00, 5.99, 59.99, 110.00]
}

df=pd.DataFrame(data)

df.insert(loc=2,column='Tax', value=df.get('Cost')*0.1)

df.insert(loc=3,column='Total', value=df.get('Cost')+df.get('Tax'))
print(df)

print(df[df['Total']>50])

#task7
data = {
    'Product': ['A_Desk', 'B_Chair', 'C_Laptop', 'D_Mouse', 'E_Monitor', 'F_Keyboard', 'G_Software', 'H_Lamp'],
    'Category': ['Furniture', 'Furniture', 'Electronics', 'Electronics', 'Electronics', 'Electronics', np.nan, 'Furniture'],
    'Price': [350.00, 150.50, 1200.00, 25.99, 450.00, 75.00, 199.99, 45.00],
    'Stock': [15, 22, 8, 50, 12, 30, 999, 5] # 999 is intentionally high stock
}

df=pd.DataFrame(data)

print(df.isnull())
print(df.notnull())

print(pd.Series(data['Category']).value_counts())

print(pd.Series(data['Price']).nlargest(3))

print(pd.Series(data['Price']).nsmallest(2))

print(f"Shape:{df.shape} , dim:{df.ndim}")

#task8

data = {
    'Student': [
        'Alex', 'Beth', 'Chris', 'David', 'Eve',
        'Alex', 'Beth', 'Chris', 'Fiona', 'George'
    ],
    'Subject': [
        'Math', 'Science', 'History', 'Math', 'English',
        'Science', 'Math', 'Geography', 'Science', 'English'
    ],
    'Score': [
        92, 85, 78, 65, 95,
        88, 75, 82, 90, 70
    ],
    'Attendance': [
        0.95, 0.90, 0.85, 0.98, 0.99,
        0.92, 0.88, 0.80, 0.95, 0.93
    ]
}

df=pd.DataFrame(data)
print(df)

print(df['Student'].duplicated(keep='first'))

df=df.drop_duplicates(subset='Student',keep='first')
print(df)

print(df.loc[df['Student']=='Alex'])
print(df.iloc[:3])


print(df.query('Score > 80 and Attendance > 0.85'))
print(df[df['Score'].between(70,90)])

