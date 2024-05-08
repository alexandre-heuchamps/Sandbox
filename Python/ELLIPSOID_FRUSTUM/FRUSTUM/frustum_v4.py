import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_frustum(r1, c, h, alpha, num_points = 100):
    # Create the base of the frustum
    theta = np.linspace(0.0, 2.0 * np.pi, num_points)
    x = c[0] + r1 * np.cos(theta)
    y = c[1] + r1 * np.sin(theta)
    z = c[2] + np.zeros_like(x)

    # Calculate the radius of the top of the frustum based on the opening angle
    r2 = r1 + h * np.tan(alpha)

    # Create the top of the frustum
    x2 = c[0] + r2 * np.cos(theta)
    y2 = c[1] + r2 * np.sin(theta)
    z2 = c[2] + h * np.ones_like(x2)

    # Combine the coordinates
    x = np.append(x, x2)
    y = np.append(y, y2)
    z = np.append(z, z2)

    # Reshape the arrays into 2D arrays for plot_surface
    x = x.reshape((2, num_points))
    y = y.reshape((2, num_points))
    z = z.reshape((2, num_points))

    return x, y, z





def orient_frustum(x, y, z, c, v, num_points = 100):
    # Normalize the vector
    v = np.array(v)
    v = v / np.linalg.norm(v)

    # Rotate the points to align with the vector v
    # Calculate the rotation vector and angle
    zaxis = [0.0, 0.0, 1]
    rot_vector = np.cross(zaxis, v)
    rot_angle = np.arccos(np.dot(zaxis, v))
    rotation = R.from_rotvec(rot_angle * rot_vector)
    x, y, z = np.ravel(x) - c[0], np.ravel(y) - c[1], np.ravel(z) - c[2]
    points = rotation.apply(np.column_stack((x, y, z)))

    # Split the points back into x, y, z
    x, y, z = points[:, 0] + c[0], points[:, 1] + c[1], points[:, 2] + c[1]

    # Reshape the arrays into 2D arrays for plot_surface
    x = x.reshape((2, num_points))
    y = y.reshape((2, num_points))
    z = z.reshape((2, num_points))

    return x, y, z






# Test the function
c = [2.3, 6.5, 5.0]
r1 = 0.5
h = 12.5
alpha = np.pi / 30
npts = 500
x, y, z = create_frustum(r1 = r1, c = c, h = h, alpha = alpha, num_points = npts)

# Plot the frustum
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(x, y, z, color = 'b')

# Vector for frustum orientation
v = [1, 1, 1]
x, y, z = orient_frustum(x = x, y = y, z = z, c = c, v = v, num_points = npts)
ax.plot_surface(x, y, z, color = 'r')

plt.show()