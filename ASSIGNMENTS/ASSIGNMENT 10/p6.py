import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])
b = np.array([9, -6, 17])

sol = np.linalg.solve(A, b)
print("Solution using linalg.solve:\n", sol)

A_inv = np.linalg.inv(A)
sol2 = A_inv.dot(b)
print("Solution using inverse:\n", sol2)