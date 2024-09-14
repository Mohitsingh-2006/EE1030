import numpy as np
import matplotlib.pyplot as plt

points = {
    'A': (4, 2),
    'B': (6, 5),
    'C': (1, 4),
    'E': (2.5, 3),
    'F': (5, 3.5),
    'Q': (3.6667, 3.6667)  # Assuming Q is known or calculated
}

def interpolate(p1, p2, num_points):
    return np.linspace(p1, p2, num_points)

num_intermediate_points = 10
A = np.array(points['A'])
B = np.array(points['B'])
C = np.array(points['C'])
E = np.array(points['E'])
F = np.array(points['F'])

# Create lines between specific points
line_AB = interpolate(A, B, num_intermediate_points)
line_AC = interpolate(A, C, num_intermediate_points)
line_CF = interpolate(C, F, num_intermediate_points)
line_BC = interpolate(B, C, num_intermediate_points)
line_BE = interpolate(B, E, num_intermediate_points)

# Create the plot
plt.figure(figsize=(10, 8))

# Plot the specific points
for point, coord in points.items():
    plt.plot(coord[0], coord[1], 'o', label=f"{point} ({coord[0]}, {coord[1]})")
    plt.text(coord[0], coord[1], f'{point} ({coord[0]}, {coord[1]})', fontsize=12, ha='right')

plt.plot(line_AB[:, 0], line_AB[:, 1], 'r--', label="Line AB")
plt.plot(line_AC[:, 0], line_AC[:, 1], 'g--', label="Line AC")
plt.plot(line_CF[:, 0], line_CF[:, 1], 'b--', label="Line CF")
plt.plot(line_BC[:, 0], line_BC[:, 1], 'c--', label="Line BC")
plt.plot(line_BE[:, 0], line_BE[:, 1], 'm--', label="Line BE")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of Specific Points with Lines")
plt.legend()

plt.grid(True)
plt.show()

