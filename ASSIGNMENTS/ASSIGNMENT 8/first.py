import numpy as np

# (4x2) array with random values
random_array = np.random.rand(4, 2)
print("Random 4x2 array:\n", random_array)

# (4x2) empty array (uninitialized values)
empty_array = np.empty((4, 2))
print("\nEmpty 4x2 array:\n", empty_array)

# (3x5) array filled with zeros
zeros_array = np.zeros((3, 5))
print("\n3x5 array of zeros:\n", zeros_array)

# (4x3x2) array filled with ones
ones_array = np.ones((4, 3, 2))
print("\n4x3x2 array of ones:\n", ones_array)

