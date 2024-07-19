#Implementing Matrices Using Numpy Array

import numpy as np

print(np.zeros((4,3)))
print(np.ones((3,5)))
print(np.identity(4))

#print 30 in 3x3
print(np.ones((3,3), dtype=int)*30)

#other way
print(np.random.randint(30,31,(3,3)))