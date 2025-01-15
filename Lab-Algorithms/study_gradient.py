import numpy as np
import time
from gradient import gradient_descent
from gradient import stochastic_gradient_descent
from gradient import plot

a = 4
b = 2
sigma = 0.05
n = 1000
np.random.seed(1)

x = np.linspace(-5, 5, n)
y = a * x + b + np.random.normal(0, sigma, n)

# Gradient Descent
start_time = time.time()
gd_a_s_gd, gd_b_s, gd_total_loss = gradient_descent(x, y, gamma=0.01, step=200)
gd_time = time.time() - start_time

# Stochastic Gradient Descent
start_time = time.time()
sgd_result = stochastic_gradient_descent(x, y, gamma=0.003, step=600)
sgd_a_s_gd, sgd_b_s, sgd_total_loss = sgd_result
sgd_time = time.time() - start_time

# Plot
plot(gd_a_s_gd, gd_b_s, gd_total_loss, 'Gradient Descent')
plot(sgd_a_s_gd, sgd_b_s, sgd_total_loss, 'Stochastic Gradient Descent')

# Analyze computing time
print(f"Gradient Descent: {gd_time}")
print(f"Stochastic Gradient Descent: {sgd_time}")
