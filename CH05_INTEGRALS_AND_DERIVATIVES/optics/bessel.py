import numpy as np
from pylab import plt

# Number of steps
n = 100000

# Integration bounds
a = 0
b = np.pi

# Slice width
h = (b - a) / (n - 1)

def Jm(m, p, theta):
	return np.cos(m*theta - p*np.sin(theta))

''' 
Numerical Integration using Simpson's Rule
f - function to be integrated
a - lower integration bound
b - upper integration bound
n - number of points / steps	
'''
def Simpson(m, p):
	 # Simpson's Rule values
    s_vals = np.zeros(n)
    s_vals[0] = Jm(m, p, a)
    s_vals[-1] = Jm(m, p, b)

    # Integral value
    I = Jm(m, p, a) + Jm(m, p, b)

    for k in range(1, n):
        # Value at k-th step
        val_k = Jm(m, p, a + (k * h))

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
    I_vals = (h / 3) * (1 / np.pi) * np.cumsum(s_vals)
    return I, I_vals

x_vals = np.linspace(0, 100, n)

# 
for p in range(1):
    #  Calculate integral values for m=1, m=2 and m=3
	Jm_Simpson, Jm_1_Simpson_vals = Simpson(1, p)
	Jm_Simpson, Jm_2_Simpson_vals = Simpson(2, p)
	Jm_Simpson, Jm_3_Simpson_vals = Simpson(3, p)

	# PLOTS
	fig, ax1 = plt.subplots()
	ax1_color = "green"
	ax1.set_xlabel("x")
	ax1.set_ylabel("Jm_1(p)", color=ax1_color)
	ax1.plot(x_vals, Jm_1_Simpson_vals, color=ax1_color, label="Jm_1(p)")
	ax1.legend(loc="upper left")

     
	ax2 = ax1.twinx()
	ax2_color = "blue"
	ax2.set_ylabel("Jm_2(p)", color=ax2_color)
	ax2.plot(x_vals, Jm_2_Simpson_vals, color=ax2_color, label="Jm_2(p)")
	ax2.legend(loc="upper center")

     
	ax3 = ax1.twinx()
	ax3_color = "red"
	ax3.set_ylabel("Jm_3(p)", color=ax3_color)
	ax3.plot(x_vals, Jm_3_Simpson_vals, color=ax3_color, label="Jm_3(p)")
	ax3.legend(loc="upper right")
	
	plt.grid()
	plt.show()
