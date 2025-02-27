# Exercise 5.23 C)

from numpy import zeros, sin, cos, pi, sqrt, loadtxt
from pylab import plt

# Grid spacing [arbitrary units]
h = 2.5

stm_values = loadtxt("../resources/stm.txt")

rows = len(stm_values)
cols = len(stm_values[0])

dx_heights = zeros((rows, cols))
dy_heights = zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        # Forward method
        if j == 0:
            dx_heights[i, j] = (stm_values[i, j + 1] - stm_values[i, j]) / h
        elif i == 0:
            dy_heights[i, j] = (stm_values[i + 1, j] - stm_values[i, j]) / h
        # Backward method
        elif j == cols - 1:
            dx_heights[i, j] = (stm_values[i, j] - stm_values[i, j - 1]) / h
        elif i == rows - 1:
            dy_heights[i, j] = (stm_values[i, j] - stm_values[i - 1, j]) / h
        # Central difference method
        else:
            dx_heights[i, j] = (stm_values[i, j + 1] - stm_values[i, j - 1]) / (2 * h)
            dy_heights[i, j] = (stm_values[i + 1, j] - stm_values[i - 1, j]) / (2 * h)

Intensity = zeros((rows, cols))

# Angle for the incident light (45 deg)
phi = pi / 4

for i in range(rows):
    for j in range(cols):
        normal_magnitude = sqrt((dx_heights[i, j] ** 2) + (dy_heights[i, j] ** 2) + 1)
        val = (
            -(cos(phi) * dx_heights[i, j])
            + (sin(phi) * dy_heights[i, j]) / normal_magnitude
        )
        Intensity[i][j] = val

plt.figure(figsize=(12, 6))
plt.imshow(Intensity, cmap="gray", aspect="auto", interpolation="nearest")
plt.colorbar(label="Elevation Change")
plt.xticks([])
plt.yticks([])
plt.title("Surface of Silicon (φ = 45°)", pad=20)
plt.tight_layout()
plt.show()
