#Flatten Method
#converting higher dimensional array to 1D array

import numpy as np

a = np.array([[1,4,7], [2,5,8], [3,6,9]])
print(a)

print("---------------------------")

print(a.flatten())

print("---------------------------")

#Row Major
print(a.flatten('F'))