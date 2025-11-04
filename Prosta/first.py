import numpy as np

a = np.arange(25).reshape(5, 5)
yellow = a[-1, : ]
red = a[: , 1::2]
blue = a[1::2, :3:2]
print(yellow)
print(red)
print(blue)

mask = a[[0,1,2,3,4],[1,2,3,4,5]]
print(mask)


