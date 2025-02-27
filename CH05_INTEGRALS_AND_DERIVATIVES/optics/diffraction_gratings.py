# Exercise 5.19

from numpy import sin, sqrt, pi, linspace, log10
from cmath import exp
from pylab import plt
import sys

sys.path.insert(1, "../numerical_methods/integrals")
from gaussxw import gaussxwab

# a) Since the maximum transmission occurs for alpha*u = pi/2, 3pi/2, ...
# Then the slit separation is alpha*u2 - alpha*u1 = 3pi/2 - pi/2 = pi
# And the separation is thus pi/alpha

# b) We are asked to write the transmission function for a
# slit separation of 20 um.
# Using above formula: 20 um = pi / alpha => alpha = pi/20 um

slit_sep = 20e-6
alpha = pi / slit_sep

# c) Calculate and graph intensity of the diffraction pattern.
# The grating has 10 slits in total. Other parameters are given below:

# Wavelength [m]
lmb = 500e-9

# Focal Length of Lens [m]
f = 1

# Width of screen [m]
u = 0.1

# Number of slits
slits = 10

# Width of grating [m]
w = slits * slit_sep

# RGB Wavelengths
wavelengths = {"red": 700e-9, "green": 550e-9, "blue": 450e-9}

# Actual wavelength for the exercise
wavelength = 500e-9


# Intensity Transmission Function
def q(u):
    return sin(u) ** 2


# Intensity of the Diffraction Pattern on the screen
# With Change of Variables
def I(x, u, lmb):
    return sqrt(q(u)) * exp((1j * 2 * pi * x * u) / (lmb * f))


# Numerical Integration using Gaussian Quadrature

# Sample points
N = 500

# Integration bounds (accounting change of variables)
a = -w / 2
b = w / 2


def gaussq(f):
    xp, wp = gaussxwab(N, a, b)
    val = 0.0

    for i in range(N):
        val += wp[i] * (f(xp[i]))

    return val


# I_vals = list()
# x_vals = linspace(-u, u, N)
# plt.figure(figsize=(12, 6))

# for color, lmb in wavelengths.items():
#     I_vals = []
#     for x in x_vals:
#         val = abs(gaussq(lambda u: I(x, u, lmb))) ** 2
#         I_vals.append(val)

#     # Normalize intensities for better visualization
#     I_vals = [i / max(I_vals) for i in I_vals]
#     plt.plot(
#         x_vals * 100,
#         I_vals,
#         label=f"{color} ({int(lmb*1e9)} nm)",
#         color=color,
#         alpha=0.7,
#     )
#     plt.imshow([I_vals, I_vals])


# plt.xlabel("Position on Screen (cm)")
# plt.ylabel("Normalized Intensity")
# plt.title("Diffraction Pattern for Different Wavelengths")
# plt.legend()
# plt.grid(True, alpha=0.3)

# d) Visualization of diffraction pattern using density plot
# Calculate for single strip of x_vals
# x_vals = linspace(-0.05, 0.05, N)  # +- 5 cm on screen
# I_vals = []

# for x in x_vals:
#     val = abs(gaussq(lambda u: I(x, u, lmb))) ** 2

#     I_vals.append(val)

# # Apply logarithmic scaling to enhance fainter stripes
# # Add small number to avoid log(0)
# I_vals = log10([i + 1e-10 for i in I_vals])

# # Create 2D array for density plot
# y_vals = linspace(-0.01, 0.01, 50)
# I_vals_2d = []
# for _ in y_vals:
#     I_vals_2d.append(I_vals)

# plt.figure(figsize=(12, 2))
# plt.imshow(
#     I_vals_2d,
#     extent=[x_vals[0] * 100, x_vals[-1] * 100, y_vals[0] * 100, y_vals[-1] * 100],
#     vmax=max(I_vals),  # Set maximum value for better contrast
#     vmin=max(I_vals - 3),  # Show 3 orders of magnitude
#     cmap="gray",
#     aspect="auto",
# )

# e) we must redefine some of the functions for this part
# i)
# beta = alpha / 2


# def q_e(u):
#     return ((sin(alpha * u)) ** 2) * ((sin(beta * u)) ** 2)


# def I_e(x, u, lmb):
#     return sqrt(q_e(u)) * exp((1j * 2 * pi * x * u) / (lmb * f))


# x_vals = linspace(-0.05, 0.05, N)  # +- 5 cm on screen
# I_vals = []

# for x in x_vals:
#     val = abs(gaussq(lambda u: I_e(x, u, lmb))) ** 2

#     I_vals.append(val)

# # Apply logarithmic scaling to enhance fainter stripes
# # Add small number to avoid log(0)
# I_vals = log10([i + 1e-10 for i in I_vals])

# # Create 2D array for density plot
# y_vals = linspace(-0.01, 0.01, 50)
# I_vals_2d = []
# for _ in y_vals:
#     I_vals_2d.append(I_vals)

# plt.figure(figsize=(12, 2))
# plt.imshow(
#     I_vals_2d,
#     extent=[x_vals[0] * 100, x_vals[-1] * 100, y_vals[0] * 100, y_vals[-1] * 100],
#     vmax=max(I_vals),  # Set maximum value for better contrast
#     vmin=max(I_vals - 3),  # Show 3 orders of magnitude
#     cmap="gray",
#     aspect="auto",
# )

# plt.show()


# ii) For square slits, we need to modify the transmission function to be a piecewise function
# and check if u is in the range of the slit interval
def q_d(u):
    if -45e-6 <= u <= -35e-6:
        return 1.0
    elif 25e-6 <= u <= 45e-6:
        return 1.0
    else:
        return 0.0


def I_d(x, u, lmb):
    return sqrt(q_d(u)) * exp((1j * 2 * pi * x * u) / (lmb * f))


x_vals = linspace(-0.05, 0.05, N)  # +- 5 cm on screen
I_vals = []

for x in x_vals:
    val = abs(gaussq(lambda u: I_d(x, u, lmb))) ** 2

    I_vals.append(val)

# Apply logarithmic scaling to enhance fainter stripes
# Add small number to avoid log(0)
I_vals = log10([i + 1e-10 for i in I_vals])

# Create 2D array for density plot
y_vals = linspace(-0.01, 0.01, 50)
I_vals_2d = []
for _ in y_vals:
    I_vals_2d.append(I_vals)

plt.figure(figsize=(12, 2))
plt.imshow(
    I_vals_2d,
    extent=[x_vals[0] * 100, x_vals[-1] * 100, y_vals[0] * 100, y_vals[-1] * 100],
    vmax=max(I_vals),  # Set maximum value for better contrast
    vmin=max(I_vals - 1),  # Show 1 orders of magnitude
    cmap="gray",
    aspect="auto",
)

plt.show()
