#Memory of Array and List

import numpy as np
import sys

a=np.array([1,4,5,6])
print(a)

ele_size_array = a.itemsize
print(f"Element size in numpy array: {ele_size_array}")

array_size = a.size
print(f"Total size of numpy array: {array_size}")

total_array_size = ele_size_array * array_size
print(f"Total numpy array bit size is {total_array_size}")

b=[1,4,5,6]
print(b)

ele_size_list = sys.getsizeof(b)
print(f"Element size in list: {ele_size_list}")

list_size = len(b)
print(f"Total size of list: {list_size}")

total_list_size = ele_size_list * list_size
print(f"Total numpy array bit size is {total_list_size}")