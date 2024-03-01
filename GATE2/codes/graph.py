import numpy as np
import matplotlib.pyplot as plt

# Define the function
def my_function(f):
    return (np.sin(np.pi * f) / (np.pi * f))**2

# Generate x values (frequencies)
frequencies = np.linspace(-10, 10, 1000)  # You can adjust the range and density of points

# Calculate corresponding y values
values = my_function(frequencies)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(frequencies, values, label=r'X(f)',color='blue')
plt.xlabel('Frequency (f)')
plt.ylabel('X(f)')
plt.grid(True)
plt.legend()
plt.savefig('graph.png')
