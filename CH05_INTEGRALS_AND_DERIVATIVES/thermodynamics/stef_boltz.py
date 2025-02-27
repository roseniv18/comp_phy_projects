from numpy import pi, exp
from gaussxw import gaussxwab

# Bolztmann Constant [J/K]
kb = 1.380649e-23

# Reduced Plank Constant [J.s]
h_ = 1.054571817e-34

# Speed of Light [m/s]
c = 299792458

# Lower bound of integration
a = 0

# Upper bound of integration (after change of variables)
b = 1

# Room Temperature
T = 293.15

# Number of points
N = 50


def W(z):
    non_int = (kb**4) * (T**4) / (4 * pi**2 * (c**2) * (h_**3))
    # Integral with change of variables
    return non_int * (z**3) / ((1 - z) ** 5 * (exp(z / (1 - z)) - 1))


def gaussq(f, b):
    # Calcualte points and weights
    xp, wp = gaussxwab(N, a, b)
    # Integral value
    I_val = 0.0

    for k in range(N):
        I_val += wp[k] * f(xp[k])

    return I_val


# Total energy given off by black body per unit area per second
W = gaussq(W, b)

# True Stefan-Boltzmann Constant [W/(m^2.K^4)]
sigma = 5.670374419e-8

# Calculated Stefan-Boltzmann Constant
sigma_calc = W / T**4

# Percentage Error
perc_err = abs(sigma - sigma_calc) / sigma * 100

print(f"Calculated Stefan-Boltzmann Constant: {sigma_calc:.18f} W/(m^2.K^4)")
print(f"Percentage Error: {perc_err:.10f}%")
