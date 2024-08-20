import matplotlib.pyplot as plt

# Coordinates of the vertices
A = (4, 2)
B = (6, 5)
C = (1, 4)

# Midpoints of the sides
E = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)  # Midpoint of AC
F = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)  # Midpoint of AB

# Centroid (and points Q and R as they coincide with the centroid)
G = Q = R = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

# Plotting the triangle
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-', label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], 'bo-', label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], 'bo-', label='CA')

# Plotting the medians
plt.plot([B[0], E[0]], [B[1], E[1]], 'r--', label='BE (Median)')
plt.plot([C[0], F[0]], [C[1], F[1]], 'g--', label='CF (Median)')

# Plotting the points Q, R, and G
plt.plot(Q[0], Q[1], 'ro', label='Q (2:1 on BE)')
plt.plot(R[0], R[1], 'go', label='R (2:1 on CF)')
plt.plot(G[0], G[1], 'ko', label='G (Centroid)')

# Labels and title
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')
plt.text(E[0], E[1], 'E', fontsize=12, ha='right')
plt.text(F[0], F[1], 'F', fontsize=12, ha='right')
plt.text(G[0], G[1], 'G/Q/R', fontsize=12, ha='left')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle with Medians and Points Q and R')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show plot
plt.show()

