import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_frustum(r1, c, h, v, alpha, num_points = 100):
    # Normalize the vector
    v = np.array(v)
    v = v / np.linalg.norm(v)

    # Create the base of the frustum
    theta = np.linspace(0.0, 2.0 * np.pi, num_points)
    x = c[0] + r1 * np.cos(theta)
    y = c[1] + r1 * np.sin(theta)
    z = c[2] + np.zeros_like(x)

    # Calculate the radius of the top of the frustum based on the opening angle
    r2 = r1 + h * np.tan(alpha)

    # Create the top of the frustum
    x2 = r2 * np.cos(theta)
    y2 = r2 * np.sin(theta)
    z2 = h * np.ones_like(x2)

    # Combine the coordinates
    x = np.append(x, x2)
    y = np.append(y, y2)
    z = np.append(z, z2)

    # Rotate the points to align with the vector v
    # Calculate the rotation vector and angle
    zaxis = [0.0, 0.0, 1]
    rot_vector = np.cross(zaxis, v)
    rot_angle = np.arccos(np.dot(zaxis, v))
    rotation = R.from_rotvec(rot_angle * rot_vector)
    points = rotation.apply(np.column_stack((x, y, z)))

    # Split the points back into x, y, z
    x, y, z = points[:, 0], points[:, 1], points[:, 2]

    # Reshape the arrays into 2D arrays for plot_surface
    x = x.reshape((2, num_points))
    y = y.reshape((2, num_points))
    z = z.reshape((2, num_points))

    return x, y, z

# Test the function
v = [1, 1, 1]
c = [2.3, 6.5, 5.0]
alpha = np.pi / 30
x, y, z = create_frustum(1, c, 25.0, v, alpha)

# Plot the frustum
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(x, y, z)
plt.show()