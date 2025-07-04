import numpy as np

arr = np.array([1, -2, 3, -4, 5])
print(arr)
new_arr = np.where(arr < 0, 0, arr)

print(new_arr)