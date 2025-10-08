import numpy as np

a=np.arange(25).reshape(5, 5);

a [ [0,1,2,3,4] , [0,1,2,3,4] ]=0
a*=2;
print(a)