import numpy as np
from pylab import plt


# 1. Define our system of equations
def system(t, Y, c):
    """
    Y[0] = position (x)
    Y[1] = velocity (v)
    """
    m = 20  # kg
    k = 20  # N/m

    dy1_dt = Y[1]  # velocity
    dy2_dt = -(k / m) * Y[0] - (c / m) * Y[1]  # acceleration

    return np.array([dy1_dt, dy2_dt])


# 2. RK4 stepper function - like a recipe for taking one step forward
def rk4_step(f, t, y, h, c):
    k1 = f(t, y, c)
    k2 = f(t + h / 2, y + h / 2 * k1, c)
    k3 = f(t + h / 2, y + h / 2 * k2, c)
    k4 = f(t + h, y + h * k3, c)

    return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


# 3. Set up our timeline and arrays
t_start = 0
t_end = 15
dt = 0.01
t = np.arange(t_start, t_end + dt, dt)
n_steps = len(t)

# Arrays for each damping case
x_underdamped = np.zeros(n_steps)
x_critical = np.zeros(n_steps)
x_overdamped = np.zeros(n_steps)

v_underdamped = np.zeros(n_steps)
v_critical = np.zeros(n_steps)
v_overdamped = np.zeros(n_steps)

# Initial conditions
x_underdamped[0] = 1
x_critical[0] = 1
x_overdamped[0] = 1

v_underdamped[0] = 0
v_critical[0] = 0
v_overdamped[0] = 0

# 4. Main solution loop
c_under = 5
c_crit = 40
c_over = 200

for i in range(1, n_steps):
    # Underdamped case
    current_state = np.array([x_underdamped[i - 1], v_underdamped[i - 1]])
    new_state = rk4_step(system, t[i - 1], current_state, dt, c_under)
    x_underdamped[i] = new_state[0]
    v_underdamped[i] = new_state[1]

    # Critically damped case
    current_state = np.array([x_critical[i - 1], v_critical[i - 1]])
    new_state = rk4_step(system, t[i - 1], current_state, dt, c_crit)
    x_critical[i] = new_state[0]
    v_critical[i] = new_state[1]

    # Overdamped case
    current_state = np.array([x_overdamped[i - 1], v_overdamped[i - 1]])
    new_state = rk4_step(system, t[i - 1], current_state, dt, c_over)
    x_overdamped[i] = new_state[0]
    v_overdamped[i] = new_state[1]

# 5. Create visualization
plt.figure(figsize=(12, 8))

# Position subplot
plt.subplot(2, 1, 1)
plt.plot(t, x_underdamped, label="Underdamped (c=5)", linewidth=2)
plt.plot(t, x_critical, label="Critically damped (c=40)", linewidth=2)
plt.plot(t, x_overdamped, label="Overdamped (c=200)", linewidth=2)
plt.title("Spring-Mass System: Position and Velocity vs Time")
plt.ylabel("Position (m)")
plt.xlim(t_start, t_end)
plt.grid(True)
plt.legend()

# Velocity subplot
plt.subplot(2, 1, 2)
plt.plot(t, v_underdamped, label="Underdamped (c=5)", linewidth=2)
plt.plot(t, v_critical, label="Critically damped (c=40)", linewidth=2)
plt.plot(t, v_overdamped, label="Overdamped (c=200)", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.xlim(t_start, t_end)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
