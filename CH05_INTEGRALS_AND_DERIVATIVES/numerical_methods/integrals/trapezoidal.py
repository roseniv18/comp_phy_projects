def f(x):
    return x**4 -2*x + 1

# Integral bounds
a = 0.0
b = 2.0

# Steps
N = 10

# Width of trapezoid
h = (b - a) / N

# Sum of trapezoid side values
s = (0.5 * f(a)) + (0.5 * f(b))

for k in range(1, N):
    s += f(a + (k * h))

print(h * s)