import numpy as np

#Task 1
arr = np.arange(1, 11)
arr_sum = np.sum(arr)
arr_prod = np.prod(arr)

#Task 2
arr = np.arange(1,21)
x = arr[3:9]

#Task 3
arr = np.arange(0, 25).reshape(5,5)
subset = arr[:2, -2:]

#Task 4
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])
addition = a + b
multiplication = a * b
sine_b = np.sin(b)

#Task 5
arr = np.random.randint(0, 51, size=10)
arr_greater = arr[(arr > 25) & (arr < 40)]

#Task 6
arr = np.arange(25).reshape(5,5)
arr = 2 * arr
np.fill_diagonal(arr, 0)

#Task 7
arr = np.arange(1,10).reshape(3,3)
y = arr[1,:-1]

#Task 8
arr = np.arange(1,7).reshape(2,3)
arr_tr = arr.transpose()

#Task 9
arr = np.arange(1,10).reshape(3,3)
arr1 =  np.arange(1,4).reshape(1,3)
arr2 = arr + arr1

#Task 10
arr = np.arange(1,17).reshape(4,4)
rows = np.array([0, 2, 3])
cols = np.array([1, 3, 2])
elements = arr[rows, cols]
print(arr)
print(elements)