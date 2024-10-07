import numpy as np
import matplotlib.pyplot as plt

# Load points from the 'points.dat' file (Assuming it has x, y_parabola, y_line columns)
points = np.loadtxt('points.dat', delimiter=',')

# Extract the x values, y values for parabola, and y values for line
x_vals = points[:, 0]
y_parabola_vals = points[:, 1]
y_line_vals = points[:, 2]

# Plot the parabola
plt.plot(x_vals, y_parabola_vals, label='Parabola: $y = x^2$', color='blue', linewidth=2)

# Plot the line y = 2.86x + 2 (loaded from the points)
plt.plot(x_vals, y_line_vals, label='Line: $y = 2.86x + 2$', color='red', linestyle='--', linewidth=2)

# Fill the area between the parabola and the line where x_vals are valid
plt.fill_between(x_vals, y_parabola_vals, y_line_vals, where=(y_parabola_vals <= y_line_vals),
                 color='purple', alpha=0.3, label='Shaded Region')

# Label the axes and add a title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola and Line with Shaded Area')

# Add grid and legend
plt.grid(True)
plt.legend()

# Save the plot to a file
plt.savefig('Figure_1.png')

# Show the plot
plt.show()

