import numpy as np


def gradient_descent(x, y, gamma, step):
    """
    Input: x(independent variable), y(depentdent variable),
    gamma(step size), step(number of steps)
    Output: a_s(history of a), b_s(history of b), loss(history of loss)
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("Inputs x and y must be NumPy arrays.")
    if not isinstance(step, int) or step <= 0:
        raise ValueError("Number of steps must be a positive integer.")
    n = len(x)
    a, b = 0, 0
    a_s = [a]
    b_s = [b]
    total_loss = []

    for _ in range(step):
        y_pred = a * x + b
        loss = np.sum((y - y_pred) ** 2) / n
        total_loss.append(loss)

        a_grad = -2 * np.sum((y - y_pred) * x) / n
        b_grad = -2 * np.sum(y - y_pred) / n

        a -= gamma * a_grad
        b -= gamma * b_grad

        a_s.append(a)
        b_s.append(b)

    return a_s, b_s, total_loss


def stochastic_gradient_descent(x, y, gamma, step):
    """
    Input: x(independent variable), y(depentdent variable),
    gamma(step size), step(number of steps)
    Output: a_s(history of a), b_s(history of b), loss(history of loss)
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("Inputs x and y must be NumPy arrays.")
    if not isinstance(step, int) or step <= 0:
        raise ValueError("Number of steps must be a positive integer.")
    n = len(x)
    a, b = 0, 0
    a_s = [a]
    b_s = [b]
    total_loss = []

    for _ in range(step):
        i = np.random.randint(0, n)
        y_pred = a * x[i] + b
        loss = np.sum((y - y_pred) ** 2) / n
        total_loss.append(loss)

        a_grad = -2 * x[i] * (y[i] - y_pred)
        b_grad = -2 * (y[i] - y_pred)

        a -= gamma * a_grad
        b -= gamma * b_grad

        a_s.append(a)
        b_s.append(b)

    return a_s, b_s, total_loss

