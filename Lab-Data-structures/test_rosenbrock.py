from rosenbrock_module import rosenbrock_func, create_grid, vec_eval
from rosenbrock_module import measure_time_distance
import numpy as np

"""Unit tests"""


def test_create_grid():  # test grid creation
    n = 2
    X, Y = create_grid(n)
    assert X.shape == (n+1, n+1)
    assert Y.shape == (n+1, n+1)
    assert np.isclose(X[0, 0], -3)
    assert np.isclose(Y[0, 0], -1)


def test_vec_eval():  # test vectorized evaluation
    n = 2
    X, Y, Z = vec_eval(n)
    assert Z.shape == (n+1, n+1)
    assert np.isclose(Z[0, 0], rosenbrock_func(X[0, 0], Y[0, 0]))


def test_measure_time_distance():  # test measuring time and distance
    n = 2
    vec_time, nonvec_time, min_value, distance = measure_time_distance(n)
    assert vec_time > 0
    assert nonvec_time > 0
    assert min_value >= 0
    assert distance >= 0
