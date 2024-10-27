import matplotlib.pyplot as plt
import numpy as np

# Define the sieve sizes (x-axis) and percentage passing (y-axis) for two curves
sieve_size_forward = np.linspace(0, 100, 100)  # Forward path
sieve_size_reverse = np.linspace(100, 0, 100)  # Reverse path

# Forward path
Q_forward = 1 / (1 + np.exp(-0.09 * (sieve_size_forward - 48))) * 10000  # Curve Q forward
R_forward = 1 / (1 + np.exp(-0.09 * (sieve_size_forward - 61))) * 10000  # Curve R forward

# Reverse path (with a small offset to create hysteresis effect)
Q_reverse = 1 / (1 + np.exp(-0.09 * (sieve_size_reverse - 50))) * 10000 - 500  # Curve Q reverse
R_reverse = 1 / (1 + np.exp(-0.09 * (sieve_size_reverse - 63))) * 10000 - 500  # Curve R reverse

# Plotting the graph
plt.figure(figsize=(10, 6))  # Make the figure wider

# Forward path plot
plt.plot(sieve_size_forward - 50, Q_forward - np.max(Q_forward)/2, 'k-', label='Q Forward')
plt.plot(sieve_size_forward - 50, R_forward - np.max(Q_forward)/2, 'k-', label='R Forward')

# Reverse path plot
plt.plot(sieve_size_reverse - 50, Q_reverse - np.max(Q_forward)/2, 'k--', label='Q Reverse')
plt.plot(sieve_size_reverse - 50, R_reverse - np.max(Q_forward)/2, 'k--', label='R Reverse')

# Adjust x-axis limits to make it symmetric and wider around the origin
x_margin = 20  # Add extra margin on both sides of the x-axis
plt.xlim(-(50 + x_margin), 50 + x_margin)

# Adding horizontal and vertical lines at the origin
plt.axhline(y=0, color='gray', linestyle='-')  # horizontal line at midpoint
plt.axvline(x=0, color='gray', linestyle='-')  # vertical line at midpoint

# Labels and title
plt.xlabel('Sieve size (relative to midpoint)')
plt.ylabel('Percentage passing (relative to midpoint)')
plt.legend(loc='upper left')

# Saving the plot as 'graph.png'
plt.savefig('graph.png')

plt.show()

