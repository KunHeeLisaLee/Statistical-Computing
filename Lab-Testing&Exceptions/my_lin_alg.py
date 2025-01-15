"""Codes for matrix algebra"""

"""1) Matrix transpose"""

"""Expected input X: original matrix
Expected output X_transpose: trasposed matrix of X"""


def my_transpose(X):
    n_row = len(X)  # n_row of original matrix X
    n_col = len(X[0])  # n_col of original matrix X

    X_transpose = [[0] * n_row for _ in range(n_col)]  # create and set dim

    for i in range(n_row):
        for j in range(n_col):
            X_transpose[j][i] = X[i][j]  # fill X_transpose elements

    return X_transpose


"""2) Matrix multiplication"""

"""Expected input X and Y: original matrices
Expected output X_Y_prod: multiplied matrix of X and Y"""


def my_mat_prod(X, Y):
    n_row_X = len(X)  # n_row of first matrix X
    n_col_X = len(X[0])  # n_col of first matrix X
    n_row_Y = len(Y)  # n_row of second matrix Y
    n_col_Y = len(Y[0])  # n_col of second matrix Y

    # Checking matrix compatible size
    if n_col_X != n_row_Y:
        raise ValueError("Dimensions are incompatible with multiplication")

    X_Y_prod = [[0] * n_col_Y for _ in range(n_row_X)]  # create and set dim

    for i in range(n_row_X):
        for j in range(n_col_X):
            for k in range(n_col_Y):
                X_Y_prod[i][k] += X[i][j] * Y[j][k]  # fill X_Y_prod elements

    return X_Y_prod
