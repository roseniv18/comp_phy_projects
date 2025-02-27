# Exercise 5.14

from numpy import linspace
from gaussxw import gaussxwab
from pylab import plt

# Gravitational Constant [m^3.kg^-1.s^-2]
G = 6.674e-11

# Point mass [kg]
m = 1

# Mass of the metal sheet [kg]
M = 1000

# Length of the metal sheet [m]
L = 10

# Surface area of the metal sheet [m^2]
s = L * L

# Mass per unit area of the sheet [kg/m^2]
sigma = m / s

# Integration points (along each axis)
N = 100

# Bounds of integration
a = -L / 2
b = L / 2

# Z values
z_vals = linspace(0, 10, N)


# Component of the gravitational force along the z-axis
def F_z(x, y, z):
    gsz = G * sigma * z
    return gsz * (1 / (x * x + y * y + z * z) ** 1.5)


def d_gaussq(f):
    """Perform double Gaussian quadrature"""
    xp, wp = gaussxwab(N, a, b)
    # Integral value
    I_val = 0.0

    for i in range(N):
        for j in range(N):
            I_val += wp[i] * wp[j] * f(xp[i], xp[j], z)

    return I_val


# Integral values
I_vals = list()

for z in z_vals:
    I_vals.append(d_gaussq(F_z))

# Plot
plt.figure()
plt.title(r"$F_{z}$ due to plate (N) vs. z (m)")
plt.plot(z_vals, I_vals, "b--")
plt.show()
