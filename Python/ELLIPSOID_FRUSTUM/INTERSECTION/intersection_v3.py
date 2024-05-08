import numpy as np
import scipy as sp
from scipy.optimize import fsolve, newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_ellispoid(c: tuple[float, float, float],
                    l: tuple[float, float, float],
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X_ell = c[0] + l[0] * np.outer(np.sin(Phi), np.cos(Theta))
    Y_ell = c[1] + l[1] * np.outer(np.sin(Phi), np.sin(Theta))
    Z_ell = c[2] + l[2] * np.outer(np.cos(Phi), np.ones_like(Theta))
    return X_ell, Y_ell, Z_ell





def get_conical_frustum(c: tuple[float, float, float],
                        r1: float,
                        alpha: float,
                        z: np.ndarray,
                    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    Theta, Z = np.meshgrid(theta, z)
    R = r1 + Z * np.tan(alpha)
    X_fru = c[0] + R * np.cos(Theta)
    Y_fru = c[1] + R * np.sin(Theta)
    Z_fru = c[2] + Z
    return X_fru, Y_fru, Z_fru





# Define the equations for the ellipsoid and the conical frustum
def ellipsoid(theta, phi, ce, l):
    return np.array(
                [ce[0] + l[0]*np.cos(theta)*np.cos(phi),
                    ce[1] + l[1]*np.sin(theta)*np.cos(phi),
                    ce[2] + l[2]*np.sin(phi)]
            )





def frustum(theta, z, cf, r1, a):
    return np.array(
                [cf[0] + (r1 + z * np.tan(a)) * np.cos(theta),
                    cf[1] + (r1 + z * np.tan(a)) * np.sin(theta),
                    cf[2] + z]
            )





# Define the function for which we want to find the root
def func(x, theta, phi, z, ce, cf, l, r1, div):
    return ellipsoid(theta, phi, ce, l) - frustum(theta, z, cf, r1, div)





# Define the Jacobian matrix of the function
def jacobian(x, theta, phi, z, ce, cf, l, r1, div):
    return np.array(
        [
            [-(l[0] * np.cos(phi) - r1 - z * np.tan(div)) * np.sin(theta), -l[0] * np.cos(theta) * np.sin(phi), -np.tan(div) * np.cos(theta)],
            [-(l[1] * np.cos(phi) - r1 - z * np.tan(div)) * np.cos(theta), -l[1] * np.cos(theta) * np.sin(phi), -np.tan(div) * np.sin(theta)],
            [0.0, l[2] * np.cos(phi), -1],
        ]
    )





# Create mesh points
num_points = 20
theta = np.linspace(0.0, 2*np.pi, num_points)
phi = np.linspace(0.0, np.pi, num_points)
Theta, Phi = np.meshgrid(theta, phi)


# Ellipsoid
ce = [0.0, 0.0, 1.7]
l = [1.5, 1.1, 0.75]

# Conical frustum
cf = [0.0, 0.0, 0.0]
h = np.linalg.norm(np.array(cf) - np.array(ce))
z = np.linspace(cf[-1], h, num_points)
r1 = 0.15
div = np.pi / 9

# Initial guess
# x0 = np.array([0.0, 0.0, ce[-1]])

# Iterate over theta, phi, and z values
sol = []
for it, t in enumerate(theta):
    for ip, p in enumerate(phi):
        for iz, z_val in enumerate(z):
            try:
                root = fsolve(func, [t, p, z_val], args=(t, p, z_val, ce, cf, l, r1, div), fprime=jacobian)
                sol.append(root)
            except RuntimeError:
                continue
sol = np.array(sol)
print(sol)

# Create a 3D plot
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')

# Plot the volumes
xell, yell, zell = get_ellispoid(ce, l)
ax.plot_surface(xell, yell, zell, color = 'r', alpha = 0.005)

xfru, yfru, zfru = get_conical_frustum(cf, r1, div, z)
ax.plot_surface(xfru, yfru, zfru, color = 'b', alpha = 0.35)

# Plot the intersections
# ax.scatter(root[0], root[1], root[2], color = 'g')
ax.scatter(sol[:, 0], sol[:, 1], sol[:, 2], color = 'g', s = 1.5)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()

# xell, yell, zell = get_ellispoid(ce, l)
# xfru, yfru, zfru = get_conical_frustum(cf, r1, div, h)

# # Flatten the arrays and stack them along the second axis
# pts_ell = np.stack((xell.ravel(), yell.ravel(), zell.ravel()), axis=-1)
# pts_fru = np.stack((xfru.ravel(), yfru.ravel(), zfru.ravel()), axis=-1)

# # Create a k-d tree for the frustum
# tree = sp.spatial.cKDTree(pts_fru)

# # For each point in the ellipsoid, find the distance to the nearest point in the frustum
# distances, _ = tree.query(pts_ell)

# # If the distance is below a certain threshold, the point can be considered as belonging to the other volume
# threshold = 1e-6  # This value depends on the precision of your data
# belongs_to_other = distances < threshold
# print(np.where(belongs_to_other == True))