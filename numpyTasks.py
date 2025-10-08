import numpy as np
#Task 1
arr1 = np.arange(1, 11)
s = arr1.sum()
prod = arr1.prod()

#Task 2
arr2 = np.arange(0,21)
slice_arr2 = arr2[3:9]

#Task 3
arr3 = np.arange(25).reshape((5,5))
arr31 = arr3[:2, -2:]

#Task 4
arr41 = np.arange(1,5)
arr42 = np.array([2,4,6,8])
a3 = arr41 + arr42
m3 = arr41 * arr42
sin_b = np.sin(arr42)

#Task 5
arr5 = np.random.randint(0, 50, size=20)
mask = (arr5 > 25) & (arr5 < 40)
filtered_arr5 = arr5[mask]

#Task6
arr6 = np.arange(25).reshape((5,5))
np.fill_diagonal(arr6, 0)
arr6=arr6*2

#Task 7
arr7 = np.arange(1,10).reshape((3,3))
arr71 = arr7[1, :-1]

#Task8
arr8 = np.arange(1, 7).reshape(2,3)
arr81 = arr8.T

#Task 9
arr91 = np.arange(1,10).reshape(3,3)
arr92 = np.array([1,2,3])
arr9_broadcasted = arr91 + arr92

#Task 10
arr10 = np.arange(1,17).reshape(4,4)
indexes = arr10[[0,2,3],[1,3,2]]
