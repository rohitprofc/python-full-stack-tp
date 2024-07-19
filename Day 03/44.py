#Copy and View Array

import numpy as np

a = np.array([11,22,33,44,55])
print(a)

#copy array
b = a.copy()
print(b)

#replacing values
b[3] = 90
print(b)