# Euler-Maclaurin Numerical Integration
from numpy import ones, linspace

# Integration bounds
a = 0
b = 2

# Central Difference Interval
h_cdm = 1e-5

# Integration Slices
N = 10
# Integration Intervals
h = (b - a) / N


def f(x):
    return (x**4) - (2 * x) + 1


def cent_difference(x, f):
    val_forw = f(x + h_cdm)
    val_back = f(x - h_cdm)
    return (val_forw - val_back) / (2 * h_cdm)


def trapez(f):
    x_vals = linspace(a, b, N + 1)
    weights = ones(N + 1)
    weights[0] = 0.5
    weights[-1] = 0.5
    return h * sum(weights * f(x_vals))


# Calculate derivatives at f'(a) and f'(b)
f_pa = cent_difference(a, f)
f_pb = cent_difference(b, f)

# Euler-Maclaurin Method
final_val = trapez(f) + (((1 / 12) * h * h) * (f_pa - f_pb))
print(final_val)


# Answer to b)
"""
This method is not used much in practice, because of the calculation
of the derivatives at f'(a) and f'(b). When the function is not known at all
points, but at specific points, then the calculation of the derivatives
is even more troublesome.
"""
