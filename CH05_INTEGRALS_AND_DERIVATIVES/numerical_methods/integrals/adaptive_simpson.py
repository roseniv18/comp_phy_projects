import numpy as np
from pylab import plt


def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2


# BOUNDS
a = 0
b = 1

# INITIAL NUMBER OF STEPS
N = 2

# ACCURACY
accuracy = 1e-6


def my_simpson(N, I_prev=0):
    # SLICE WIDTH
    h = (b - a) / N
    # NUMBER OF POINTS
    x = np.linspace(a, b, N + 1)
    # WEIGHT COEFFICIENTS
    weight = np.ones(N + 1)
    weight[0] = 1 / 3
    weight[-1] = 1 / 3
    weight_S, weight_T = weight, weight
    # SKIP ODD TERMS FOR S
    weight_S[1::2] = 0
    # SKIP EVEN TERMS FOR T
    weight_T[0::2] = 0

    S = (1 / 3) * (f(a) + f(b)) + 2 * sum(weight_S * f(x))  # Eq. 5.36
    T = (2 / 3) * sum(weight_T * f(x))  # Eq. 5.37
    I = h * (S + 2 * T)  # Eq. 5.39
    err = calc_err(I, I_prev)
    return I, err  # integral, estimated error


def calc_err(I, I_prev):
    return (1 / 15) * (I - I_prev)


Ivals, Evals, Nvals = list(), list(), list()
I0, err = my_simpson(N)

while abs(err) > accuracy:
    N *= 2
    I0, err = my_simpson(N, I0)

    Ivals.append(I0)
    Evals.append(err)
    Nvals.append(N)

hz = np.ones(len(Nvals)) * 1e-6
plt.figure(figsize=(7, 4))
plt.title("Estimated error of the adaptive Simpson's integration")
plt.ylabel("Estimtated error")
plt.xlabel("Number of slices")
plt.plot(Nvals, Evals, "b--")
plt.plot(Nvals, hz, "k")
plt.xlim(0, 200)
plt.show()

print(f"An accuracy of 1e-6 is reached at the number of slices N = {N}")
