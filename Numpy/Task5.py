import numpy as np

a=np.random.randint(0,50,20)

mask=(a>25) & (a<40)

print(a[mask])