from numpy import sqrt, linspace
from gaussxw import gaussxwab
from pylab import plt

# Mass of particle
m = 1

# Points
N = 20
# Lower bound
a = 0.0
# Amplitude vals
a_vals = linspace(0.1, 2, N)


def v(x):
    return x**4


# Period
def T(x):
    return sqrt(8 * m) / (sqrt(v(amplitude) - v(x)))


# Gaussian quadratue
def gaussq(f, b):
    # Calculate points and weights
    xp, wp = gaussxwab(N, a, b)
    # Integral value
    I_val = 0.0

    for k in range(N):
        I_val += wp[k] * f(xp[k])

    return I_val


I_vals = list()

for amplitude in a_vals:
    I_vals.append(gaussq(T, amplitude))


plt.plot(a_vals, I_vals, "b.")
plt.xlabel("Amplitude [m]")
plt.ylabel("Period [s]")
plt.title("Period of a particle in a potential well")
plt.grid()
plt.show()
