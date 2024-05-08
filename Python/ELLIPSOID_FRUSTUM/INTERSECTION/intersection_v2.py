""" import numpy as np
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





def get_conical_frustum(c: tuple[float, float, float],
                        r1: float,
                        alpha: float,
                        h: float,
                        npt_z: int = 200,
                    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z = np.linspace(0, h, npt_z)
    Theta, Z = np.meshgrid(theta, z)
    R = r1 + Z * np.tan(alpha)
    X_fru = c[0] + R * np.cos(Theta)
    Y_fru = c[1] + R * np.sin(Theta)
    Z_fru = c[2] + Z
    return X_fru, Y_fru, Z_fru





def equations(vars, ce, d, cf, r1, div):
    x, y, z = vars

    # Equation for the ellipsoid
    eq1 = ((x - ce[0]) / d[0])**2 + ((y - ce[1]) / d[1])**2 + ((z - ce[2]) / d[2])**2 - 1

    # Equation for the frustum
    r = np.sqrt((x - cf[0])**2 + (y - cf[1])**2)
    eq2 = r - (r1 + (z + cf[2]) * np.tan(div))

    # Dummy equation
    eq3 = 0.0

    return [eq1, eq2, eq3]





# Create a grid of points
npt_t = 35
npt_p = 100
theta = np.linspace(0, 2 * np.pi, npt_t)
phi = np.linspace(0, np.pi, npt_p)
Theta, Phi = np.meshgrid(theta, phi)

# Ellipsoid
ce = [0.0, 0.0, 0.0]
dims = [1.5, 1.1, 0.45]
X_ell, Y_ell, Z_ell = get_ellispoid(ce, dims)

# Conical frustum
cf = [0.0, 0.0, -1.5]
h = np.linalg.norm(np.array(cf) - np.array(ce))
r1 = 0.15
alpha = np.pi / 18
X_fru, Y_fru, Z_fru = get_conical_frustum(cf, r1, alpha, h)

# Stack the coordinates to create 2D arrays
Xell, Yell, Zell = X_ell.flatten(), Y_ell.flatten(), Z_ell.flatten()
Xf, Yf, Zf = X_fru.flatten(), Y_fru.flatten(), Z_fru.flatten()
ellipsoid_points = np.column_stack((Xell, Yell, Zell))
frustum_points = np.column_stack((Xf, Yf, Zf))

# Build a KDTree for the frustum points
tree = sp.spatial.cKDTree(frustum_points)

# # Query the tree for the nearest frustum point to each ellipsoid point
# distances, indices = tree.query(ellipsoid_points)

# # Find the ellipsoid points where the distance to the nearest frustum point is below a small threshold
# tol = 1e-3
# intersection_points = ellipsoid_points[distances < tol]
# print(intersection_points)
# Find the ellipsoid points where the distance to the nearest frustum point is below a small threshold
tol = 1e-3
intersection_indices = tree.query_ball_point(ellipsoid_points, tol)

# Flatten the list of lists to get the indices of the intersection points
intersection_indices = [index for sublist in intersection_indices for index in sublist]

# Get the unique indices (since some points might be repeated)
# intersection_indices = np.unique(intersection_indices)

# Use these indices to get the intersection points
intersection_points = ellipsoid_points[np.array(intersection_indices).astype(int)]


# Create a 3D plot
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')

# Plot the volumes
ax.plot_surface(X_ell, Y_ell, Z_ell, color = 'r', alpha = 0.005)
ax.plot_surface(X_fru, Y_fru, Z_fru, color = 'b', alpha = 0.3)
print(intersection_points)
# ax.scatter(intersection_points[0, :], intersection_points[1, :], intersection_points[2, :], color = 'g')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()



# # Initial guess for the roots
# x0, y0, z0 = ce

# # Use fsolve to solve the system of equations
# x, y, z = sp.optimize.fsolve(equations, (x0, y0, z0), args = (ce, dims, cf, r1, div))

# print(f"The solutions are x={x}, y={y}, z={z}") """

import numpy as np
from scipy.optimize import newton, fsolve

# Define the equations for the ellipsoid and the conical frustum
def ellipsoid(theta, phi, ce, l):
    return np.array([ce[0] + l[0]*np.cos(theta)*np.cos(phi), ce[1] + l[1]*np.sin(theta)*np.cos(phi), ce[2] + l[2]*np.sin(phi)])

def frustum(theta, z, cf, r1, a):
    return np.array([cf[0] + (r1 + z*np.tan(a))*np.cos(theta), cf[1] + (r1 + z*np.tan(a))*np.sin(theta), cf[2] + z])

# Define the function for which we want to find the root
def func(x, theta, phi, z, ce, cf, l, r1, div):
    return ellipsoid(theta, phi, ce, l) - frustum(theta, z, cf, r1, div)

# Define the Jacobian matrix of the function
def jacobian(x, theta, phi, z, ce, cf, l, r1, div):
    return np.array([[-l[0]*np.sin(theta)*np.cos(phi), -l[0]*np.cos(theta)*np.sin(phi), 0],
                     [l[1]*np.cos(theta)*np.cos(phi), -l[1]*np.sin(theta)*np.sin(phi), 0],
                     [0, l[2]*np.cos(phi), -r1*np.tan(div) - z*(np.tan(div))**2]])





num_points = 10
theta = np.linspace(0, 2*np.pi, num_points)
phi = np.linspace(0, np.pi, num_points)


# Ellipsoid
ce = [0.0, 0.0, 0.0]
l = [1.5, 1.1, 0.45]

# Conical frustum
cf = [0.0, 0.0, -1.5]
h = np.linalg.norm(np.array(cf) - np.array(ce))
r1 = 0.15
div = np.pi / 18

# Initial guess
z = np.linspace(-2.0, h, num_points)
x0 = np.array([0.0, 0.0, np.min(np.array([ce[-1], cf[-1]]))])

# Iterate over theta, phi, and z values
sol = []
for t in theta:
    for p in phi:
        for z_val in z:
            try:
                # Use the Newton-Raphson method to find the root
                # root = newton(func, x0, fprime=jacobian, args=(t, p, z_val, ce, cf, l, r1, div))
                root = fsolve(func, x0, args=(t, p, z_val, ce, cf, l, r1, div))
                sol.append(root)
            except RuntimeError:
                # If the method fails to converge, skip this set of parameters
                continue
print(sol)