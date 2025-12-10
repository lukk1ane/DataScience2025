import numpy as np
#1______________________________________________________________

a = np.arange(1,11)
print(a)

sum = a.sum()
product = a.prod()

print("Sum:", sum)
print("Product:", product)

print("______________________________________________________________")

#2______________________________________________________________

b = np.arange(21)

slice = b[3:9]

print("Slice from index 3 to 8:", slice)

print("______________________________________________________________")


#3______________________________________________________________

c = np.arange(25).reshape(5,5)

rows = c[:2, :]
columns = c[:, -2:]

print(f"First 2 rows: {rows}")
print(f"Last 2 columns: {columns}")
print("______________________________________________________________")

#4______________________________________________________________

a = np.array([1, 2, 3,4])
b = np.array([2,4,6,8])

addition = a + b    
multiplication = a * b  
sine_of_elements_b = np.sin(b)

print(f"Addition: {addition}")
print(f"Multiplication: {multiplication}")
print(f"Sine of elements in b: {sine_of_elements_b}")
print("______________________________________________________________")

#5______________________________________________________________

a = np.random.randint(1, 51, size = 20)

mask = (a > 25) & (a < 40)
b = a[mask]

print(b)
print("______________________________________________________________")

#6______________________________________________________________

a = np.arange(25).reshape(5,5)

np.fill_diagonal(a,0)
a *= 2

print(a)
print("______________________________________________________________")

#7

a = np.arange(1,10).reshape(3,3)

c = a[1:2, :-1]

print(c)
print("______________________________________________________________")

#8______________________________________________________________

a = np.arange(1,7).reshape(2,3)

print(f"Original array:\n{a}")

a = a.T

print(f"Transposed array:\n{a}")
print("______________________________________________________________")

#9______________________________________________________________

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1,4).reshape(1,3)

c = a + b
print(f"Array a + b:\n{c}")

print("______________________________________________________________")
#10______________________________________________________________

a = np.arange(1,17).reshape(4,4)

rows = [0, 2, 3]
cols = [1, 3, 2]

print(f"Original array:\n{a}")

b = a[rows, cols]
print(b)

