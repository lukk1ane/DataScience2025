import numpy as np

# Slide problems

# Task 1
a = np.arange(25).reshape(5, 5)

first = a[:, 1::2]

second = a[1::2, 0:3:2]

third = a[4, :]

# Task 2
b = np.arange(25).reshape(5, 5)
positions = [[1, 2, 3, 4], [0, 1, 2, 3]]
res1 = b[positions]

x = b > 3
res2 = b[x]

# Task 3

c = np.arange(-15, 15).reshape(5, 6) ** 2

max_each_row = np.max(c, axis=1)
mean_each_row = np.mean(c, axis=1)
min_element = np.min(c)

mask = c == min_element
position = np.where(mask)

# HomeWork problems


# Task 1
task1 = np.arange(1, 11)
jami = np.sum(task1)
namravli = np.prod(task1)

# Task 2
task2 = np.arange(0, 21)
task2res = task2[3:9]

# Task 3

task3 = np.arange(25).reshape(5, 5)
first_two_rows = task3[:2, :]
last_two_cols = task3[:, -2:]

# Task 4

a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])
summ = a + b
prod = a * b
sin = np.sin(b)

# Task 5
task5 = np.random.randint(0, 51, 20)
mask1 = (task5 > 25) & (task5 < 40)

# Task 6

task6 = np.arange(25).reshape(5, 5)
np.fill_diagonal(task6, 0)
task6 *= 2

# Task 7
task7 = np.arange(1, 10).reshape(3, 3)
task7_res = task7[1, :-1]

# Task 8
task8 = np.arange(6).reshape(2, 3)
transp = np.transpose(task8)

# Task 9
x = np.arange(9).reshape(3, 3)
y = np.arange(3).reshape(1, 3)
task9_res = x + y

# Task 10

task10 = np.arange(16).reshape(4, 4)
indexes = task10[[0,2,3],[1,3,2]]
