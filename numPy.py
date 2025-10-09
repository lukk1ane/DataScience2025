# 1. Array Creation and Basic Operations
# Task: Create a 1D NumPy array containing numbers from 1 to 10. Then, calculate the sum and
# product of all elements in the array.


import numpy as np
arr= np.arange(1,11)


total = np.sum(arr)
product = np.prod(arr)

print("sum of numebrs:", total)
print("product:", product)



# 2. Array Indexing and Slicing
# Task: Create a 1D array with numbers from 0 to 20. Extract the elements from index 3 to 8.

arr=np.arange(0,21)
sliced= arr[3:9]
print("extract the elements from index 3 to 8: ", sliced)




# 3. 2D Array Manipulation
# Task: Create a 5x5 array with values from 0 to 24. Extract the first two rows and the last two
# columns.


arr = np.arange(0, 25)
matrixed = arr.reshape(5,5)


result=matrixed[:2,-2:]
print(result)


# 4. Element-wise Mathematical Operations
# Task: Create two arrays: a = [1, 2, 3, 4] and b = [2, 4, 6, 8]. Perform element-wise addition,
# multiplication, and calculate the sine of each element in b.


a=np.array([1,2,3,4])
b=np.array([2,4,6,8])

print(a+b, a*b, np.sin(b))


# 5. Fancy Indexing and Boolean Masking
# Task: Create a 1D array with random integers between 0 and 50 (size 20). Extract elements that
# are greater than 25 and less than 40 using boolean masking.
arr = np.random.randint(0, 50, 20)
masking = (arr > 25) & (arr < 40)
result = arr[masking]
print(result)




# 6. Multi-dimensional Array Challenge
# Task: Create a 5x5 matrix using np.arange(25).reshape(5, 5). Set the diagonal elements to zero
# and multiply all other elements by 2.


arr = np.arange(25).reshape(5, 5)
np.fill_diagonal(arr, 0)

arr[arr != 0] = arr[arr != 0] * 2

print(arr)



# 7. Array Slicing
# Task: Create a 3x3 NumPy array with values from 1 to 9. Extract the second row and all columns
# except the last one.


arr = np.arange(1,10).reshape(3, 3)

result = arr[1, :-1]
print("extracted slice:")
print(result)


# 8. Transposing an Array Task: Create a 2x3 array and transpose it. 


arr = np.arange(1,7).reshape(2,3)
arrT = arr.T
print("transposed:")
print(arrT)

# 9. Broadcasting Task: Create a 3x3 array and a 1x3 array. 
# Use broadcasting to add the 1x3 array to each row of the 3x3 array. 


A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


B = np.array([10, 20, 30])


C = A + B
print(C)



# 10. Fancy Indexing with 2D arrays Task: 
# Create a 4x4 array and use fancy indexing to extract the elements at positions (0, 1), (2, 3), and (3, 2)



arr = np.arange(16).reshape(4, 4)

rows = [0, 2, 3]
cols = [1, 3, 2]
result = arr[rows, cols]
print("extracted elements:")
print(result)
