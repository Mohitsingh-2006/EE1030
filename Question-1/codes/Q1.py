import numpy as np
import matplotlib.pyplot as plt

# Load data from file 'values.dat' (assuming each line contains coordinates x, y)
f = open("values.dat", "r")
data = np.loadtxt(f,skiprows=1)

# Assign points A, B, C from the file
A = data[0]  # First row is A
B = data[1]  # Second row is B
C = data[2]  # Third row is C

# Midpoints of sides AC and AB
E = (A + C) / 2
F = (A + B) / 2

# Points Q and R on the medians, dividing in the ratio 2:1
# BQ:QE = 2:1, Q = (2E + B) / 3
Q = (2*E + B) / 3

# CR:RF = 2:1, R = (2F + C) / 3
R = (2*F + C) / 3

# Data for plotting
x_vals = np.array([A[0], B[0], C[0], A[0]])  # Close the triangle
y_vals = np.array([A[1], B[1], C[1], A[1]])

# Plot the triangle
plt.plot(x_vals, y_vals, label="Triangle ABC")

# Plot medians BE and CF
plt.plot([B[0], E[0]], [B[1], E[1]], linestyle='--', label="Median BE")
plt.plot([C[0], F[0]], [C[1], F[1]], linestyle='--', label="Median CF")

# Plot points A, B, C, E, F, Q, R
plt.scatter(*A, color='red', label=f'A {A}')
plt.scatter(*B, color='green', label=f'B {B}')
plt.scatter(*C, color='blue', label=f'C {C}')
plt.scatter(*E, color='purple', label=f'E {E}')
plt.scatter(*F, color='orange', label=f'F {F}')
plt.scatter(*Q, color='cyan', label=f'Q {Q.round(2)}')
plt.scatter(*R, color='magenta', label=f'R {R.round(2)}')

# Annotating the points
plt.text(A[0]+0.1, A[1], 'A', fontsize=12)
plt.text(B[0]+0.1, B[1], 'B', fontsize=12)
plt.text(C[0]+0.1, C[1], 'C', fontsize=12)
plt.text(E[0]+0.1, E[1], 'E', fontsize=12)
plt.text(F[0]+0.1, F[1], 'F', fontsize=12)
plt.text(Q[0]+0.1, Q[1], 'Q', fontsize=12)
plt.text(R[0]+0.1, R[1], 'R', fontsize=12)

# Axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle ABC with Medians BE and CF and Points Q, R')

# Display grid, legend, and equal scaling
plt.grid(True)
plt.legend()
plt.axis('equal')

# Save and show the plot
plt.savefig('triangle_plot_from_file.png')
plt.show()

