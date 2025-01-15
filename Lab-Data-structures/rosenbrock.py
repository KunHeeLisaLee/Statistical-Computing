import numpy as np
import matplotlib.pyplot as plt
from rosenbrock_module import measure_time_distance, plot_results, vec_eval
from rosenbrock_module import plot_results_2, plot_results_3, plot_results_4

# Store the values
n_values = range(100, 2001, 100)
vec_times = []
nonvec_times = []
distances = []
min_values = []


for i in n_values:
    vec_time, nonvec_time, min_value, distance = measure_time_distance(i)
    vec_times.append(vec_time)
    nonvec_times.append(nonvec_time)
    min_values.append(min_value)
    distances.append(distance)


plot_results(n_values, vec_times, nonvec_times)

plot_results_2(n_values, vec_times, nonvec_times)

plot_results_3(n_values, distances)

plot_results_4(n_values, min_values)

n = 2000
X, Y, Z = vec_eval(n)

# Plot 5
plt.figure(figsize=(12, 6))

contour = plt.contourf(X, Y, np.log(Z), levels=50, cmap='viridis')
plt.colorbar(contour, label='log(f)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithmic of Rosenbrock Function (n=2000)')
plt.show()
