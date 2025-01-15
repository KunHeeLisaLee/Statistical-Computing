import platform
import statsmodels.api as sm
import numpy as np

print("This program is running on " + platform.node())

print("Python version: " + platform.python_version())
print("statsmodels version: " + sm.__version__ + "\n")

np.random.seed(9876789)

x = np.linspace(0, 10, 100)
X = np.column_stack((x, x ** 2))
beta = np.array([1, 0.1, 10])
e = np.random.normal(size=100)

X = sm.add_constant(X)
y = np.dot(X, beta) + e

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
