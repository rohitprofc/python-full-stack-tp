#Converting one datatype to another datatype of numpy array

import numpy as np

a=np.array([1,4,5,6])
print(a, a.dtype)

b=a.astype('float64')#converting int to float
c=a.astype('<U21')#converting int to string

print(b, b.dtype)
print(c, c.dtype)