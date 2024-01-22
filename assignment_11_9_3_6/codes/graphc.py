import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.txt")
n_values, y1, y2 = data[:, 0], data[:, 1], data[:, 2]

plt.stem(n_values, y1, linefmt='-', markerfmt='o', basefmt='r', label=r'$(-7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph1.png")
plt.clf()

plt.stem(n_values, y2, linefmt='-', markerfmt='o', basefmt='r', label=r'$-(7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph2.png")
