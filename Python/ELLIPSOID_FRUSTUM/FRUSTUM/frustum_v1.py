import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# def frustum_plane1(x, y, z, A1, B1, C1, D1):
#     return A1*x + B1*y + C1*z + D1

# def frustum_plane2(x, y, z, A2, B2, C2, D2):
#     return A2*x + B2*y + C2*z + D2

""" The equation 
    A1x + B1y + C1*z + D1 = 0
is the general form of the equation of a plane in three-dimensional space.

Here's how to interpret the coefficients:
    A1, B1, and C1
are the coefficients of x, y, and z, respectively.
They determine the orientation of the plane in space.
In fact, the vector n = [A1, B1, C1] is a normal vector to the plane, meaning it is perpendicular to the plane.
    D1
is the constant term.
It affects the position of the plane in relation to the origin of the coordinate system.
If D1 is positive, the plane is in the direction of the normal vector from the origin, and if D1 is negative, it is in the opposite direction.
So, for a frustum (a portion of a cone) and this equation is given, it represents one of the planes that cut the cone to form the frustum. """





def draw_ellipsoid(dims, c):
    x = dims[0] * np.outer(np.cos(u), np.sin(v)) + c[0]
    y = dims[1] * np.outer(np.sin(u), np.sin(v)) + c[1]
    z = dims[2] * np.outer(np.ones(np.size(u)), np.cos(v)) + c[2]
    return x, y, z




def draw_frustum(P1, P2, R1, alpha):
    height = np.linalg.norm(np.array(P2) - np.array(P1))
    v = np.linspace(0, height, nangs)
    r = lambda z: R1 + z * np.tan(alpha)
    x = np.outer(r(v), np.cos(u)) + P1[0]
    y = np.outer(r(v), np.sin(u)) + P1[1]
    z = np.outer(v, np.ones_like(u)) + P1[2]
    direction = np.array(P2) - np.array(P1)
    direction /= np.linalg.norm(direction)
    rotation_matrix = sp.spatial.transform.Rotation.from_rotvec(np.cross([0, 0, 1], direction)).as_matrix()
    coords = np.dot(rotation_matrix, np.array([x.flatten(), y.flatten(), z.flatten()]))
    coords += np.array(P1).reshape(-1, 1)
    return coords[0, :].reshape(x.shape), coords[1, :].reshape(y.shape), coords[2, :].reshape(z.shape)





# Angular mesh
nangs = 100
u = np.linspace(0, 2 * np.pi, nangs)
v = np.linspace(0, np.pi, nangs)

# Ellipsoid
lell = [2.5, 2.0, 1.5]
cell = [40.0, 0.0, 100.0]
xe, ye, ze = draw_ellipsoid(lell, cell)

# Conical frustum
cf = [0.0, 0.0, 0.0]
R1 = 1e-3
alpha = 1e-2
xf, yf, zf = draw_frustum(cf, cell, R1, alpha)

# Create a new figure
fig = plt.figure()

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces
ax.plot_surface(xe, ye, ze, color='r', alpha = .5)
ax.plot_surface(xf, yf, zf, color='b', alpha = .3)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()



from scipy.optimize import fsolve

# Define the implicit equations for the conical frustum and the ellipsoid
def conical_frustum(x, y, z):
    # Check if the point is inside the frustum
    if np.min((x - xf)**2 + (y - yf)**2 + (z - zf)**2) <= 0:
        return -1e6  # Large negative number
    else:
        return 1e6  # Large positive number

def ellipsoid(x, y, z, dims):
    return ((x - xe) / dims[0])**2 + ((y - ye) / dims[1])**2 + ((z - ze) / dims[2])**2 - 1

# Define the system of equations
def system(t, o, d, dims):
    x, y, z = o + t * d
    return [conical_frustum(x, y, z), ellipsoid(x, y, z, dims)]

# Generate 100 rays within the frustum
rays = []
for i in range(100):
    # The origin of each ray is the origin of the frustum
    origin = cf
    # The direction of each ray is towards the center of the ellipsoid
    direction = np.array(cell) - np.array(origin)
    direction /= np.linalg.norm(direction)  # Normalize the direction
    rays.append((origin, direction))  # Each ray is defined by an origin and a direction

# Find the intersection points of the rays with the conical frustum and the ellipsoid
intersection_points = []
for o, d in rays:
    t_value = fsolve(system, 0, args=(o, d, lell))
    # Only keep the value of t that is positive (since the ray starts at the origin of the frustum)
    if t_value[0] > 0:
        intersection_points.append(o + t_value[0] * d)

print(intersection_points)