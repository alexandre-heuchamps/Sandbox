import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ellipsoid
xe, ye, ze = 0.0, 0.0, 0.0
a, b, c = 1.5, 1.1, 0.45

# Conical frustum
xf, yf, zf = 0.0, 0.0, -1.5
h = 1.5
R = 0.45
alpha = np.pi / 18
tanalpha = np.tan(alpha)

angles = np.linspace(0.0, 2 * np.pi, 400)
upper = []
lower = []

for phi in angles:
   # Set up coefficients in quadratic equation
   cosphi, sinphi = np.cos(phi), np.sin(phi)
   x1, x2 = xf - xe + (R + zf * tanalpha) * cosphi, tanalpha * cosphi
   y1, y2 = yf - ye + (R + zf * tanalpha) * sinphi, tanalpha * sinphi
   z1, z2 = ze, 1
   A = (x2 / a) ** 2 + (y2 / b) ** 2 + (z2 / c) ** 2
   B = -2 * (x1 * x2 / a ** 2 + y1 * y2 / b ** 2 + z1 * z2 / c ** 2)
   C = (x1 / a) ** 2 + (y1 / a) ** 2 + (z1 / c) ** 2 - 1
   discriminant = B**2 - 4 * A * C
   if discriminant >= 0:
      root1 = (-B - np.sqrt(discriminant)) / (2 * A)
      root2 = -B / A - root1
      if zf <= root1 <= zf + h: lower.append([xf + (R + (root1 - zf) * tanalpha) * cosphi, yf + (R + (root1 - zf) * tanalpha) * sinphi, root1])
      if zf <= root2 <= zf + h: upper.append([xf + (R + (root2 - zf) * tanalpha) * cosphi, yf + (R + (root2 - zf) * tanalpha) * sinphi, root2])

lower = np.array(lower)
upper = np.array(upper)

################################################################################################

# Create a 3D plot

def get_ellipsoid(c, l):
    num_points = 20
    th = np.linspace(0.0, 2 * np.pi, num_points)
    ph = np.linspace(0.0, np.pi, num_points)
    Theta, Phi = np.meshgrid(th, ph)

    X_ell = c[0] + l[0] * np.outer(np.sin(Phi), np.cos(Theta))
    Y_ell = c[1] + l[1] * np.outer(np.sin(Phi), np.sin(Theta))
    Z_ell = c[2] + l[2] * np.outer(np.cos(Phi), np.ones_like(Theta))
    return X_ell, Y_ell, Z_ell

def get_frustum( c, r1, alpha, h ):
    num_points = 20
    th = np.linspace(0.0, 2 * np.pi, num_points)
    z = np.linspace(0, h, num_points)
    Theta, Z = np.meshgrid(th, z)
    R = r1 + Z * np.tan(alpha)
    X_fru = c[0] + R * np.cos(Theta)
    Y_fru = c[1] + R * np.sin(Theta)
    Z_fru = c[2] + Z
    return X_fru, Y_fru, Z_fru




fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection = '3d')

# Plot the volumes
xell, yell, zell = get_ellipsoid([xe, ye, ze], [a, b, c])
ax.plot_surface(xell, yell, zell, color = 'r', alpha = 0.005)

xfru, yfru, zfru = get_frustum([xf, yf, zf], R, alpha, h)
ax.plot_surface(xfru, yfru, zfru, color = 'b', alpha = 0.35)

# Plot the intersections
if lower.size > 0: ax.plot(lower[:, 0], lower[:, 1], lower[:, 2], color = 'g')
if upper.size > 0: ax.plot(upper[:, 0], upper[:, 1], upper[:, 2], color = 'g')

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.savefig("intersection_analytic.svg")

plt.show()