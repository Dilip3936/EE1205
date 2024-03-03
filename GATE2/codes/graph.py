import matplotlib.pyplot as plt

# Read data from file
data = []
with open('data.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data.append((x, y))

# Separate x and y values
frequencies = [point[0] for point in data]
values = [point[1] for point in data]

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(frequencies, values, label=r'X(f)', color='blue')
plt.xlabel('Frequency (f)')
plt.ylabel('Function Value')
plt.grid(True)
plt.legend()
plt.savefig("graph.png")
