import numpy as np

# task 1

# arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr1=np.arange(1,11)
total=np.sum(arr1)

print(total)
print("*********************")
# task 2

arr=np.arange(0,21)
print(arr[3:9])
print("*********************")

# task 3

arr=np.arange(0,25).reshape(5,5)
print(arr[:2,-2:])
print("*********************")

# task 4

a=np.arange(1,5)
b=np.arange(2,9,2)

arr=np.add(a,b)
arr2=np.multiply(a,b)
arr3=np.sin(b)
print(arr)
print(arr2)
print(arr3)
print("*********************")

# task 5

arr=np.random.randint(0,52,20)
print(arr)
print(arr[(arr>25)&(arr>40)])
print("*********************")

# task 6

arr6=np.arange(25).reshape(5, 5)
arr6=np.multiply(arr6,2)  #aq mititeba rato unda
np.fill_diagonal(arr6,0)

print(arr6)

print("*********************")

# task 7

arr7=np.arange(1,10).reshape(3,3)
print(arr7)
print(arr7[1,:-1])

print("*********************")

# task 8

arr8=np.arange(6).reshape(2,3)
print(arr8.T)

print("*********************")

# task 9

arr9=np.arange(9).reshape(3,3)
arr91=np.arange(3).reshape(1,3)
print(arr9)
print(arr91)
print(arr9+arr91)

print("*********************")


# task 10

arr10=np.arange(16).reshape(4,4)
r=[0,2,3]
c=[1,3,2]
print(arr10)
print(arr10[r,c])