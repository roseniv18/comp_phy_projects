import numpy as np


def f(x):
    return (x**4) - (2 * x) + 1


# Integration bounds
a = 0
b = 2


def trapz(n):
    # Trapezoid width
    h = (b - a) / n
    # Trapezoidal rule
    tr = (0.5 * f(a)) + (0.5 * f(b))
    for i in range(1, n):
        tr += f(a + i * h)
    return tr * h


# Compute the integrals
integral_1 = trapz(10)
integral_2 = trapz(20)

# Actual value of integral
integral = 4.4

# Calculate the error
eps = abs((integral_2 - integral_1) / 3)
# Error between actual value and integral_2
eps_actual = abs(integral_2 - integral)

print("Integral with 10 trapezoids: ", integral_1)
print("Integral with 20 trapezoids: ", integral_2)
print("Error estimate: ", eps)
print("Error with actual value: ", eps_actual)
