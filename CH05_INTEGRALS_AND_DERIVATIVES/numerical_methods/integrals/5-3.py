import numpy as np
from pylab import plt

def E(x):
    return np.exp(-x**2)

# Integration bounds
a = 0
b = 3

n = 31

# Slice width
h = (b - a) / n

# Number of subintervals (n-1) must be an even number!
are_subintervals_even = True
if (n - 1) % 2 != 0:
    are_subintervals_even = False

# Number of steps
n = n if not are_subintervals_even else n - 1

x_vals = np.linspace(a, b, n)
# fn_vals = np.array([E(a + i * h) for i in range(n)])
fn_vals = E(x_vals)

# Integration using Simpson's Rule
def simpson(f, a, b, n):
    # Simpson's Rule values
    s_vals = np.zeros(n)
    s_vals[0] = f(a)
    s_vals[-1] = f(b)

    # Integral value
    I = f(a) + f(b)

    for k in range(1, n):
        # Value at k-th step
        val_k = f(a + (k * h))

        if k % 2 != 0:
            s_vals[k] = 4 * val_k
            I += 4 * val_k
            # s_vals[k] = 4 * fn_vals[k]
        else:
            s_vals[k] = 2 * val_k
            I += 2 * val_k
            # s_vals[k] = 2 * fn_vals[k]

    # Integral value
    I *= (h / 3)
    # Cumulative sum for intermediate integral values
    I_vals = (h / 3) * np.cumsum(s_vals)
    return I, I_vals

def trapezoid(f, a, b, n):
    # Trapezoidal rule
    tr = (0.5 * f(a)) + (0.5 * f(b))
    tr_vals = np.zeros(n)
    tr_vals[0] = 0.5 * f(a)
    tr_vals[-1] = 0.5 * f(b)

    for k in range(1, n):
        tr += f(a + (k * h))
        tr_vals[k] = f(a + (k * h))

    # Integral value
    I = h * tr
    I_vals = h * np.cumsum(tr_vals)
    return I, I_vals

I_Trapezoid, I_Trapezoid_vals  = trapezoid(E, a, b, n)
I_Simpson, I_Simpson_vals = simpson(E, a, b, n)
print(f"Value of integral using Trapezoid Rule: {I_Trapezoid}")
print(f"Value of integral using Simpson's Rule: {I_Simpson}")

# PLOTS
fig, ax1 = plt.subplots()
ax1_color = "green"
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)", color=ax1_color)
ax1.plot(x_vals, fn_vals, color=ax1_color, label="f(x)")

plt.grid()

print(I_Trapezoid_vals)
print(I_Simpson_vals)

ax2_color = "red"
ax2 = ax1.twinx()
ax2.set_ylabel("Integration", color=ax2_color)
ax2.plot(x_vals, I_Trapezoid_vals, color=ax2_color, label="Trapezoidal")
ax2.plot(x_vals, I_Simpson_vals, color="purple", label="Simpson's Rule")

fig.legend(loc="upper center")
plt.show()
