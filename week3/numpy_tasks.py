import numpy as np 

# 1. Array Creation and Basic Operations
arr1 = np.arange(1,11)
summ = np.sum(arr1)
product = np.prod(arr1)
print(arr1)
print(f" sum={summ}, product={product}")

#  2. Array Indexing and Slicing
arr2 = np.arange(21)
print(arr2)
print("elements from index 3 to 8:" , arr2[3:9])

#  3. 2D Array Manipulation
arr3= np.arange(25).reshape(5,5)
first_two_rows = arr3[0:2, :]
last_two_colls = arr3[:, -2:]
print(arr3)
print(first_two_rows)
print(last_two_colls)

#  4. Element-wise Mathematical Operations
a=np.array([1,2,3,4])
b=np.array([2,4,6,8])
print("add=", np.add(a,b))
print("mult=", np.multiply(a,b))
print("sine=", np.sin(b))

#  5. Fancy Indexing and Boolean Masking
arr5 = np.random.randint(0,50,20)
mask = (arr5>25) & (arr5<40)

#  6. Multi-dimensional Array Challenge
arr6 = np.arange(25).reshape(5,5)
np.fill_diagonal(arr6, 0)
arr6 *= 2

#  7. Array Slicing
arr7 = np.arange(1,10).reshape(3,3)
print(arr7[1, :-1])

#  8. Transposing an Array
arr8=np.arange(6).reshape(2,3)
T_arr8 = np.transpose(arr8)

#  9. Broadcasting
arr9 = np.arange(9).reshape(3,3)
arrr9 = np.arange(3).reshape(1, 3)
brod_sum = arr9 + arrr9

#  10. Fancy Indexing with 2D arrays
arr10 = np.arange(16).reshape(4,4)
fanc_arr10 = arr10[[0,2,3],[1,3,2]]
print(arr10)
print(fanc_arr10)

