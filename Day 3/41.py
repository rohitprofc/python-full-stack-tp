#Resize

import numpy as np

a = np.array([[5,1], [4,5], [9,6]]) #2D Array

print(np.resize(a, (2,3)))
print("-----------------------")
print(np.resize(a, (1,4)))
print("-----------------------")
print(np.resize(a, (6,1)))
