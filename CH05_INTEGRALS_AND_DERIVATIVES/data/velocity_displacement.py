import numpy as np
from pylab import plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("../resources/velocities_2.txt", float)

# Time [s]
t = data[:, 0]
# Velocity [m/s]
v = data[:, 1]

displacement = cumulative_trapezoid(v, initial=0)


def trapezoid_exp(x, y, n):
    a = x[0]
    b = x[-1]
    # Width of trapezoid
    h = (b - a) / (n - 1)

    # Trapezoidal rule
    s = np.zeros(n)
    s[0] = 0.5 * v[0]
    s[-1] = 0.5 * v[-1]

    for k in range(1, n):
        s[k] = y[k]

    return np.array(h * np.cumsum(s))


displacement_exp = trapezoid_exp(t, v, len(t))

print(displacement)
print(displacement_exp)

# PLOTS
fig, ax1 = plt.subplots()

# Velocity plot
ax1_color = "blue"
ax1.set_xlabel("t [s]")
ax1.set_ylabel("v [m/s]")
ax1.plot(t, v, color=ax1_color, label="Velocity graph")

# Displacement plot using cumulative trapezoid from scipy
ax2_color = "red"
ax2 = ax1.twinx()
# ax2.set_xlabel("t [s]")
ax2.set_ylabel("s [m]")
ax2.plot(t, displacement, color=ax2_color, label="Displacement graph")

# Displacement plot using own trapezoid_exp
# ax3.set_xlabel("t [s]")
ax2.plot(t, displacement_exp, color="purple", label="Displacement graph exp")

fig.tight_layout()
fig.legend(loc="upper center")

plt.show()
