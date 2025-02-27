from math import tanh
from numpy import linspace
from sympy import cosh
from pylab import plt


def sech(x):
    return cosh(x) ** -1


def f(x):
    return 1 + 0.5 * tanh(2 * x)


# First derivative (analytically calculated)
def dfdx(x):
    return sech(2 * x) * sech(2 * x)


# STEP SIZE
h = 0.000026777


x_vals = linspace(-2, 2, 100)


# Central Difference Approximation
def cdf(x):
    difference = f(x + h / 2) - f(x - h / 2)
    return difference / h


cdf_vals = list()
dfdx_vals = list()
err_vals = list()

for i in range(len(x_vals)):
    cdf_val = cdf(x_vals[i])
    dfdx_val = dfdx(x_vals[i])
    cdf_vals.append(cdf_val)
    dfdx_vals.append(dfdx_val)
    err_vals.append(abs(dfdx_val - cdf_val))


print("Maximum Error: ", max(err_vals))
print("Sum of absolute errors", sum(err_vals))

# PLOT

plt.plot(x_vals, cdf_vals, ".")
plt.plot(x_vals, dfdx_vals)
plt.legend(["Central Difference Approximation", "Calculated Derivative"])
plt.xlabel("x")
plt.ylabel("derivative")
plt.grid(True)
plt.show()
