import numpy as np

# task 1
arr = np.arange(1, 11)
print(arr.sum(), arr.prod())

# task 2
arr = np.arange(0, 20)
slice = arr[3:8]
print(slice)

# task 3
arr = np.arange(25).reshape(5, 5)
print('first 2 rows:', arr[:2], 'last 2 columns:', arr[:, -2:], sep='\n')


# task 4
print("------TASK 4------")
a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])
print(a + b, a * b, np.sin(b), sep='\n')

print('--------Task 5--------')
arr = np.random.randint(0,51, size=20)
print(arr)
mask = (arr > 25) & (arr < 40)
print(arr[mask])

print('----Task 6-----')
arr = np.arange(25).reshape(5, 5)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if i == j:
            arr[i,j] = 0
        else:
            arr[i,j] = arr[i,j] ** 2
print(arr)

print('----Task 7----')
arr = np.arange(1, 10).reshape(3, 3)
print(arr[1, :-1])

print('----Task 8----')
arr = np.array([[1,2,3],[4,5,6]])
print(arr, arr.T, sep='\n')

print('----Task 9----')
arr = np.arange(9).reshape(3, 3)
arr2 = np.array([10, 20, 30])
print(arr + arr2.T)

print('----Task 10----')
arr = np.arange(16).reshape(4,4)
print(arr)
print(arr[[0, 2, 3],[1, 3, 2]])