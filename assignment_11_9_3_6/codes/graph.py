import matplotlib.pyplot as plt
import numpy as np

def plot_stem(n_values, x_func, label, filename):
    y_values = np.heaviside(n_values, 0) * x_func(n_values)
    plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt='r', label=label)
    plt.xlabel('n')
    plt.ylabel("x(n)")
    plt.title(f"Stem Plot of {label}")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def x_func(n):
    return (-7/2)**(n-1)

def y_func(n):
    return -(7/2)**(n-1)

n_values = np.arange(0, 10, 1)

plot_stem(n_values, x_func, r'$(-7/2)^{n-1}$', "graph1.png")
plot_stem(n_values, y_func, r'$-(7/2)^{n-1}$', "graph2.png")
