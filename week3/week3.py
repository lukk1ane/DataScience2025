import numpy as np

#task1
my_list1 = [1,2,3,4,5,6,7,8,9,10]
my_np_arr = np.array(my_list1)
total_sum = np.sum(my_np_arr)
total_prod = np.prod(my_np_arr)
print(total_sum)
print(total_prod)

#task2
my_list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
my_np_arr2 = np.array(my_list2)
split_arr = my_np_arr2[3:8]
print(split_arr)

#task3
my_np_arr3 = np.arange(25).reshape(5,5)

first_two_rows = my_np_arr3[:2, :]
last_two_columns = my_np_arr3[:, -2:]
print(first_two_rows)
print(last_two_columns)

#task4
a = np.array([1,2,3,4])
b = np.array([2,4,6,8])

sum_arr = a + b
mul_arr = a*b
sin_b = np.sin(b)

print(sum_arr)
print(mul_arr)
print(sin_b)

#task5
my_np_arr5 = np.random.randint(0,51, size = 20)

my_elements = (my_np_arr5>25) & (my_np_arr5 < 40)
filtered_el = my_np_arr5[my_elements]
print(filtered_el)

#task6
my_np_arr6 = np.arange(25).reshape(5,5)

my_np_arr6[np.diag_indices_from(my_np_arr6)] = 0
my_np_arr6 *= 2

print(my_np_arr6)

#task7
my_np_arr7 = np.arange(1,10).reshape(3,3)
extracted_row = my_np_arr7[1,:]
extracted_columns = my_np_arr7[:,:-1]
print(extracted_row)
print(extracted_columns)

#task8
my_np_arr8 = np.arange(6).reshape(2,3)
transposed_arr = np.transpose(my_np_arr8)

print(transposed_arr)

#task9
arr1 = np.arange(9).reshape(3,3)
arr2 = np.arange(3).reshape(1,3)

matrix_sum = arr1 + arr2

print(matrix_sum)

#task10
my_np_arr10 = np.arange(16).reshape(4,4)
rows = [0,2,3]
columns = [1,3,2]
extracted_elements = my_np_arr10[rows,columns]

print(extracted_elements)