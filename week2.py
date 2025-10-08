import numpy as np

#task1
arr = np.array([1, 2, 3, 4, 5, 6,7,8,9,10])
s=np.sum(arr)
product=np.prod(arr)

#task2
arr = np.arange(0, 21)
subset = arr[3:9]

#task3
arr=np.arange(25).reshape(5,5)
result=arr[:2,-2]

#task4
arr1=np.array([1,2,3,4])
arr2=np.array([2,4,6,8])

add=arr1+ arr2
mul=arr1* arr2
sin_b = np.sin(arr2)

#task5
arr = np.random.randint(0, 51, size=20)
mask = (arr > 25) & (arr < 40)
filtered = arr[mask]

#task6
arr = np.arange(25).reshape(5, 5)
np.fill_diagonal(arr, 0)
arr = arr * 2
print(arr)

#task7
arr = np.arange(1, 10).reshape(3, 3)
second_row = arr[1, :]

#task8
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
transposed = arr.T


#task9
arr_3x3 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
arr_1x3 = np.array([10, 20, 30])

res = arr_3x3 + arr_1x3

#task10

arr = np.arange(16).reshape(4, 4)
rows = [0, 2, 3]
cols = [1, 3, 2]
selected = arr[rows, cols]
