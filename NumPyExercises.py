import numpy as np


#task1
arr = np.arange(1,11)
arr_sum = np.sum(arr)
arr_prod = np.prod(arr)
print(arr_sum)
print(arr_prod)


#task2
arr = np.arange(0,20)
s_array = arr[3:8]
print(s_array)


#task3
arr = np.arange(25).reshape(5,5)
print(arr)


#task4
arr = np.arange(1,5)
arr1 = np.arange(2,9,2)

result = arr + arr1
result1 = arr * arr1
sines = np.sin(arr1)
print(sines)


#task5
arr = np.random.randint(0, 51, size=20)
mask = (arr > 25) & (arr < 40)
result = arr[mask]
print(result)


#task6
arr = np.arange(25).reshape(5,5)
np.fill_diagonal(arr, 0)

mask = ~np.eye(arr.shape[0], dtype=bool)
arr[mask] = arr[mask] * 2
print(arr)

#task7
arr = np.arange(9).reshape(3,3)
arr = np.delete(arr, 1, axis=0)
arr = np.delete(arr, 1, axis=1)

print(arr)

#task8
arr = np.arange(6).reshape(2,3)
arr = arr.T
print(arr)


#task9
arr = np.arange(9).reshape(3,3)
arr1 = np.arange(3)

result = arr + arr1
print(result)


#task10
arr = np.arange(16).reshape(4,4)
fi = arr[[0,2,3],[1,3,2]]
print(fi)
