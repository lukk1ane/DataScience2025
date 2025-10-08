import numpy as np

#Task 1
arr1 = np.arange(1, 11)
sum_elements = np.sum(arr1)
product_elements = np.prod(arr1)

#Task 2
arr2=np.arange(0, 21)
arrr2=arr2[3:9]

#Task 3
arr3=np.arange(25).reshape(5, 5)
result = arr3[:2, -2:]

#Task 4
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
addition = a+b
multiplication = a*b
sine = np.sin(b)

#Task 5
arr = np.random.randint(0, 51, size=20)
filtered = arr[(arr > 25) & (arr < 40)]

#Task 6
arr6 =  np.arange(25).reshape(5, 5)
np.fill_diagonal(arr6, 0)
arr6 = arr6 *2

#Task 7
arr7 = np.arange(1,10).reshape(3,3)
result=arr7[1, :-1]

#Task 8
arr8 = np.arange(6).reshape(2,3)
transpose = arr8.transpose()

#Task 9
arr9 = np.arange(9).reshape(3,3)
arrr9 = np.arange(3)
result9= arr9 + arrr9

#Task 10
arr10 = np.arange(16).reshape(4,4)
rows = [0, 2, 3]
cols = [1, 3, 2]

result10 = arr10[rows, cols]
