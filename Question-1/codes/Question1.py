#Code by GVV Sharma
#September 12, 2023
#released under GNU GPL
#Medians of a triangle
#Centroid

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Function to generate a line segment between two points
def line_gen(A, B):
    len = 100
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(0, 1, len)
    for i in range(len):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.T
    return x_AB

# Function to calculate the normal vector to the line passing through two points
def norm_vec(A, B):
    return np.array([A[1] - B[1], B[0] - A[0]])

# Function to find the intersection of two lines given by their normal vectors and points
def line_intersect(n1, A, n2, B):
    N = np.vstack((n1.T, n2.T))
    p = np.array([n1.T @ A, n2.T @ B])
    return np.linalg.solve(N, p)

# Triangle vertices
A = np.array([4, 2]).reshape(-1,1)
B = np.array([6, 5]).reshape(-1,1) 
C = np.array([1, 4]).reshape(-1,1) 

# Midpoints of sides opposite to the vertices
D = (B + C) / 2
E = (C + A) / 2
F = (A + B) / 2

# Centroid G (intersection of medians)
G = (A + B + C) / 3

# Calculate the coordinates of points Q and R
# For BQ : QE = 2 : 1
Q = (2 * E + B) / 3
# For CR : RF = 2 : 1
R = (2 * F + C) / 3

# Generating all lines
x_AD = line_gen(A, D)
x_BE = line_gen(B, E)
x_CF = line_gen(C, F)
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$')
plt.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
plt.plot(x_BE[0,:], x_BE[1,:], label='$BE$')
plt.plot(x_CF[0,:], x_CF[1,:], label='$CF$')

# Plotting the points A, B, C, G, Q, R
points = np.hstack((A, B, C, G, Q, R))
labels = ['A', 'B', 'C', 'G', 'Q', 'R']

plt.scatter(points[0,:], points[1,:])
for i, label in enumerate(labels):
    plt.annotate(label, 
                 (points[0,i], points[1,i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Uncomment the following line to display the plot
plt.show()

# If using termux
# plt.savefig('figs/triangle/medians_with_Q_R.pdf')
# subprocess.run(shlex.split("termux-open figs/triangle/medians_with_Q_R.pdf"))

