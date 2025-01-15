import numpy as np
import time
import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import apply_quick_sort

# 1-2. Analyzing running times  & plotting


def measure_runtime(sort_function, list, iteration=10):
    """
    Input:
    sort_function(sorting algorithm),
    list(testing list),
    iteration(given as 10 by default)
    Output:
    median runtime
    """
    runtime = []
    for _ in range(iteration):
        list_copy = list.copy()
        start_time = time.time()
        sort_function(list_copy)
        runtime.append(time.time() - start_time)
    return np.median(runtime)


def measure_runtime_small_n():
    """
    Output: Plots runtime of sorting algorithms
    """
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": apply_quick_sort
    }

    small_n = [40, 70, 100, 130, 160, 190]
    results = {name: [] for name in algorithms.keys()}

    for n in small_n:
        list = np.random.normal(size=n).tolist()
        for name, sort_function in algorithms.items():
            runtime = measure_runtime(sort_function, list)
            results[name].append(runtime)

    # Plotting
    for name, runtimes in results.items():
        plt.plot(small_n, runtimes, label=name)

    plt.xlabel("Input size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()


# 2. Analyzing running time for large n


def measure_runtime_large_n():
    """
    Output: Plots runtime of sorting algorithms
    """
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Numpy Sort": lambda test_list: np.sort(test_list).tolist(),
        "Quick Sort": apply_quick_sort
    }

    large_n = range(40, 2000, 200)
    results = {name: [] for name in algorithms.keys()}

    for n in large_n:
        list = np.random.normal(size=n).tolist()
        for name, sort_function in algorithms.items():
            runtime = measure_runtime(sort_function, list)
            results[name].append(runtime)

    # Plotting
    for name, runtimes in results.items():
        plt.plot(large_n, runtimes, label=name)

    plt.xlabel("Input size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()


# 3. Asymptotic analysis


def asymptotic_analysis():
    """
    Output: Plots f(n)/g(n) to check asymptotic scaling
    """
    algorithms = {
        "Bubble Sort (O(n^2))": (bubble_sort, lambda n: n**2),
        "Merge Sort (O(nlog(n)))": (merge_sort, lambda n: n * np.log(n)),
        "Selection Sort (O(n^2))": (selection_sort, lambda n: n**2),
        "Numpy Sort (O(nlog(n)))": (
            lambda test_list: np.sort(test_list).tolist(),
            lambda n: n * np.log(n)),
        "Quick Sort (O(nlog(n)))": (apply_quick_sort, lambda n: n * np.log(n))
    }

    large_n = range(40, 2000, 200)  # same as large_n
    results = {name: [] for name in algorithms.keys()}

    for n in large_n:
        list = np.random.normal(size=n).tolist()
        for name, (sort_function, o_scale_function) in algorithms.items():
            runtime = measure_runtime(sort_function, list)
            scaling = runtime / o_scale_function(n)
            results[name].append(scaling)

    # Plotting
    for name, scaling_values in results.items():
        plt.plot(large_n, scaling_values, label=name)

    plt.xlabel("Input size (n)")
    plt.ylabel("Runtime / Scale of O(n)")
    plt.title("Asymptotic Analysis of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

    for name, scaling_values in results.items():
        print(f"{name}: {scaling_values}")


if __name__ == "__main__":
    asymptotic_analysis()
    # measure_runtime_small_n(), measure_runtime_large_n()
    # asymptotic_analysis()
