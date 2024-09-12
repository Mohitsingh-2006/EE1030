#Code by GVV Sharma
#September 12, 2023
#released under GNU GPL
#Medians of a triangle
#Centroid
#for path to external scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

# Triangle vertices
A = np.array([4,2]).reshape(-1,1)
B = np.array([6,5]).reshape(-1,1)
C = np.array([1,4]).reshape(-1,1)

# Triangle midpoints
E = (C + A) / 2  # Midpoint of CA
F = (A + B) / 2  # Midpoint of AB
#print(E,F)

# Median parameters
n1 = norm_vec(A, E)
c1 = n1.T @ A
n2 = norm_vec(B, F)
c2 = n2.T @ B

# Intersecton of BE and CF (Centroid G)
G = line_intersect(n1, A, n2, B)

# Point division on medians BE and CF
def divide_point(P, Q, m, n):
    return (n * P + m * Q) / (m + n)

# Points Q and R on medians BE and CF such that BQ:QE = 2:1 and CR:RF = 2:1
Q = divide_point(B, E, 2, 1)  # BQ : QE = 2 : 1
R = divide_point(C, F, 2, 1)  # CR : RF = 2 : 1
print("Coordinates of Q:", Q)
print("Coordinates of R:", R)

# Collinearity check (for validation)
mat = np.block([[1, 1, 1], [A, G, E]]).T
print("Matrix rank check (for collinearity):", LA.matrix_rank(mat))

# Generating lines for plotting
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)
x_BE = line_gen(B, E)
x_CF = line_gen(C, F)

# Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$')
plt.plot(x_BE[0,:], x_BE[1,:], label='$BE$')
plt.plot(x_CF[0,:], x_CF[1,:], label='$CF$')

# Labeling the coordinates
tri_coords = np.block([[A, B, C, Q, R, E, F]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A', 'B', 'C', 'Q', 'R','E','F']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,  # this is the text
                 (tri_coords[0,i], tri_coords[1,i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0,10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/median_Q_R.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/median_Q_R.pdf"))
#else
plt.show()

