import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter




# def draw_ellipsoid(t, dims, ax):
#     rotation = slerp_e(t)
#     print(rotation.as_euler('zxy'))
#     c = [cxe_interp(t), cye_interp(t), cze_interp(t)]
#     x = dims[0] * np.outer(np.cos(u), np.sin(v)) + c[0]
#     y = dims[1] * np.outer(np.sin(u), np.sin(v)) + c[1]
#     z = dims[2] * np.outer(np.ones(np.size(u)), np.cos(v)) + c[2]
#     rotated = rotation.apply(np.column_stack([x.ravel(), y.ravel(), z.ravel()]))
#     x = rotated[:, 0].reshape(x.shape)
#     y = rotated[:, 1].reshape(y.shape)
#     z = rotated[:, 2].reshape(z.shape)
#     ax.cla()
#     ax.set_xlim([-2 * dims[0], 2 * dims[0]])
#     ax.set_ylim([-2 * dims[1], 2 * dims[1]])
#     ax.set_zlim([-2 * dims[2], 20 * dims[2]])
#     ax.plot_surface(x, y, z, color = 'b', alpha = .75)
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')





# # Define the ellipse parameters
# lx = 2.5
# ly = 1.5
# lz = .5
# dims = [lx, ly, lz]

# cxe = 0.0
# cye = 0.0
# cze = 0.0
# c = [cxe, cye, cze]

# # Create the mesh of the angles
# nangs = 100
# u = np.linspace(start = 0, stop = 2 * np.pi, num = nangs)
# v = np.linspace(start = 0.0, stop = np.pi, num = nangs)

# # Define the key times, center positions, angles and times
# ktimes = [0.0, 1.2, 2.6, 3.2, 4.1, 4.8]
# cxe = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# cye = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# cze = [0.0, 1.0, 2.0, 2.0, 2.0, 2.0]
# kte = np.radians([0.0, 23.5, 48.79, 67.2, 80.0, 90.0])
# kpe = np.radians([0.0, 0.0, 0.0, 10.0, 17.5, 17.5])
# krot_e = sp.spatial.transform.Rotation.from_euler('zyx',
#                                                     np.column_stack(
#                                                         [kte,
#                                                         kpe,
#                                                         np.zeros_like(kte)
#                                                         ]
#                                                     )
#                                                 )

# # Define the times at which to compute the orientations and center positions
# times = np.linspace(np.min(ktimes), np.max(ktimes), 50)

# # Create the Slerp object
# slerp_e = sp.spatial.transform.Slerp(ktimes, krot_e)

# # Create different interpolate ellipsoid center positions
# cxe_interp = sp.interpolate.interp1d(ktimes, cxe)
# cye_interp = sp.interpolate.interp1d(ktimes, cye)
# cze_interp = sp.interpolate.interp1d(ktimes, cze)

# # Create a new figure and axis for the plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')

# # Create the animation
# ani = animation.FuncAnimation(fig, draw_ellipsoid, frames=times, fargs=(dims, ax,))
# # ani.save("ellipsoid_animation.gif", writer = PillowWriter(fps = 30))

# # Display the animation
# plt.show()



def draw_ellipsoid(t, dims, ax):
    rotation_e = slerp_e(t)
    theta_e, phi_e, _ = rotation_e.as_euler('ZYX', degrees = True)
    print(f"Time: {t}, Theta: {theta_e}, Phi: {phi_e}")
    c_e = [cxe_interp(t), cye_interp(t), cze_interp(t)]
    x_e = dims[0] * np.outer(np.cos(u), np.sin(v)) + c_e[0]
    y_e = dims[1] * np.outer(np.sin(u), np.sin(v)) + c_e[1]
    z_e = dims[2] * np.outer(np.ones(np.size(u)), np.cos(v)) + c_e[2]
    # rotated_e = rotation_e.apply(np.column_stack([x_e.ravel(), y_e.ravel(), z_e.ravel()]))
    rotated_e = rotation_e.apply(np.column_stack([np.ravel(x_e), np.ravel(y_e), np.ravel(z_e)]))
    x_e = rotated_e[:, 0].reshape(x_e.shape)
    y_e = rotated_e[:, 1].reshape(y_e.shape)
    z_e = rotated_e[:, 2].reshape(z_e.shape)
    ax.cla()
    ax.set_xlim([-2 * dims[0], 2 * dims[0]])
    ax.set_ylim([-2 * dims[1], 2 * dims[1]])
    ax.set_zlim([-2 * dims[2], 2 * dims[2]])
    ax.plot_surface(x_e, y_e, z_e, color = 'b', alpha = .75)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')



# Ellipsoid parameters
lx = 2.5
ly = 1.5
lz = .5
dims = [lx, ly, lz]

# Angles unsed to mesh the ellipsoid
nangs = 100
u = np.linspace(start = 0, stop = 2 * np.pi, num = nangs)
v = np.linspace(start = 0.0, stop = np.pi, num = nangs)

# Ellipsoid center coordinates and orientations at specified times
ktimes = [0.0, 1.2, 2.6, 3.2, 4.1, 4.8]
cx_e = [0.0, 1.1, 1.2, 1.3, 1.4, 1.5]
cy_e = [0.0, 1.1, 1.2, 1.3, 1.4, 1.5]
cz_e = [0.0, 1.0, .5, .5, .5, .5]
ce = zip(cx_e, cy_e, cz_e)
kt_e = np.radians([0.0, 23.5, 48.79, 67.2, 80.0, 90.0])
kp_e = np.radians([0.0, 0.0, 0.0, 10.0, 17.5, 17.5])

# Conical frustum parametres
cx_f = [0.0] * len(ktimes)
cy_f = [0.0] * len(ktimes)
cz_f = [0.0] * len(ktimes)
cf = zip(cx_f, cy_f, cz_f)
r1 = .5
alpha = np.pi / 30

# Lengths and key relative ellipsoid-HEL orientation
kv = [np.array(ve) - np.array(vf) for ve, vf in zip(ce, cf)]

# Convert spherical coordinates to Cartesian coordinates
krot_e = sp.spatial.transform.Rotation.from_euler('zyz',
                np.column_stack(
                    [
                        kt_e,
                        -kp_e,
                        np.zeros_like(kt_e)
                    ]
                )
            )

# Concatenate the rotations into a single Rotation instance
krot_e = sp.spatial.transform.Rotation.concatenate(krot_e)

# Create rotation interpolation
slerp_e = sp.spatial.transform.Slerp(ktimes, krot_e)

# Create interpolation for ellipsoid center coordinates
times = np.linspace(np.min(ktimes), np.max(ktimes), 50)
cxe_interp = sp.interpolate.interp1d(ktimes, cx_e)
cye_interp = sp.interpolate.interp1d(ktimes, cy_e)
cze_interp = sp.interpolate.interp1d(ktimes, cz_e)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ani = animation.FuncAnimation(fig, draw_ellipsoid, frames=times, fargs=(dims, ax,))
# ani.save("ellipsoid_animation.gif", writer = PillowWriter(fps = 30))
plt.show()