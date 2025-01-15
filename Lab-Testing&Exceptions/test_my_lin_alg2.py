import numpy as np
import pytest
from my_lin_alg import my_transpose, my_mat_prod

"""For part c)"""
"""Tests for my_mat_prod() using try-except block"""

X = np.array(  # 5 x 3 matrix
    [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 4, 2],
     [3, 11, 5]])
Y = np.array(  # 3 x 4 matrix
    [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]])
Z = np.array(   # 3 x 3 matrix
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])
W = np.array(  # 2 x 5 matrix
    [[3, 8, 1, 3, 5],
     [5, 6, 2, 6, 8]])

# Case when matrix product is successfuly calculated
try:
    print(my_mat_prod(X, Y))
except ValueError:
    print("Dimensions are incompatible with multiplication")

# Case when matrix product is failed
try:
    print(my_mat_prod(X, W))
except ValueError:
    print("Dimensions are incompatible for multiplication")

"""For part d)"""
"""Tests for properties"""


def test_my_transpose_properties():  # testing my_transpose()
    """Testing transpose of a transpose is the original matrix"""
    assert np.array_equal(my_transpose(my_transpose(Z)), Z)  # square matrix
    assert np.array_equal(my_transpose(my_transpose(X)), X)  # n_row > n_col
    assert np.array_equal(my_transpose(my_transpose(W)), W)  # n_row < n_col

    """Testing multiplication with a scalar by randomized test"""
    scalar = np.random.randint(20)
    X_scaled = [[scalar * i for i in row] for row in X]
    assert np.array_equal(my_transpose(X_scaled), [[scalar * i for i in row]
                                                   for row in my_transpose(X)])
    """Testing transpose of an identity matrix"""
    I_3 = np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]])
    assert np.array_equal(my_transpose(I_3), I_3)


def test_my_mat_prod_properties():  # testing my_mat_prod()
    """Testing multiplication with a scalar by randomized test"""
    scalar = np.random.randint(20)
    X_scaled = [[scalar * i for i in row] for row in X]
    expected = [[scalar * i for i in row] for row in my_mat_prod(X, Z)]
    assert np.array_equal(my_mat_prod(X_scaled, Z), expected)

    """Testing multipliacation with identity matrix"""
    I_4 = np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]])
    assert np.array_equal(my_mat_prod(Y, I_4), Y)


"""Tests for edge & error cases"""


def test_my_transpose_edge_error():  # testing my_transpose()
    E = [[]]
    assert my_transpose(E) == []  # empty matrix
    assert my_transpose([[5]]) == [[5]]  # single element matrix

    A = [[1, 2, 3]]
    expected_A = [[1], [2], [3]]
    assert my_transpose(A) == expected_A  # one-row matrix
    assert my_transpose(expected_A) == A  # one-column matrix


def test_my_mat_prod_edge_error():  # testing my_mat_prod()
    E_1 = [[]]
    E_2 = [[]]
    with pytest.raises(ValueError):
        my_mat_prod(E_1, E_2)  # empty matrices
    B = [[5]]
    C = [[3]]
    assert my_mat_prod(B, C) == [[15]]  # single element matrices
    W_zero = np.array(
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]])
    zero = np.array(
        [[0, 0, 0, 0],
         [0, 0, 0, 0]])
    assert np.array_equal(my_mat_prod(W, W_zero), zero)  # with zero matrix
