import numpy as np
# Task 1
arr_1d = np.arange(1,10,1)
array_sum = arr_1d.sum()
array_prod = arr_1d.prod()
print(arr_1d, array_sum, array_prod)

# Task 2
arr_1d_1= np.arange(1,20,1)
print(arr_1d_1[3], arr_1d[8])

# Task 3
values = np.arange(25)
array = values.reshape(5,5)

print(array[0], array[1], array[:, 3], array[:,4])

# Task 4
a = [1,2,3,4]
b = [2,4,6,8]
addition_list = []
for i in range(len(a)):
    addition_list.append(a[i]+b[i])
print(addition_list)
mul_list = []
for i in range(len(a)):
    mul_list.append(a[i]*b[i])
print(mul_list)
angles_array = []
sine_array = []
for i in range(len(b)):
    angles_array.append(np.pi / b[i])
for i in range(len(angles_array)):
    sine_array.append(np.sin(angles_array[i]))
print(sine_array)

# Task 5
array_5 = np.random.randint(0, 50, size=20)
print(array_5)
mask = (40 > array_5) & (array_5 > 25)
filtered_array = array_5[mask]
print(filtered_array)

# Task 6
matrix = np.arange(25).reshape(5,5)
np.fill_diagonal(matrix, 0)
matrix_final = matrix*2
print(matrix_final)

# Task 7
array_7 = np.arange(1,10).reshape(3,3)
print(array_7)
print(array_7[1])
print(array_7[:,:-1])

# Task 8
array_8 = np.arange(6).reshape(2,3)
print(array_8)
transposed = array_8.T
print(transposed)

# Task 9
array_1 = np.arange(9).reshape(3,3)
array_2 = np.arange(3).reshape(1,3)
print(array_1, array_2)
result = array_1 + array_2
print(result)

# Task 10
array_10 = np.arange(16).reshape(4,4)
row,col = [0,2,3],[1,3,2]
print(array_10[row,col])