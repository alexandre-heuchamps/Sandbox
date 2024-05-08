""" import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for the conical frustum
R1 = 2.0  # Base radius
R2 = 1.0  # Top radius
h = 3.0   # Height

# Define parameters for the ellipsoid
x0, y0, z0 = 0.0, 0.0, 0.0
lx, ly, lz = 1.0, 2.0, 3.0

# Create a grid of points (adjust resolution as needed)
n_points = 20
x_vals = np.linspace(-R1, R1, n_points)
y_vals = np.linspace(-R1, R1, n_points)
z_vals = np.linspace(0, h, n_points)

# Evaluate the ellipsoid equation at all points
X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals, indexing='ij')
ellipsoid_vals = ((X - x0) / lx)**2 + ((Y - y0) / ly)**2 + ((Z - z0) / lz)**2

# Find points within the ellipsoid
intersection_indices = np.where(ellipsoid_vals <= 1)
intersection_points = np.column_stack(
                            (
                                X[intersection_indices],
                                Y[intersection_indices],
                                Z[intersection_indices]
                            )
                        )

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(intersection_points[:, 0],
            intersection_points[:, 1],
            intersection_points[:, 2],
            color='red',
            s=10,
            label='Intersection Points')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersection of Conical Frustum and Ellipsoid')

# Show the legend
ax.legend()

# Show the plot
plt.show() """










import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def get_ellispoid(c: tuple[float, float, float],
                    l: tuple[float, float, float],
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X_ell = c[0] + l[0] * np.outer(np.sin(Phi), np.cos(Theta))
    Y_ell = c[1] + l[1] * np.outer(np.sin(Phi), np.sin(Theta))
    Z_ell = c[2] + l[2] * np.outer(np.cos(Phi), np.ones_like(Theta))
    return X_ell, Y_ell, Z_ell





def get_normal_ellipsoid(X_ell, Y_ell, Z_ell, c, l):
    normals = np.vstack([2*(X_ell-c[0])/l[0]**2, 2*(Y_ell-c[1])/l[1]**2, 2*(Z_ell-c[2])/l[2]**2])
    norms = np.linalg.norm(normals, axis=0)
    normals = normals / norms
    return normals





def get_conical_frustum(c: tuple[float, float, float],
                        r1: float,
                        alpha: float,
                        h: float,
                        n_points: int = 20,
                    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z = np.linspace(0, h, n_points)
    Theta, Z = np.meshgrid(theta, z)
    R = r1 + Z * np.tan(alpha)
    X_fru = c[0] + R * np.cos(Theta)
    Y_fru = c[1] + R * np.sin(Theta)
    Z_fru = c[2] + Z
    return X_fru, Y_fru, Z_fru





def get_inter_pts(X1, Y1, Z1, X2, Y2, Z2, tol = 1e-3):
    points1 = np.vstack([X1.ravel(), Y1.ravel(), Z1.ravel()]).T
    points2 = np.vstack([X2.ravel(), Y2.ravel(), Z2.ravel()]).T

    # intersection_points = []
    # for point1 in points1:
    #     distances = np.sum((points2 - point1)**2, axis=1)
    #     if np.min(distances) < tol:
    #         intersection_points.append(point1)

    # return np.array(intersection_points)
    # Calculate the Euclidean distance between all pairs of points
    distances = sp.spatial.distance.cdist(points1, points2)
    mask = np.any(distances < tol, axis = 1)
    intersection_points = points1[mask]

    return intersection_points





# Create a grid of points
n_points = 20
theta = np.linspace(0, 2 * np.pi, n_points)
phi = np.linspace(0, np.pi, n_points)
Theta, Phi = np.meshgrid(theta, phi)

# Define parameters for the ellipsoid
ce = (0.0, 0.0, 0.0)
l = (1.0, 2.0, 3.0)

# Compute coordinates for the ellipsoid
X_ell, Y_ell, Z_ell = get_ellispoid(ce, l)
normals = get_normal_ellipsoid(X_ell, Y_ell, Z_ell, ce, l)

# Define parameters for the conical frustum
cf = (0.0, 0.0, -5.0)
h = np.linalg.norm(np.array(cf) - np.array(ce))
r1 = 0.15
alpha = np.pi / 60

# Compute coordinates for the conical frustum
X_fru, Y_fru, Z_fru = get_conical_frustum(cf, r1, alpha, h)

# Create a 3D plot
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')

# Plot the volumes
ax.plot_surface(X_ell, Y_ell, Z_ell, color = 'r', alpha = 0.5)
ax.plot_surface(X_fru, Y_fru, Z_fru, color = 'b', alpha = 0.3)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()