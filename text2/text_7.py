import numpy as np

A = np.array([[1, -1, 3],

              [-5, 3, 9],

              [1, 0, -2]])

eigenvalue, featurevector = np.linalg.eig(A)

print(eigenvalue)

print(featurevector)




