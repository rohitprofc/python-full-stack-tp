#Arithmetic operations in numpy

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

#addition
print(np.add(arr1, arr2))

#substract
print(np.subtract(arr1, arr2))

#multiplication
print(np.multiply(arr1, arr2))

#division
print(np.divide(arr1, arr2))

#sum
print(np.sum(arr1))
print(np.sum(arr1, axis=0))

#min and max values
print(np.min(arr1))
print(np.max(arr1))

#mean
print(np.mean(arr1))

#sorting
print(np.sort(arr1)) #ascending
print(-np.sort(-arr1)) #decending