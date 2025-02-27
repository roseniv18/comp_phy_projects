# Exercise 5.13

from numpy import sqrt, pi, exp, linspace, zeros, array, float64, int64
from math import factorial
import matplotlib.pyplot as plt
import sys

sys.path.insert(1, "../numerical_methods/integrals")
from gaussxw import gaussxwab

# STEPS
steps = 500
# N energy levels
n = 4
# X values
x_vals = linspace(-4, 4, steps)


def hermite_polynomials(n, x):
    # First check if x is a single number or an array
    if isinstance(x, (float, int, float64, int64)):
        x = array([x])  # Convert single number to array

    H_vals = zeros((n + 1, len(x)))
    H_vals[0] = 1
    H_vals[1] = 2 * x
    for i in range(2, n + 1):
        H_vals[i] = 2 * x * H_vals[i - 1] - 2 * (i - 1) * H_vals[i - 2]

    # If input was single number, return single number
    if len(x) == 1:
        return H_vals[:, 0]
    return H_vals


def wavefunction(n, x):
    if isinstance(x, (float, int, float64, int64)):
        x = array([x])  # Convert single number to array

    H = hermite_polynomials(n, x)
    w_vals = zeros((n + 1, len(x)))

    for i in range(n + 1):
        norm = 1 / sqrt(2**i * factorial(i) * sqrt(pi))
        w_vals[i] = norm * exp(-(x**2) / 2) * H[i]

    if len(x) == 1:
        return w_vals[:, 0]
    return w_vals


w_vals = wavefunction(n, x_vals)

# Plotting

fig = plt.figure(figsize=(10, 6))
ax = plt.axes()

for i in range(n):
    ax.plot(x_vals, w_vals[i], label=f"n = {i}")

ax.set_xlabel("x")
ax.set_ylabel("$\psi_n(x)$")
ax.set_title("Harmonic Oscillator Wavefunctions")
ax.legend()

# Separate plot of the wavefunction for n = 30 from x = -10 to x = 10
ax2 = plt.figure(figsize=(10, 6))
ax2 = plt.axes()
ax2.set_xlabel("x")
ax2.set_ylabel("$\psi_n(x)$")
ax2.set_title("Harmonic Oscillator Wavefunction for n = 30")

n = 30
x_vals = linspace(-10, 10, steps)

w_vals = wavefunction(n, x_vals)

ax2.plot(x_vals, w_vals[-1])
plt.show()


# C) Calculate quantum uncertainty in the position of a particle in the n-th
# energy level of a harmonic oscillator. This is quantified by its root-mean-square
# position sqrt(<x^2>)

# Points of integration
points = 100
# Chosen energy level
n = 5

# We can't numerically integrate from -inf to +inf,
# so we make a change of variables.
# The new bounds are -1 to 1.
a = -1
b = 1
# The resulting integrand is:


def pos_square(n, z):
    z_term = 1 - z**2
    z_term_sq = z_term**2
    x = z / (z_term)  # Change of variables
    return (x**2) * (wavefunction(n, x)[n] ** 2) * ((1 + z**2) / (z_term_sq))


def gaussq(f, b):
    xp, wp = gaussxwab(points, a, b)
    # Integral value
    I_val = 0.0

    for i in range(points):
        I_val += wp[i] * f(n, xp[i])

    return I_val


# Root-mean-square position with given n amount of energy levels
rms_pos = sqrt(gaussq(pos_square, b))

print(rms_pos)
