# Exercise 5.21

from numpy import linspace, pi, sqrt, meshgrid, zeros, sign, log10, abs, max
from math import floor
from pylab import plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

q1 = 1
q2 = -1
# Permittivity in vacuum [F/m]
e0 = 8.8542e-12
# Length of square plane [m]
a = 1
# Distance between grid points [m]
l = 0.01
# Grid points
n = floor(a / l)
# Coordinates of charged particles
q1_point = Point(0.45, 0.5)
q2_point = Point(0.55, 0.5)

x_points = linspace(0, a, n)
y_points = linspace(0, a, n)
X, Y = meshgrid(x_points, y_points)

def el_pot(q, r):
    return (q / (4 * pi  * e0 * r))

# Calculated as minus the gradient of the electric potential
def el_field(q, x, y):
    constant_term = q / (4 * pi * e0)
    x_term = constant_term * (x / ((x**2 + y**2)**(3/2)))
    y_term = constant_term * (y / ((x**2 + y**2)**(3/2)))
    return x_term, y_term

# Electric field values (with magnitude and direction)
arrow_density = 20
x_arrows = linspace(0, a, arrow_density)
y_arrows = linspace(0, a, arrow_density)
X_arrows, Y_arrows = meshgrid(x_arrows, y_arrows)

# Electric field components
Ex = zeros((arrow_density, arrow_density))
Ey = zeros((arrow_density, arrow_density))

for i in range(arrow_density):
    for j in range(arrow_density):
        x1, y1 = X_arrows[i, j] - q1_point.x, Y_arrows[i, j] - q1_point.y
        x2, y2 = X_arrows[i, j] - q2_point.x, Y_arrows[i, j] - q2_point.y
        
        # Sum the contributions from both charges
        Ex1, Ey1 = el_field(q1, x1, y1)
        Ex2, Ey2 = el_field(q2, x2, y2)
        Ex[i, j] = Ex1 + Ex2
        Ey[i, j] = Ey1 + Ey2

def r_mag(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    eps = 1e-6
    return sqrt((dx ** 2) + (dy ** 2) + eps)


E_mag = sqrt(Ex**2 + Ey**2)

Ex_norm = Ex / E_mag
Ey_norm = Ey / E_mag


el_pot_vals = zeros((n, n))

for i in range(n):
    for j in range(n):
        grid_point = Point(X[i][j], Y[i][j])
        r1 = r_mag(q1_point, grid_point)
        r2 = r_mag(q2_point, grid_point)
        el_pot_val = el_pot(q1, r1) + el_pot(q2, r2)
        el_pot_vals[i][j] = el_pot_val
        

def transform_potential(el_pot_vals):
    # Find the maximum absolute value for normalization
    max_abs_val = max(abs(el_pot_vals))
    
    # Normalize the values while preserving signs
    normalized = el_pot_vals / max_abs_val
    
    # Apply a symmetric logarithmic scaling
    # This handles both positive and negative values smoothly
    return sign(normalized) * log10(1 + 10000*abs(normalized))

log_vals = transform_potential(el_pot_vals)
  
# Plot for electric potential   
# plt.figure(figsize=(10, 10))
# plt.imshow(log_vals, extent=[0, a, 0, a], cmap="RdBu_r")
# plt.colorbar(label="Electric Potential [V]")
# plt.xlabel("x [m]")
# plt.ylabel("y [m]")
# plt.title("Electric Potential on a 1x1 plane (Log Scale)")

# plt.plot(q1_point.x, q1_point.y, "k+", markersize=10, label="Positive Charge")
# plt.plot(q2_point.x, q2_point.y, "k_", markersize=10, label="Negative Charge")
# plt.legend()

# Plot for electric field with magnitude and arrows indicating direction
plt.figure(figsize=(10,10))
plt.quiver(X_arrows, Y_arrows, Ex_norm, Ey_norm, E_mag, cmap="viridis", pivot="middle", scale=30)
plt.colorbar(label="Electric Field Magnitude [C/N]")

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Electric Field")

# Add charges for reference
plt.plot(q1_point.x, q1_point.y, 'k+', markersize=10, label='Positive Charge')
plt.plot(q2_point.x, q2_point.y, 'k_', markersize=10, label='Negative Charge')
plt.legend()

plt.show()
