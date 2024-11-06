center_x = 0
center_y = 13.0 / 6.0

# Plot the circle using the imported points without showing them
fig, ax = plt.subplots()
ax.plot(x_coords, y_coords, label="Circle Outline")  # Just plot the outline

# Plot the center of the circle
ax.plot(center_x, center_y, 'ro', label="Center")  # 'ro' for red dot
ax.annotate(f'Center\n({center_x}, {center_y:.2f})', 
             (center_x, center_y), textcoords="offset points", 
             xytext=(5,5), ha='center')

# Set equal scaling to ensure the plot is circular
ax.set_aspect('equal', 'box')

# Plot configurations
plt.grid(True)
plt.title("Circle Plot from Imported Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Save and show plot
plt.savefig("circle_plot_with_center.png")
plt.show()

