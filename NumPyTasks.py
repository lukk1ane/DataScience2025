import numpy as np

# task 1
arr = np.arange(1,11)
sum = np.sum(arr)
prod = np.prod(arr)
print("Sum:" , sum)
print("Product:" , prod)

# task 2
ar = np.arange(21)
print(ar[3:8])

# task 3
c = np.arange(25).reshape(5,5)
print(c[0:2, 3:])

# task 4
a = np.arange(1,5)
b = np.arange(2,9,2)
print(np.add(a,b))
print(np.multiply(a,b))
print(np.sin(b))

# task 5
array = np.random.randint(0, 51, size = 20)
mask = (array > 25) & (array < 40)
print(array[mask])

# task 6
arra = np.arange(25).reshape(5,5)
np.fill_diagonal(arra,0)
arra = arra * 2
print(arra)

# task 7
array = np.arange(1,10).reshape(3,3)
print(array[1,:2])

# task 8
array1 = np.arange(6).reshape(2,3)
print(array1.T)

# task 9
array2 = np.arange(9).reshape(3,3)
array3 = np.arange(3).reshape(1,3)
print(array2 + array3)

# task 10
array4= np.arange(16).reshape(4,4)
rows = [0, 2, 3]
cols = [1, 3, 2]
print(array4[rows,cols])
