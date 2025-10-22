import pandas as pd
import numpy as np


"""
Task 1 
Create a Pandas Series with custom index labels.
Use the data [10, 20, 30, 40, 50] and index labels ['a', 'b', 'c', 'd', 'e'] and display it.
"""

data_list = [10, 20, 30, 40, 50]
labels = ['a', 'b', 'c', 'd', 'e']

my_series = pd.Series(data_list, index = labels)
print(my_series)


"""
#Task 2 Access the element at position 2 from a Series created from the list [100, 200, 300, 400, 500].
Also give any example of labelled indexing for that list and display it.
"""


data_list1 = [100, 200, 300, 400, 500]
custom_labels = ['1', '2','3','4','5']
my_series1 = pd.Series(data_list1, index = custom_labels)
my_element = my_series1.iloc[1]
print(my_series1)
print(my_element)


"""
#Task 3 
Create two Series: Series1 with values [5, 10, 15, 20] and index ['w', 'x', 'y', 'z'],
and Series2 with values [2, 4, 6, 8] and index ['w', 'x', 'y', 'p']. 
Add, Subtract, Multiply and divide these two Series together. 
Handle possible NaN values.
"""


data_list2 = [5, 10, 15, 20]
labels2 = ['w', 'x', 'y', 'z']
data_list3 = [2, 4, 6, 8]
labels3 = ['w', 'x', 'y', 'p']
my_series2 = pd.Series(data_list2, index = labels2)
my_series3 = pd.Series(data_list3, index = labels3)

add_series = (my_series2 + my_series3).fillna(0)
mul_series = (my_series2 * my_series3).fillna(0)
div_series = (my_series2 / my_series3).fillna(0)

print(f"divided series{div_series}")
print(f"multiplied series{mul_series}")
print(f"added series{add_series}")


"""
#Task 4 
Create a DataFrame with at least 5 rows and use the head() method to display the first 3 rows. 
Then use the tail() method to display the last 2 rows. 
Also, try experimenting with the default value and negative arguments for the these methods.
"""


data = {'Name': ['name1', 'name2', 'name3', 'name4', 'name5'],
        'Age': [12,20,21,30,25],
        'City': ['Tbilisi', 'Kutaisi', 'Batumi', 'Khashuri', 'Zugdidi']
        }
df = pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))


"""
Task 5 
Create a Series from [15, 22, 15, 30, 22, 45, 30, 15].
Find the unique values, count how many unique values there are using nunique(),
and display the frequency of each value using value_counts().
"""


my_list3 = [15, 22, 15, 30, 22, 45, 30, 15]
my_series4 = pd.Series(my_list3)
unique_values = my_series4.nunique()
frequency_of_values = my_series4.value_counts()
print(f"unique values: {unique_values}")
print(f"frequency of values:\n{frequency_of_values}")


"""
Task 6 
Create a DataFrame with columns 'Item' and 'Cost' containing at least 5 items.
Add a new column called 'Tax' that is 10% of the Cost. 
Add another column called 'Total' which is Cost plus Tax. 
Then filter and display only the rows where Total is greater than 50.
"""


item_data = {
    'Item' : ['item1', 'item2', 'item3', 'item4', 'item5'],
    'Cost' : [10,20,30,60,70]
}

items_df = pd.DataFrame(item_data)

def calculate_tax(cost):
    tax = cost / 10
    return tax

items_df['Tax'] = items_df['Cost'].apply(calculate_tax)

def calculate_total(tax, cost):
    total = cost + tax
    return total

items_df['Total'] = items_df.apply(lambda row: calculate_total(row['Cost'], row['Tax']), axis = 1)
filtered_df = items_df[items_df['Total'] > 50]

print(filtered_df)



"""
Task 7 Create a DataFrame with columns 'Product', 'Category', 'Price', 'Stock' containing at least 8 products from different categories. Then perform the following operations:
• Use isnull() and notnull() to check for missing values
• Use value_counts() on the Category column to count products in each category
• Use nlargest() to find the top 3 most expensive products
• Use nsmallest() to find the 2 products with the lowest stock
"""


product_data = {
    'Product' :['product1', 'product2', 'product3', 'product4', 'product5', 'product6', 'product7', 'product8'],
    'Category' : ['category1', 'category2', 'category3', 'category4', 'category5', 'category6', 'category7', 'category8'],
    'Price': [10,20,30,40,50, 60,70,80],
    'Stock': [1,2,3,4,5,6,7,8]
}

product_df = pd.DataFrame(product_data)
null_values = product_df.isnull().values.any()
not_missing_values = product_df.notnull().values.any()
product_count = product_df['Category'].value_counts()
most_expensive_products = product_df.nlargest(3, 'Price', keep = 'first')
lowest_stock = product_df.nsmallest(2,'Stock', keep = 'first')
print(null_values)
print(not_missing_values)
print(product_count)
print(most_expensive_products)
print(lowest_stock)


"""
Task8 
Create a DataFrame with columns 'Student', 'Subject', 'Score', 'Attendance' containing at least 10
students with some duplicate student names taking different subjects. Then perform the
following operations:
• Use duplicated() to identify duplicate student names
• Use drop_duplicates() to remove duplicate student names keeping the first occurrence
• Use set_index() to set Student as the index
• Use loc[] to retrieve data for a specific student
• Use iloc[] to retrieve the first 3 rows
• Use query() method to find students with Score greater than 80 and Attendance greater
than 85
• Use between() to find students with scores between 70 and 90
"""

students_data = {
    'Student' : ['student1', 'student1', 'student3', 'student4', 'student5', 'student3', 'student7', 'student8', 'student9', 'student10'],
    'Subject' : ['math', 'science', 'physics', 'biology', 'english', 'chemistry', 'physics', 'english', 'math', 'biology'],
    'Score' : [10,90,30,40,50,60,70,80,90,100],
    'Attendance': [70, 90, 30, 100, 90, 95, 85, 75, 55, 60]
}

student_df = pd.DataFrame(students_data)

duplicate_values = student_df['Student'].duplicated().values.any()
remove_duplicates = student_df['Student'].drop_duplicates(keep = 'first')
index_column = student_df.set_index('Student', inplace = True)
specific_student = student_df.loc['student1']
first_three_rows = student_df.iloc[:3, :]
high_score_attendance = student_df.query('Score > 80 and Attendance > 85')
students_by_score = student_df[student_df['Score'].between(70,90)]

print(remove_duplicates)
#print(duplicate_values)
print(student_df)
print(specific_student)
print(first_three_rows)
print(high_score_attendance)
print(students_by_score)