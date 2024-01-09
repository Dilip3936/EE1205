import matplotlib.pyplot as plt
import numpy as np

def x(n):
        return (-7/2)**(n-1)
n_values= np.arange(0, 10, 1)

y= np.heaviside(n_values, 0) *x(n_values)

plt.stem(n_values, y, linefmt='-', markerfmt='o', basefmt='r', label=r'$(-7/2)^{n-1}$')

plt.xlabel('n')
plt.ylabel("x(n)")
plt.title("Stem Plot of $x(n)$")
plt.legend()
plt.grid(True)
plt.show()
