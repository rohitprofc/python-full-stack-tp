#Performance

import numpy as np
import time
SIZE = 10

#declaring two lists with range
l1 = range(SIZE)
l2 = range(SIZE)

#delcaring array
arr1 = np.arange(SIZE)
arr2 = np.arange(SIZE)

#Time
initial_t = time.time()
print(f"Time: {initial_t}")

l3 = [(a*b) for a,b in zip(l1,l2)]
print(f"List multiplication time: {time.time()-initial_t}")
initial_t = time.time()

arr3 = arr2 * arr1
print(f"Multiplication of array: {time.time()-initial_t}")