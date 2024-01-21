import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
a=-2/7
r1=-7/2
r2=7/2
y1=a*(r1**x)
y2=a*(r2**x)

plt.stem(x, y1, linefmt='-', markerfmt='o', basefmt='r', label= r'$(-7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph1.png")
plt.clf() 

plt.stem(x, y2, linefmt='-', markerfmt='o', basefmt='r', label=r'$-(7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph2.png")
