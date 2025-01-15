import numpy as np
import pytest
from my_lin_alg import my_transpose, my_mat_prod

"""Test for my_transpose()"""


def test_my_transpose():
    X = np.array(
        [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9],
         [1, 4, 2],
         [3, 11, 5]])
    expected = np.transpose(X).tolist()
    assert my_transpose(X) == expected

    Z = np.array(
        [[3, 8],
         [5, 6],
         [8, 9],
         [1, 4],
         [3, 5]])
    expected2 = np.transpose(Z).tolist()
    assert my_transpose(Z) == expected2


"""Test for my_mat_prod()"""


def test_my_mat_prod():
    X = np.array(
        [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9],
         [1, 4, 2],
         [3, 11, 5]])
    Y = np.array(
        [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]])
    expected = np.dot(X, Y).tolist()
    assert my_mat_prod(X, Y) == expected

    Z = np.array(
        [[3, 8],
         [5, 6],
         [8, 9],
         [1, 4],
         [3, 5]])
    W = np.array(
        [[3, 8, 1, 3, 5],
         [5, 6, 2, 6, 8]])
    expected2 = np.dot(Z, W).tolist()
    assert my_mat_prod(Z, W) == expected2

    def test_my_mat_prod_error():
        """Unit test for incompatible case"""
    with pytest.raises(ValueError):
        A = np.array(
            [[1, 2, 3],
             [4, 5, 6]]
        )
        B = np.array(
            [[1, 2],
             [5, 7],
             [7, 8],
             [6, 5]]
        )
        my_mat_prod(A, B)
