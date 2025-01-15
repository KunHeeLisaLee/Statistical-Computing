from trial_division import trial_division
import time
import multiprocessing as mp
import matplotlib.pyplot as plt


def factorize_number(n):
    """Factorize a number and return its factors."""
    if not isinstance(n, int) or n < 2:
        raise ValueError(f"Input must be an integer greater than 1. Got: {n}")
    try:
        return trial_division(n)
    except Exception as e:
        raise RuntimeError(f"Error during factorization of {n}: {e}")


def compute_time(integers, num_cores):
    """Measure time taken using a specified number of cores"""
    if num_cores < 1:
        raise ValueError("Number of cores must be at least 1.")
    if not isinstance(num_cores, int):
        raise TypeError("Number of cores must be an integer.")

    try:
        start_time = time.time()
        with mp.Pool(num_cores) as pool:
            pool.map(factorize_number, integers)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        raise RuntimeError(f"An error occurred during multiprocessing: {e}")


if __name__ == '__main__':
    integers = []
    with open("./integers.dat", "r") as f:
        for line in f:
            integers.append(int(line.rstrip("\n")))

    factors = []
    primes = []

    num_cores = mp.cpu_count()
    print(f"Using {num_cores} logical cores for parallel processing.")

    core_counts = list(range(1, num_cores + 1))
    times = []

    for cores in core_counts:
        print(f"Analyzing with {cores} core(s)...")
        elapsed_time = compute_time(integers, cores)
        times.append(elapsed_time)
        print(f"Time taken with {cores} core(s): {elapsed_time:.2f} seconds")

    # Calculate speedup
    single_core_time = times[0]
    speedups = [single_core_time / t for t in times]

    # Plot the results
    plt.plot(core_counts, speedups, marker='o')
    plt.xlabel('Number of Cores')
    plt.ylabel('Speedup')
    plt.title('Speedup vs. Number of Cores')
    plt.grid()
    plt.show()

    # Output results
    print("Core Count | Time (s) | Speedup")
    for cores, time_taken, speedup in zip(core_counts, times, speedups):
        print(f"{cores:10} | {time_taken:.2f}  | {speedup:.2f}")
