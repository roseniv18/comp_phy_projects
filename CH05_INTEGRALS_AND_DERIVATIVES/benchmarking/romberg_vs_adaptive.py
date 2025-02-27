# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comparative benchmark script to
# demonstrate the efficiency of the Romberg integration
# when compared to the adaptive trapezoid method.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import numpy as np
import time
import matplotlib.pyplot as plt


def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2


def adaptive_trapezoid(f, a, b, accuracy=1e-6):
    N = 10

    def my_trapz(N, I_prev):
        h = (b - a) / N
        x = np.linspace(a, b, N + 1)
        weight = np.ones(N + 1)
        weight[0] = 0.5
        weight[-1] = 0.5
        weight[::2] = 0
        I = 0.5 * I_prev + h * sum(weight * f(x))
        return I

    approx_value = my_trapz(N, 0)
    iterations = 1

    while True:
        N *= 2
        approx_value_new = my_trapz(N, approx_value)
        error = np.abs(approx_value_new - approx_value) / 3
        iterations += 1

        if error < accuracy + 1e-6:
            break
        approx_value = approx_value_new

    return approx_value, iterations


def romberg_integration(f, a, b, accuracy=1e-6, max_iterations=20):
    R = np.zeros((max_iterations, max_iterations))

    for i in range(max_iterations):
        n = 2**i
        h = (b - a) / n

        x = np.linspace(a, b, n + 1)
        R[i, 0] = h / 2 * (f(a) + 2 * np.sum(f(x[1:-1])) + f(b))

        for j in range(1, i + 1):
            R[i, j] = (4**j * R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

        if i > 0:
            error = abs(R[i, i] - R[i - 1, i - 1])
            if error < accuracy:
                return R[i, i], i + 1

    return R[max_iterations - 1, max_iterations - 1], max_iterations


def run_benchmark(num_runs=50):
    trapezoid_times = []
    romberg_times = []
    trapezoid_iterations = []
    romberg_iterations = []

    for _ in range(num_runs):
        # Trapezoid Method
        start = time.time()
        trap_result, trap_iterations = adaptive_trapezoid(f, 0, 1)
        trapezoid_times.append(time.time() - start)
        trapezoid_iterations.append(trap_iterations)

        # Romberg Method
        start = time.time()
        romberg_result, romberg_iter = romberg_integration(f, 0, 1)
        romberg_times.append(time.time() - start)
        romberg_iterations.append(romberg_iter)

    # Plotting and analysis
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.title("Computation Time Comparison")
    plt.boxplot([trapezoid_times, romberg_times], labels=["Trapezoid", "Romberg"])
    plt.ylabel("Time (seconds)")

    plt.subplot(1, 2, 2)
    plt.title("Iterations to Convergence")
    plt.boxplot(
        [trapezoid_iterations, romberg_iterations], labels=["Trapezoid", "Romberg"]
    )
    plt.ylabel("Number of Iterations")

    plt.tight_layout()
    plt.show()

    print("Trapezoid Method:")
    print(f"Avg Time: {np.mean(trapezoid_times) * 1000:.4f} ms")
    print(f"Avg Iterations: {np.mean(trapezoid_iterations):.2f}")

    print("\nRomberg Method:")
    print(f"Avg Time: {np.mean(romberg_times) * 1000:.4f} ms")
    print(f"Avg Iterations: {np.mean(romberg_iterations):.2f}")


run_benchmark()
