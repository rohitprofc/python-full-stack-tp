#Inserting Element in Array
#Syntax:
#insert(array, index, value, axis)
    #axis-0 for row
    #axis-1 for column

#for 1D array

import numpy as np

a = np.array(np.random.randint(0,51,(1,10)))
print(a)

print(np.insert(a,4,51))

#for 2D array

a = np.array(np.random.randint(0,51,(3,3)))
print(np.insert(a,2,0,0)) #for whole row

a = np.array(np.random.randint(0,51,(3,3)))
print(np.insert(a,2,0,1)) #for whole column