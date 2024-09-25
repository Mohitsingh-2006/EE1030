import matplotlib.pyplot as plt

# Read points from lines.dat
points = []
with open('lines.dat', 'r') as file:
    for line in file:
        # Assuming each line in the file contains two space-separated values (x, y)
        x, y = map(float, line.split())
        points.append((x, y))

# Separate the points into x and y values
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Create the plot for the line without showing points
plt.plot(x_values, y_values, color='blue', label='Line from File')  # Line from file

# Add labels, title, and legend
plt.title("Plot of a Line from 11 Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Add grid
plt.grid()

# Set axis limits based on the points
plt.xlim(min(x_values) - 1, max(x_values) + 1)  # Adjust x-axis limits
plt.ylim(min(y_values) - 1, max(y_values) + 1)  # Adjust y-axis limits
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Y-axis
plt.show()

