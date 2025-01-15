from multiprocessing import cpu_count

logical_cores = cpu_count()

print(f"Number of logical cores available: {logical_cores}")
