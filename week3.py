# Numpy tasks
import numpy as np

# task 1
num1 = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
sum1 = 0
product1 = 1
for i in num1:
    sum1 += i
    product1 *= i
print("=================task1================")
print(sum1)
print(product1)

# task 2
num2 = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20))
print("=================task2================")
print(num2[3:9])

# task 3
num3 = np.arange(25).reshape(5,5)
print("=================task3================")
print(num3[0:2])
print(num3[0:5, 3:5])

# task 4
a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])

print("=================task4================")
print(a+b)
print(a*b)
print(np.sin(b))

# task 5
num5 = np.random.randint(50, size=(1, 20))
print("=================task5================")
print(num5)
print(num5[(num5 > 25) & (num5 < 40)])

# task 6
num6 = np.arange(25).reshape(5,5)
np.fill_diagonal(num6, 0)
num6 *= 2
print("=================task6================")
print(num6)

# task 7
num7 = np.arange(1, 10).reshape(3,3)
print("=================task7================")
print(num7[1:2])
print(num7[0:3, 0:2])

# task 8
num8 = np.random.randint(50, size=(2, 3))
print("=================task8================")
print(num8)
print(np.transpose(num8))

# task 9
m = np.random.randint(50, size=(3, 3))
n = np.random.randint(50, size=(1, 3))
print("=================task9================")
print(m)
print(n)
print(m+n)

# task 10
num10 = np.random.randint(50, size=(4, 4))
print("=================task10================")
print(num10)
print(num10[[0, 2, 3], [1, 3, 2]])
