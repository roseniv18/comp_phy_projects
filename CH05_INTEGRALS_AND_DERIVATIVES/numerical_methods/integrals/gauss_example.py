from gaussxw import gaussxw


def f(x):
    return x**4 - 2 * x + 1


a = 0.0
b = 2.0
N = 3

# Calculate sample points and weights.
# Then, map them to the required integration domain
x, w = gaussxw(N)
xp = 0.5 * (b - a) * x + 0.5 * (b + a)
wp = 0.5 * (b - a) * w
# Perform the integration
s = 0.0
for k in range(N):
    s += wp[k] * f(xp[k])
print(s)
