import numpy as np
import matplotlib.pyplot as plt

# Function to calculate a point that divides a line segment in a given ratio
def divide_line(P, Q, m, n):
    x = (m * Q[0] + n * P[0]) / (m + n)
    y = (m * Q[1] + n * P[1]) / (m + n)
    return np.array([x, y]).reshape(-1,1)

# Read points from 'lines.dat' using np.loadtxt
f = open("lines.dat", "r")
lines = np.loadtxt(f)

# Initialize arrays for line segments with 11 points each
x_AB = np.zeros((2, 11))
x_BC = np.zeros((2, 11))
x_CA = np.zeros((2, 11))
x_BE = np.zeros((2, 11))
x_CF = np.zeros((2, 11))

# Fill in the arrays with points from the file
x_AB[0,:] = lines[:, 0]
x_AB[1,:] = lines[:, 1]
x_BC[0,:] = lines[:, 2]
x_BC[1,:] = lines[:, 3]
x_CA[0,:] = lines[:, 4]
x_CA[1,:] = lines[:, 5]
x_BE[0,:] = lines[:, 6]
x_BE[1,:] = lines[:, 7]
x_CF[0,:] = lines[:, 8]
x_CF[1,:] = lines[:, 9]

# Extract points A, B, C, E, and F
A = np.array([x_AB[0,0], x_AB[1,0]]).reshape(-1,1)
B = np.array([x_AB[0,-1], x_AB[1,-1]]).reshape(-1,1)
C = np.array([x_BC[0,-1], x_BC[1,-1]]).reshape(-1,1)
E = np.array([x_BE[0,-1], x_BE[1,-1]]).reshape(-1,1)
F = np.array([x_CF[0,-1], x_CF[1,-1]]).reshape(-1,1)

# Calculate points Q and R dividing the medians in the ratio 2:1
Q = divide_line(B, E, 2, 1)
R = divide_line(C, F, 2, 1)

# Plot the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the triangle and medians
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$', color='r')  # Line AB
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$', color='g')  # Line BC
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$', color='b')  # Line CA

# Plot medians BE and CF
plt.plot(x_BE[0,:], x_BE[1,:], '--', label='$BE$', color='m')
plt.plot(x_CF[0,:], x_CF[1,:], '--', label='$CF$', color='c')

# Plot the points Q and R
plt.scatter(Q[0], Q[1], color='k', label='Point Q (2:1 on BE)')
plt.scatter(R[0], R[1], color='k', label='Point R (2:1 on CF)')

# Label the points
tri_coords = np.hstack((A, B, C, Q, R, E, F))
vert_labels = ['A', 'B', 'C', 'Q', 'R', 'E', 'F']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})', 
                 (tri_coords[0,i], tri_coords[1,i]), textcoords="offset points", 
                 xytext=(0,5), ha='center')

# Adding x and y axis arrows
plt.arrow(0, 0, 8, 0, width=0.005, length_includes_head=True, 
          head_width=0.3, overhang=0.5)
plt.arrow(0, 0, 0, 8, width=0.005, length_includes_head=True, 
          head_width=0.3, overhang=0.5)

# Set the axis limits to zoom into the first quadrant with x and y ranges from 0 to 8
plt.xlim(0, 8)
plt.ylim(0, 8)

# Set axes, grid, and legend
plt.legend(loc='upper left')
plt.grid()
plt.axis('equal')

# Save and show the plot
plt.savefig('Figure_1.png')
plt.show()

# Close the file
f.close()

