import numpy as np
from pylab import plt


def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2


# BOUNDS
a = 0
b = 1

# INITIAL NUMBER OF STEPS
N = 10

# ACCURACY
accuracy = 1e-6

# INITIAL ERROR
# Purely for programming purposes
initial_error = 1


def my_trapz(N, I_prev):
    # TRAPEZOID WIDTH
    h = (b - a) / N
    # NUMBER OF POINTS
    x = np.linspace(a, b, N + 1)
    # WEIGHT COEFFICIENTS
    weight = np.ones(N + 1)
    weight[0] = 0.5
    weight[-1] = 0.5
    # SKIP EVEN TERMS
    weight[::2] = 0
    I = 0.5 * I_prev + h * sum(weight * f(x))
    return I


I1 = my_trapz(1, 0)
R_prev = list()
R_prev.append(I1)
err_romberg = initial_error


def my_romberg(m_max, R_prev):
    R = list()
    for m in range(m_max):
        m = int(m)

        if m == 0:
            R_curr = my_trapz(m_max, 0)
            error = calc_error(R_curr, R_prev[0])
        else:
            num = (1 / (4**m - 1)) * (R[m - 1] - R_prev[m - 1])
            R_curr = R[m - 1] + num  # Eq. 5.51
            error = num + h ** (2 * m + 2)  # Eq. 5.49

        R.append(R_curr)

    return R, error


# STEP VALUES LIST
N_vals = list()
N_vals.append(N)
# ERROR VALUES LIST
err_vals = list()
err_vals.append(initial_error)


def calc_error(INTEGRAL, INTEGRAL_prev):
    return np.abs(INTEGRAL - INTEGRAL_prev) / 3


# INITIAL APPROXIMATION
approx_value = my_trapz(N, 0)

# REFINEMENT LOOP FOR ADAPTIVE TRAPEZOID RULE
while True:
    # DOUBLE NUMBER OF STEPS ON EACH ITERATION
    N *= 2
    h = (b - a) / N

    approx_value_new = my_trapz(N, approx_value)
    error = calc_error(approx_value_new, approx_value)
    print(f"N: {N}, I: {approx_value_new}, eps: {error}")

    # APPEND TO LISTS
    N_vals.append(N)
    err_vals.append(error)

    # CHECK FOR DESIRED ACCURACY
    # Note: Add 1e-6 so that it stops when it reaches 1.999999e-06 instead of going to e-07 values.
    if (error) < accuracy + 1e-6:
        break

    # UPDATE APPROXIMATION
    approx_value = approx_value_new

# LOOP FOR ROMBERG INTEGRATION
i = 1
while abs(err_romberg) > accuracy:
    i += 1
    R_prev, err_romberg = my_romberg(i, R_prev)
    print(f"Slice {i}: {R_prev}\n")

print(
    f"The Romberg integration achieves an accuracy of 1e-6 for the number of slices N = {i}"
)


print(f"The approximate value of the integral is: {approx_value_new}")
print(f"Number of steps used: {N}")

hz = np.ones(len(N_vals)) * 1e-6
plt.figure(figsize=(7, 4))
plt.title("Estimated error of the adaptive trapezoidal integration")
plt.ylabel("Estimtated error")
plt.xlabel("Number of slices")
plt.plot(N_vals, err_vals, "b--")
plt.plot(N_vals, hz, "k")
plt.xlim(0, 200)
plt.show()
