from numpy import exp, linspace, log as ln
from pylab import plt
from gaussxw import gaussxwab

x_vals = linspace(0, 5, 100)
a_vals = [2, 3, 4]


def gamma(x):
    return x ** (a - 1) * exp(-x)


# Gamma integrand function after change of variables
def gamma_cov(z):
    az_term = ((a - 1) * z) / (1 - z)
    az_term_sq = (a - 1) / ((1 - z) ** 2)
    exp_term = exp((a - 1) * ln(az_term) - az_term)
    return exp_term * az_term_sq


# Bounds of integration (after change of variables)
lb = 0
ub = 1

# Number of points
N = 20


def gaussq(f, a_val):
    global a  # This is not ideal but will work for now
    a = a_val
    xp, wp = gaussxwab(N, lb, ub)
    I_val = 0
    for i in range(N):
        I_val += wp[i] * f(xp[i])
    return I_val


# For each a value, calculate ONE integral
gamma_values = []
for a in a_vals:
    gamma_val = gaussq(gamma_cov, a)
    gamma_values.append(gamma_val)

# Plot the original integrand for verification
plt.figure(figsize=(8, 6))
for a in a_vals:
    integrand_vals = []
    for x in x_vals:
        integrand_vals.append(gamma(x))
    plt.plot(x_vals, integrand_vals, label=f"a = {a}")

plt.xlabel("x")
plt.ylabel("Integrand")
plt.title("Original Gamma Function Integrand")
plt.legend()
plt.grid()
plt.show()

# Print the calculated gamma values
# for a, g in zip(a_vals, gamma_values):
#     print(f"Γ({a}) = {g}")

print(f"Γ({3/2}) = {gaussq(gamma_cov, 1.5)}")

print(f"Γ({3}) = {gaussq(gamma_cov, 3)}")
print(f"Γ({6}) = {gaussq(gamma_cov, 6)}")
print(f"Γ({10}) = {gaussq(gamma_cov, 10)}")
