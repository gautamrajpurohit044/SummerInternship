import numpy as np
print("\n4) Practice operations on a 2D array")

sample_array = np.array([
    [3, 7, 2],
    [5, 1, 9]
])

# Maximum and minimum values
max_val = np.max(sample_array)
min_val = np.min(sample_array)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

# Number of rows and columns
rows, cols = sample_array.shape
print("Rows:", rows)
print("Columns:", cols)

# Selecting elements
print("All elements:\n", sample_array)
print("Element at (1,2):", sample_array[1, 2])
print("First row:", sample_array[0])
print("First column:", sample_array[:, 0])

# Sum of all values using a for loop
total_sum = 0
for row in sample_array:
    for val in row:
        total_sum += val
print("Total sum of elements:", total_sum)

# Arithmetic operations
other_array = np.array([
    [1, 1, 1],
    [1, 1, 1]
])

added = sample_array + other_array
subtracted = sample_array - other_array
multiplied = sample_array * other_array
divided = sample_array / other_array

print("\nAdded:\n", added)
print("Subtracted:\n", subtracted)
print("Multiplied:\n", multiplied)
print("Divided:\n", divided)