######################################################################
#
# A Python program to calculate the heat capacity of a solid with a
# temperature T, where:
# V - 		volume of the solid;
# rho - 	density of the solid;
# theta_d - Debye temperature;
# k - 		Boltzmann constant;
# N_A - 	Avogadro's number;
#
# The program uses Gaussian Quadrature to evaluate the integral.
#
# Author: 																#
# Rosen Ivanov															#
# 																		#
# 																		#
# References: 															#
# [1] Newman, M. (2013). Computational Physics. 						#
#
######################################################################

from numpy import exp, linspace, cumsum
from gaussxw import gaussxwab
from pylab import plt

# We will calculate the heat capacity of a 1000
# cubic centimeter solid aluminum sample:

# The heat capacity of a solid is given by:
# C_V = 9 * V * rho * k * (T/theta_d)^3 * int_0^(theta_d/T) x^4 / (exp(x) - 1)^2 dx

# Volume in cubic meters
V = 1e-3
# Density in m^-3
rho = 6.022e28
# Debye temperature in K
theta_d = 428
# Boltzmann constant in J/K
k = 1.38064852e-23

# Numerical Integration Parameters
# Sample points
N = 50
# Lower bound
a = 0.0

temps = linspace(5, 500, 500)


def gaussq(f, b):
    xp, wp = gaussxwab(N, a, b)
    # Integral value
    I_val = 0.0

    for k in range(N):
        I_val += wp[k] * f(xp[k])

    return I_val


def cv(x):
    return 9 * V * rho * k * (temp / theta_d) ** 3 * (x**4 * exp(x)) / (exp(x) - 1) ** 2


I = list()

for temp in temps:
    b = theta_d / temp
    I.append(gaussq(cv, b))


print(f"Value of Integral is: {I}")

plt.figure(figsize=(7, 4))
plt.plot(temps, I, color="purple")
plt.title("Heat capacity of solid aluminum")
plt.xlabel(r"Temperature ($K$)")
plt.ylabel(r"$C_V$ ( $J \cdot K^{-1}$)")
plt.xlim(temps[0], temps[-1])
plt.grid()
plt.show()
