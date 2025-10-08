#  Task: Create a 1D NumPy array containing numbers from 1 to 10. Then, calculate the sum and product of all elements in the array.
import numpy as np
arr = np.arange(1, 11) 
sum = np.sum(arr) 
product = np.prod(arr) 

print(arr)


# Task: Create a 1D array with numbers from 0 to 20. Extract the elements from index 3 to 8.
arr=np.arange(0,21)
extr_arr= arr[3:9]
print(extr_arr)

# Task: Create a 5x5 array with values from 0 to 24. Extract the first two rows and the last two columns.
matrix = np.arange(25).reshape(5, 5) 
extracted = matrix[:2, -2:]  
print(extracted)

# Task: Create two arrays: a = [1, 2, 3, 4] and b = [2, 4, 6, 8]. Perform element-wise addition, 
# multiplication, and calculate the sine of each element in b.
a = np.array([1, 2, 3, 4]) 
b = np.array([2, 4, 6, 8]) 
addition = a + b
multiplication = a * b 
sinb = np.sin(b)  
print(addition)
print(multiplication)       
print(sinb)

#Task: Create a 1D array with random integers between 0 and 50 (size 20). Extract elements that
# are greater than 25 and less than 40 using boolean masking.
random_array = np.random.randint(0, 50, size=20)  
masked_array = random_array[(random_array > 25) & (random_array < 40)] 
print(masked_array)

# Task: Create a 5x5 matrix using np.arange(25).reshape(5, 5). Set the diagonal elements to zero
# and multiply all other elements by 2.
matrix = np.arange(25).reshape(5, 5)  
np.fill_diagonal(matrix, 0) 
matrix = matrix * 2 
print(matrix)


#Task: Create a 3x3 NumPy array with values from 1 to 9. Extract the second row and all columns
arr = np.arange(1, 10).reshape(3, 3)  
second_row = arr[1, :]
print(second_row)

#  Task: Create a 2x3 array and transpose it
arr = np.arange(6).reshape(2, 3)  
transposed_arr = arr.T  
print(arr)
print(transposed_arr)

# Task: Create a 3x3 array and a 1x3 array. Use broadcasting to add the 1x3 array to each row of
# the 3x3 array.
arr1 = np.arange(9).reshape(3, 3)  
arr2 = np.array([1, 2, 3])  
result = arr1 + arr2 
print(result)

# Task: Create a 4x4 array and use fancy indexing to extract the elements at positions (0, 1), (2, 3), and (3, 2).
arr = np.arange(16).reshape(4, 4)
fancyindxel=arr[[0,2,3],[1,3,2]]
print(fancyindxel)