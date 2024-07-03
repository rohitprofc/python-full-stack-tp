#2D and 3D arrays

import numpy as np

print("2D-Array")
a = np.array(np.random.randint(10, 45,(6,2)))
print(a)

print("---------------------------------")

print("3D Array-2,1,6")
n = (2, 1, 6) #3D
print(np.reshape(a, n))

print("---------------------------------")

#Reshaping
print("3D Array-3,2,2")
n = (3, 2, 2)
print(np.reshape(a, n))