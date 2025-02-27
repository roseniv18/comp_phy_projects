from numpy import sin, linspace
from pylab import plt

def f(x):
    if x == 0:
        return 1.0
    else:
        return ((sin(x))**2)/(x**2)

err = 1e-4

# Bounds
a = 0
b = 10

# Store unique x-values where we evaluate f(x)
eval_points = set()

def adv_trapz(x1, x2, f1, f2):
    eval_points.add(x1)
    eval_points.add(x2)
    
    h = x2 - x1
    # First estimate using one slice
    I1 = h * (f1 + f2) / 2
    
    # Second estimate using two slices
    xm = (x1 + x2) / 2  # Midpoint
    eval_points.add(xm)
    fm = f(xm)          # Function value at midpoint
    # Trapezoid rule
    # I2 = (h/2) * ((f1 + fm)/2 + (fm + f2)/2)
    # Simpson's Rule
    I2 = (h/6) * (f1 + (4*fm) + f2)
    
    # Calculate error and target accuracy for this interval
    error = abs(I2 - I1) / 3
    target_accuracy = err * (h / (b - a))
    
    if error <= target_accuracy:
        return I2
    else:
        # Recursively compute integrals of left and right halves
        left = adv_trapz(x1, xm, f1, fm)
        right = adv_trapz(xm, x2, fm, f2)
        return left + right
        
        
print(adv_trapz(a, b, f(a), f(b)))

# PLOTTING
x_vals = linspace(a, b, 1000)
y_vals = [f(x) for x in x_vals]

x_evals = list(eval_points)
y_evals = [f(x) for x in x_evals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, "b-", label="f(x)=sin²(x)/x²")
plt.plot(x_evals, y_evals, "r.", markersize=4, label="Integration Points")
plt.grid(True)
plt.legend()
plt.title("Adaptive Trapezoidal / Simpson's Integration Points")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
