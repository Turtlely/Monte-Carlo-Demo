# Monte Carlo demonstration of its ability to calculate integrals numerically.
import numpy as np
import matplotlib.pyplot as plt

# Gaussian Integral

def f(x):
    return np.exp(-(x**2))

# Bounds for the monte carlo simulation
a = -10

b = 10
y=1

# Number of points
n = 1000

x_sample = (b-a)*np.random.rand(n) - b
y_sample = y*np.random.rand(n)

y_real = f(x_sample)

in_bound = 0

y_in = []
x_in = []

y_out = []
x_out = []

for i in range(n):
    if y_sample[i] < y_real[i]:
        in_bound+=1
        y_in.append(y_sample[i])
        x_in.append(x_sample[i])
    else:
        y_out.append(y_sample[i])
        x_out.append(x_sample[i])

print(y*(b-a)*in_bound/n)

x_plot = np.linspace(a,b,10*(b-a))
plt.plot(x_plot,f(x_plot),c='red')
plt.scatter(x_in,y_in,c="orange",label="Inside Curve")
plt.scatter(x_out,y_out,c="blue",label="Outside Curve")
plt.title(f"Monte Carlo Integration Method with {n} sample points")
plt.legend()
plt.show()