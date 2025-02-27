import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from scipy import integrate

# Constants
L = 0.10  # 10 cm in meters
q0 = 100  # C/m^2
epsilon0 = 8.854e-12  # F/m
points = 21  # reduced for computation speed

# Create grid
x = np.linspace(0, L, points)
y = np.linspace(0, L, points)
X, Y = np.meshgrid(x, y)

def integrand(x_prime, y_prime, x, y, z=0.001):
    """Integrand for potential calculation"""
    sigma = q0 * sin(2*pi*x_prime/L) * sin(2*pi*y_prime/L)
    r = np.sqrt((x-x_prime)**2 + (y-y_prime)**2 + z**2)
    return sigma/r

# Calculate potential
V = np.zeros((points, points))
for i in range(points):
    for j in range(points):
        V[i,j] = integrate.dblquad(integrand, 0, L, 0, L, 
                                 args=(X[i,j], Y[i,j]))[0]
V *= 1/(4*pi*epsilon0)

# Calculate E-field by numerical differentiation
dx = L/(points-1)
Ex = np.zeros((points, points))
Ey = np.zeros((points, points))

# Central difference for interior points
for i in range(1, points-1):
    for j in range(points):
        Ex[i,j] = -(V[i+1,j] - V[i-1,j])/(2*dx)
for i in range(points):
    for j in range(1, points-1):
        Ey[i,j] = -(V[i,j+1] - V[i,j-1])/(2*dx)

# Forward/backward difference for edges
Ex[0,:] = -(V[1,:] - V[0,:])/dx
Ex[-1,:] = -(V[-1,:] - V[-2,:])/dx
Ey[:,0] = -(V[:,1] - V[:,0])/dx
Ey[:,-1] = -(V[:,-1] - V[:,-2])/dx

# Calculate field magnitude
E_magnitude = np.sqrt(Ex**2 + Ey**2)

# Create the plot
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, Ex, Ey, E_magnitude, cmap='viridis')
plt.colorbar(label='Electric field magnitude (V/m)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Electric Field from Continuous Charge Distribution')
plt.axis('equal')
plt.grid(True)
plt.show()