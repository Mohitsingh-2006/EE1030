import matplotlib.pyplot as plt
import numpy as np

# Define half-ellipse shape
t = np.linspace(0, np.pi, 100)
x = np.cos(t)
y = np.sin(t)

# Plot the half-ellipse
plt.figure()
plt.plot(x, y, 'black')
plt.plot(x, -y, 'black')

# Draw horizontal arrows within the half-ellipse
for y_val in np.linspace(-0.8, 0.8, 10):
    plt.arrow(-1, y_val, 1.8, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')

plt.axis('equal')
plt.axis('off')
plt.show()

