"""Codes for testing calculations"""

import numpy as np
# The command below allows you to call my_transpose and my_mat_prod as if they
# were functions defined within this module
from my_lin_alg import my_transpose, my_mat_prod  # import functions

# 5x3 matrix
X = np.array(
    [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 4, 2],
     [3, 11, 5]])
# 3x4 matrix
Y = np.array(
    [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]])
# 5x2 matrix - added
Z = np.array(
    [[3, 8],
     [5, 6],
     [8, 9],
     [1, 4],
     [3, 5]])
# 2x5 matrix - added
W = np.array(
    [[3, 8, 1, 3, 5],
     [5, 6, 2, 6, 8]])

# 1. Compare matrix transpose
print("Test 1 for my_transpose vs np.transpose")
Transpose_1 = my_transpose(X)
Transpose_2 = np.transpose(X).tolist()  # convert to list form
print("Result of my_transpose:")
print(Transpose_1)
print("Result of np.transpose:")
print(Transpose_2)
print("Are they exactly the same?", Transpose_1 == Transpose_2)  # True/False

print("Test 2 for my_transpose vs np.transpose")
Transpose_3 = my_transpose(Z)
Transpose_4 = np.transpose(Z).tolist()  # convert to list form
print("Result of my_transpose:")
print(Transpose_3)
print("Result of np.transpose:")
print(Transpose_4)
print("Are they exactly the same?", Transpose_3 == Transpose_4)  # True/False

# 2. Compare matrix multiplication
print("Test 1 for my_mat_prod vs numpy.dot")
Production_1 = my_mat_prod(X, Y)
Production_2 = np.dot(X, Y).tolist()  # convert to list form
print("Result of my_mat_prod:")
print(Production_1)
print("Result of np.dot:")
print(Production_2)
print("Are they exactly the same?", Production_1 == Production_2)  # True/False

print("Test 2 for my_mat_prod vs numpy.dot")
Production_3 = my_mat_prod(Z, W)
Production_4 = np.dot(Z, W).tolist()  # convert to list form
print("Result of my_mat_prod:")
print(Production_3)
print("Result of np.dot:")
print(Production_4)
print("Are they exactly the same?", Production_3 == Production_4)  # True/False
