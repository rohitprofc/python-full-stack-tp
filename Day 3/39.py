#Array Slicing

import numpy as np

a = [1, 2, 3, 4, 5, 6, 7]
b = np.array(a) #convert list to array

print(b)
type(b)

print(b[2:5])
print(b[:4])
print(b[-1:-3:-1])
print(b[-3:-1])
print(b[0:5:2])
print(b[2:5])
print(b[::2])