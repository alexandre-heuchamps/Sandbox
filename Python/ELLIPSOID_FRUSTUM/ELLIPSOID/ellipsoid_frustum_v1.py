import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R

# Ellipsoid parameters
cex, cey, cez = 10, 20, 30  # Center of the ellipsoid
lx, ly, lz = 4, 5, 6  # Axes of the ellipsoid

# Conical frustum parameters
cfx, cfy, cfz = 7, 8, 9  # Center of the conical frustum
r1 = .5  # Small base radius
alpha = np.pi / 60  # Opening angle

# Calculate the vector joining the centers
vector = np.array([cfx - cex, cfy - cey, cfz - cez])
length = np.linalg.norm(vector)  # Length of the vector

# Create the ellipsoid
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = cex + lx * np.outer(np.cos(u), np.sin(v))
y = cey + ly * np.outer(np.sin(u), np.sin(v))
z = cez + lz * np.outer(np.ones(np.size(u)), np.cos(v))

# Create the conical frustum
theta = np.linspace(0, 2*np.pi, 100)
zz = np.linspace(0, length, 100)
theta, zz = np.meshgrid(theta, zz)
x_frust = cfx + (r1 + zz * np.tan(alpha)) * np.cos(theta)
y_frust = cfy + (r1 + zz * np.tan(alpha)) * np.sin(theta)
z_frust = cfz + zz

# Calculate the rotation matrix
rotation_axis = np.cross([0, 0, 1], vector)
rotation_angle = np.arccos(np.dot([0, 0, 1], vector/length))
rotation_matrix = R.from_rotvec(rotation_angle * rotation_axis)

# Apply the rotation to the conical frustum
frustum_points = np.column_stack([x_frust.ravel(), y_frust.ravel(), z_frust.ravel()])
rotated_frustum_points = rotation_matrix.apply(frustum_points)
translated_frustum_points = rotated_frustum_points
x_frust, y_frust, z_frust = translated_frustum_points.T.reshape(3, x_frust.shape[0], x_frust.shape[1])

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the ellipsoid
ax.plot_surface(x, y, z, color='b')

# Plot the conical frustum
ax.plot_surface(x_frust, y_frust, z_frust, color='r')

plt.show()