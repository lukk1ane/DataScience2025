import numpy as np

arr1 = np.arange(1,11)
print(np.sum(arr1))
print(np.prod(arr1))

arr2 = np.arange(20)
print(arr2[3:8])

arr3 = np.arange(25).reshape(5, 5)
print(arr3[2:, -2:])

a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])
print(a + b)
print(a * b)
print(np.sin(b))

arr4 = np.random.randint(0, 50, size=20)
mask = (arr4 > 25) & (arr4 < 40)
print(arr4[mask])

arr5 = np.arange(25).reshape(5, 5)
np.fill_diagonal(arr5, 0)
arr5 = np.where(arr5 != 0, arr5 * 2, 0)
print(arr5)

arr6 = np.arange(1, 10).reshape(3, 3)
print(arr6[2])
print(arr6[:, :-1])

arr7 = np.arange(1, 7).reshape(2, 3)
print(arr7.T)

arr7 = np.arange(1, 10).reshape(3, 3)
arr8 = np.array([1, 2, 3])
print(arr7 + arr8)

arr9 = np.arange(1, 17).reshape(4, 4)
print(arr9[[0, 2, 3], [1, 3, 2]])


