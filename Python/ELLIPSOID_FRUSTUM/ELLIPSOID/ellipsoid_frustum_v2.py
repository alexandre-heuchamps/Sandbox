import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_frustum(r1, h, v, alpha):
    # Normalize the vector
    v = np.array(v)
    v = v / np.linalg.norm(v)

    # Create the base of the frustum
    theta = np.linspace(0, 2.*np.pi, 100)
    x = r1 * np.cos(theta)
    y = r1 * np.sin(theta)

    # Calculate the radius of the top of the frustum based on the opening angle
    r2 = r1 + h * np.tan(alpha)

    # Create the top of the frustum
    x2 = r2 * np.cos(theta)
    y2 = r2 * np.sin(theta)

    # Combine the coordinates
    points = np.column_stack((np.append(x, x2), np.append(y, y2), np.append(np.zeros_like(x), h*np.ones_like(x2))))

    # Rotate the points to align with the vector v
    # Calculate the rotation vector and angle
    rot_vector = np.cross([0, 0, 1], v)
    rot_angle = np.arccos(np.dot([0, 0, 1], v))
    rotation = R.from_rotvec(rot_angle * rot_vector)
    points = rotation.apply(points)

    # Create the frustum using ConvexHull
    frustum = ConvexHull(points)

    return frustum

# Test the function
v = [1, 1, 1]
alpha = np.pi / 4  # Opening angle of 45 degrees
frustum = create_frustum(1, 2, v, alpha)

# Plot the frustum
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_trisurf(frustum.points[:,0], frustum.points[:,1], frustum.points[:,2], triangles=frustum.simplices, cmap=plt.cm.Spectral)
plt.show()