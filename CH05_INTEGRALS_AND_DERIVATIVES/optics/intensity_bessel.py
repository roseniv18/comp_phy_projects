from numpy import zeros, pi, cumsum, linspace, empty, sqrt, sin, cos, loadtxt
from pylab import plt


def Jm(m, x, theta):
    return cos(m * theta - x * sin(theta))


n = 100
# Lower bound of integration
a = 0
# Upper bound of integration
b = pi

intensity_data = loadtxt("../resources/intensity.txt", dtype=float)

# # Slice width
# h = (b - a) / (n - 1)

# def Simpson(m, p, n):
# 	# Number of subintervals (n-1) must be an even number!
# 	if (n-1) % 2 != 0:
# 		n += 1

# 	 # Simpson's Rule values
# 	s_vals = zeros(n)
# 	s_vals[0] = Jm(m, p, a)
# 	s_vals[-1] = Jm(m, p, b)

# 	# Integral value
# 	I = s_vals[0] + s_vals[-1]

# 	for k in range(1, n):
# 		# Value at k-th step
# 		val_k = Jm(m, p, a + (k * h))

# 		if k % 2 != 0:
# 			s_vals[k] = 4 * val_k
# 			I += 4 * val_k
# 			# s_vals[k] = 4 * fn_vals[k]
# 		else:
# 			s_vals[k] = 2 * val_k
# 			I += 2 * val_k
# 			# s_vals[k] = 2 * fn_vals[k]

# 	# Integral value
# 	I *= (h / 3)
# 	# Cumulative sum for intermediate integral values
# 	I_vals = (h / 3) * (1 / pi) * cumsum(s_vals)
# 	return I, I_vals


# # Lambda value
# lmb = 500e-9

# # r - distance in the focal plane from the center of the diffraction pattern
# # Lower bound of r
# r_a = 0
# # Upper bound of r (1 micro meter)
# r_b = 1e-6

# # Intensity
# def I(lmb, r):
# 	k = 2 * pi / lmb
# 	return ((Simpson(1, k*r, n)[0]) / (k*r))**2

# points = 500
# Intensity = empty([points, points], dtype=float)
# separation = 20e-4
# I0 = 1

# # print(I(lmb, r_b))

# for i in range(points):
# 	y = separation * (i - points/2)
# 	for j in range(points):
# 		x = separation * (j - points/2)
# 		r = sqrt(x**2 + y**2)
# 		if r < r_b:
# 			Intensity[i, j] = 0.5
# 		else:
# 			Intensity[i, j] = I0 * I(lmb, r)

# print(Intensity)

plt.imshow(intensity_data, vmax=0.001, cmap="hot")
# plt.gray()
plt.show()

# r_vals = linspace(r_a, r_b, 100)
