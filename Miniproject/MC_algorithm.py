import numpy as np
import matplotlib.pyplot as plt

"""Codes for implementing MC_algorithm for computing pi"""

"""Expected input n: positive integer
Expected output pi_hat: estimated pi value"""


def mc_algo(n):
    # 1) generate n x 2 random variables that follow Unif(-1,1)
    # First, generate from Unif(0,1)
    # Then, multiply and subtract to scale to (-1,1)
    var = np.random.rand(n, 2) * 2 - 1

    # 2) compute indicator function
    # First, extract every X(i) and Y(i)
    # Then, square each and sum
    # Compare the result (distance from (0,0)) with 1
    sum_indi = np.sum(var[:, 0]**2 + var[:, 1]**2 <= 1)

    # 3) calculate pi_hat
    # based on the given formula
    pi_hat = (4 * sum_indi) / n
    return pi_hat


"""Codes for actual steps"""

# b) Testing the above function
n_test = [50, 500, 5000, 50000]
pi_est_test = [mc_algo(n) for n in n_test]
print(pi_est_test)  # verified it works as desired

# c-1) Running algorithm with the given numbers
n_given = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
pi_est = [mc_algo(n) for n in n_given]
print(pi_est)

# c-2) Creating plot
plt.semilogx(n_given, pi_est, marker='o')  # used log scale
plt.axhline(y=np.pi, linestyle='--', color='tab:pink')  # added hline
plt.title('Estimated pi using MC algorithm')
plt.xlabel('Number of points')
plt.ylabel('Estimated pi value')
plt.savefig('MC_algorithm_pi_plot.pdf')  # saved as a pdf
plt.show()
