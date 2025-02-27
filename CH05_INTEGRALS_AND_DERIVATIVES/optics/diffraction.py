# EXERCISE 5.11 page 174

from numpy import sqrt, sin, cos, pi, linspace
from gaussxw import gaussxwab
import matplotlib.pyplot as plt

# Wavelength [m]
lmb = 1.0

# Location past the edge [m]
z = 3

# Points
N = 50

# Lower bound of integrals
a = 0.0


# Upper bound of integrals
def u(x):
    return x * sqrt(2 / (lmb * z))


# X values from -5 m to +5 m
x_vals = linspace(-5, 5, N * 10)


# INTEGRALS


def C(t):
    return cos(0.5 * pi * t**2)


def S(t):
    return sin(0.5 * pi * t**2)


# I / I0
def ratio(x):
    u_val = u(x)
    # 't' is passed through the function reference f in gaussq
    # In reality, xp[k] corresponds to the 't' variable
    C_val = gaussq(C, u_val)
    S_val = gaussq(S, u_val)
    return 0.125 * ((2 * C_val + 1) ** 2 + (2 * S_val + 1) ** 2)


# GAUSSIAN QUADRATURE
def gaussq(f, b):
    # Calcualte points and weights
    xp, wp = gaussxwab(N, a, b)
    # Integral value
    I_val = 0.0

    for k in range(N):
        I_val += wp[k] * f(xp[k])

    return I_val


r_vals = list()

for x in x_vals:
    r_vals.append(ratio(x))

# Plotting

plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$\frac{I}{I_{0}}$")
plt.plot(x_vals, r_vals, "k--")
plt.title(r"$I \div I_{0}$ as a function of $x$")
plt.show()
