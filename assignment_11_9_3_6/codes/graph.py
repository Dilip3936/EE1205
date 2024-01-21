import matplotlib.pyplot as plt
import numpy as np

def plot_stem(n_values,a,r, label, filename):
    y_values = np.heaviside(n_values, 0) * func(n_values,a,r)
    plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt='r', label=label)
    plt.xlabel('n')
    plt.ylabel("x(n)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def func(n,a,r):
    return a*(r**n)

n_values = np.arange(0, 10, 1)
a=-2/7
r1=-7/2
r2=7/2
plot_stem(n_values, a,r1, r'$(-7/2)^{n-1}$', "graph1.png")
plot_stem(n_values, a,r2, r'$-(7/2)^{n-1}$', "graph2.png")
