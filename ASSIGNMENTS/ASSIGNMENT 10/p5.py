import numpy as np

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

avg = (arr1 + arr2) / 2
print("Average of NumPy 1D arrays:\n", avg,"\n")

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
print(array1)
print(array2)
combined = np.concatenate((array1.flatten(), array2.flatten()))
mean_val = np.mean(combined)
median_val = np.median(combined)
unique, counts = np.unique(combined, return_counts=True)
mode_val = unique[np.argmax(counts)]

print("Mean value:", mean_val)
print("Median value:", median_val)
print("Mode value:", mode_val)