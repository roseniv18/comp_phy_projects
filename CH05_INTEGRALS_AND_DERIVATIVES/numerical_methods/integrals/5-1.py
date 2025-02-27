import numpy as np
from pylab import plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("../../resources/velocities.txt", float)
# Time values
t = np.array(data[:, 0])
# Velocity values for particle at time t
v = np.array(data[:, 1])

# Integration bounds
a = t[0]
b = t[-1]

# Steps
n = len(data)

# Width
h = (b - a) / (n - 1)

# Trapezoidal rule
s = np.zeros(n)
s[0] = 0.5 * v[0]
s[-1] = 0.5 * v[-1]
# Store absolute values for distance (not displacement)
s_abs = abs(0.5 * (v[0] + v[-1]))

for k in range(1, n):
    s[k] = v[k]
    s_abs += abs(v[k])

# Total distance traveled
distance_traveled = h * s_abs
# Distance traveled per unit time
distance_traveled_per_unit_time = np.linspace(0, distance_traveled, n)
# Displacement
displacement = h * sum(s)
# Displacement as a function of time
displacement_per_unit_time = np.array(h * np.cumsum(s))

# print(f"Displacement: {displacement} m", )
# print(f"Total distance traveled: {distance_traveled} m", )
# print(distance_traveled_per_unit_time)


# PLOTS #
fig, ax1 = plt.subplots()

# Plots for velocity and trapezoidal approximation
ax1_color = "red"
ax1.set_xlabel("t (s)")
ax1.set_ylabel("v (m/s)", color=ax1_color)
ax1.plot(t, v, color=ax1_color, label="Data values for velocities")
ax1.plot(t, s, ".k", label="Trapezoidal approximation")

plt.grid()

# Plot for distance traveled per unit time
ax2_color = "blue"
ax2 = ax1.twinx()
ax2.set_yticks(
    np.arange(
        distance_traveled_per_unit_time[0], distance_traveled_per_unit_time[-1], 3.0
    )
)
ax2.set_ylabel("Distance traveled [m]", color=ax2_color)
ax2.plot(t, distance_traveled_per_unit_time, color=ax2_color, label="Distance traveled")
ax2.plot(
    t, displacement_per_unit_time, color="purple", label="Displacement own trapezoid"
)
ax2.plot(t, cumulative_trapezoid(v, t, initial=0), "--y", label="Displacement cumtrapz")

fig.tight_layout()
fig.legend(loc="upper center")

plt.xlim(t[0], t[-1])
print(t[-1])
plt.xticks(np.arange(t[0], t[-1] + 1, 10.0))
plt.show()
