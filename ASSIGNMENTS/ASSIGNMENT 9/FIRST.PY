import numpy as np

arr1d = np.array([10, 20])
arr2d = np.array([[1, 2], [3, 4]])

# Reshape 1D array to 2D row to stack vertically
combined = np.vstack((arr2d, arr1d))
print("Combined array:\n", combined)
