import numpy as np
arr = np.array([1, 2, 1, 3, 5, 0, 0, 0, 2, 3])
result = np.bincount(arr)
print(result)