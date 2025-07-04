import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

arr = np.nan_to_num(arr, nan=0)
print(arr)

interchanged = arr[:, :3].T
print("Replaced NaN and Transposed first 3 columns:\n", interchanged)