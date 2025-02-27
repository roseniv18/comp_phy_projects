# Numerical integration using Simpson's Rule. Exercise 5.2
import numpy as np
from pylab import plt

def f(x):
    return (x**4) - (2 * x) + 1

def simpson(fn, n, a, b):
    # Number of subintervals (n-1) must be an even number!
    if (n - 1) % 2 != 0:
        n += 1

    x = np.linspace(a, b, n)
    fn_vals = fn(x)
    fn_vals_odd = fn_vals[1 : n - 1 : 2]
    fn_vals_even = fn_vals[2 : n - 2 : 2]

    # Slice width
    h = (b - a) / (n - 1)

    # Integral value
    I = (h / 3) * (f(a) + (4 * sum(fn_vals_odd)) + (2 * sum(fn_vals_even)) + f(b))
    return I
    
# Integration bounds
a = 0
b = 2

# Steps (number of points)
n = 100

x_axis = np.linspace(a, b, n)
y_axis = f(x_axis)

print(f"Value of integral is {simpson(f, n, a, b)}")

# PLOTS
fig, ax1 = plt.subplots()

ax1_color = "red"
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.plot(x_axis, y_axis, color=ax1_color)

plt.grid()
plt.show()