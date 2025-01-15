import numpy as np
import time

"""1. Defining Rosenbrock function"""


def rosenbrock_func(X, Y):
    """output: numpy array of rosenbrock function"""
    return (np.pi/2 - X)**2 + 100*(Y - X**2)**2


"""2. Creating grid"""


def create_grid(n):
    """input: number of subintervals
    output: grid points"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    x = np.linspace(-3, 3, n+1)
    y = np.linspace(-1, 5, n+1)

    return np.meshgrid(x, y)  # denote set of grid points


"""3. Evaluating f on G"""


# a) Vectorized manner


def vec_eval(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    X, Y = create_grid(n)
    Z = rosenbrock_func(X, Y)
    return X, Y, Z


# b) Non-vectorized manner


def nonvec_eval(n):  # defined a function that evaluates f on G
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    X = np.linspace(-3, 3, n+1)
    Y = np.linspace(-1, 5, n+1)
    Z = np.zeros((n+1, n+1))
    for i in range(n+1):
        for j in range(n+1):
            Z[i, j] = rosenbrock_func(X[i], Y[j])
    return X, Y, Z


"""4. Finding Minimizer/minimum value"""


def find_minimizer(Z):
    """min_index: indices of the minimum value
    Z[min_index]: minimum value """
    min_index = np.unravel_index(np.argmin(Z, axis=None), Z.shape)
    return min_index, Z[min_index]


"""5. Measuring computing time and distance"""


def measure_time_distance(n):
    """vec_time & nonvec_time: taken computing time,
    min_value_vec: minimum value,
    distance: Euclidean distance to the actual minimizer"""
    start = time.time()  # start time
    X_vec, Y_vec, Z_vec = vec_eval(n)
    vec_time = time.time() - start  # end time

    start = time.time()  # start time
    X_nonvec, Y_nonvec, Z_nonvec = nonvec_eval(n)
    nonvec_time = time.time() - start  # end time

    min_index_vec, min_value_vec = find_minimizer(Z_vec)
    min_index_nonvec, min_value_nonvec = find_minimizer(Z_nonvec)

    assert np.isclose(min_value_vec, min_value_nonvec), "Values do not match"

    x_min, y_min = X_vec[min_index_vec], Y_vec[min_index_vec]
    true_min = (np.pi/2, (np.pi/2)**2)
    distance = np.sqrt((x_min - true_min[0])**2 + (y_min - true_min[1])**2)

    return vec_time, nonvec_time, min_value_vec, distance


# Plot 1
def plot_results(n_values, vec_times, nonvec_times):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))

    plt.plot(n_values, vec_times, label='Vectorized')
    plt.plot(n_values, nonvec_times, label='Non-Vectorized')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.title('Computation Time')

    plt.show()


# Plot 2
def plot_results_2(n_values, vec_times, nonvec_times):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))

    ratio = np.array(nonvec_times) / np.array(vec_times)
    plt.plot(n_values, ratio, label='Non-vec / Vec')
    plt.xlabel('n')
    plt.ylabel('Time Ratio')
    plt.legend()
    plt.title('Time Ratio (Non-vec / Vec)')

    plt.show()


# Plot 3
def plot_results_3(n_values, distances):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))

    plt.plot(n_values, distances, label='Distance to Actual Minimizer')
    plt.xlabel('n')
    plt.ylabel('Distance')
    plt.legend()
    plt.title('Distance to Actual Minimizer')

    plt.show()


# Plot 4
def plot_results_4(n_values, min_values):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))

    plt.plot(n_values, min_values, label='Minimum Value')
    plt.xlabel('n')
    plt.ylabel('Minimum Value')
    plt.legend()
    plt.title('Minimum Value')

    plt.show()
