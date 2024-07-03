#linspace and random functions in numpy

import numpy as np

ab = np.linspace(1, 3, 5, endpoint=False, retstep=True)
print(ab)

b = np.random.random((4,3))
print(b)