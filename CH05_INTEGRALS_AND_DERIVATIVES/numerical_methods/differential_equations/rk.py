import numpy as np
from scipy.integrate import solve_ivp
from pylab import plt

n = 20  # Number of points
x = np.linspace(0, 10, n)  # Spatial grid
f = 10  # Heat source term
ta = 30  # Left boundary T(0)
tb = 150  # Right boundary T(10)
dt = (tb - ta) / 10  # Initial guess for temperature gradient


# Define our system of ODEs
def heat_equations(x, t):
    """
    t[0] is temperature T
    t[1] is temperature gradient dT/dx
    Returns [dT/dx, d²T/dx²]
    """
    return [
        t[1],  # dT/dx = t[1]
        -f,
    ]  # d²T/dx² = -f


# Initial solution attempt
solution = solve_ivp(
    heat_equations,
    [0, 10],  # Time span [start, end]
    [ta, dt],  # Initial conditions [T(0), T'(0)]
    t_eval=x,  # Points where we want the solution
)

# Shooting method iteration
while abs(solution.y[0, -1] - tb) > 0.1:
    dt = dt + (tb - solution.y[0, -1]) / 10  # Adjust step size based on error
    solution = solve_ivp(heat_equations, [0, 10], [ta, dt], t_eval=x)

# Plot result
plt.figure(figsize=(10, 6))
plt.plot(x, solution.y[0], "b-o", linewidth=1.5)
plt.xlabel("Position (x)")
plt.ylabel("Temperature (T)")
plt.title("Temperature Distribution in Heated Rod")
plt.grid(True)
plt.show()


# Time arrays
t_start = 0
t_end = 15
dt = 0.01
t = np.arange(t_start, t_end + dt, dt)
n_steps = len(t)

# Solution arrays for positions
x_underdamped = np.zeros(n_steps)  # c = 5
x_critical = np.zeros(n_steps)  # c = 40
x_overdamped = np.zeros(n_steps)  # c = 200

# Solution arrays for velocities
v_underdamped = np.zeros(n_steps)
v_critical = np.zeros(n_steps)
v_overdamped = np.zeros(n_steps)

# Initial conditions (like filling in the first page of each notebook)
x_underdamped[0] = 1  # Initial displacement = 1m
x_critical[0] = 1
x_overdamped[0] = 1

v_underdamped[0] = 0  # Initial velocity = 0 m/s
v_critical[0] = 0
v_overdamped[0] = 0


def rk4_step(f, t, y, h, c):
    k1 = f(t, y, c)
    k2 = f(t + h / 2, y + h / 2 * k1, c)
    k3 = f(t + h / 2, y + h / 2 * k2, c)
    k4 = f(t + h, y + h * k3, c)

    return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def system(t, Y, c):
    """
    Define our system of ODEs
    Y[0] = y₁ = position
    Y[1] = y₂ = velocity
    """
    m = 20  # kg
    k = 20  # N/m

    dy1_dt = Y[1]  # velocity
    dy2_dt = -(k / m) * Y[0] - (c / m) * Y[1]  # acceleration

    return np.array([dy1_dt, dy2_dt])


for i in range(n_steps - 1):
    k1_underdamped = dt * v_underdamped[i]
    k1_critical = dt * v_critical[i]
    k1_overdamped = dt * v_overdamped[i]
