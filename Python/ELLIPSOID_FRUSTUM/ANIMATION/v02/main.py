import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from frustum import Frustum





def animate(t, frustum, h, vec, ax):
    frustum.h = h(t)
    frustum.v = [vec[0](t), vec[1](t), vec[2](t)]
    frustum.orient_frustum()
    surf = ax.plot_surface(frustum.x, frustum.y, frustum.z, color = 'r', alpha = .5)

    # If 'surfaces' doesn't exist in the animate function's namespace, create it
    if not hasattr(animate, 'surfaces'):
        animate.surfaces = []

    # Add the new surface to 'surfaces'
    animate.surfaces.append(surf)

    # If there are more than 1 surfaces, remove the oldest one
    if len(animate.surfaces) > 1:
        animate.surfaces.pop(0).remove()





if __name__ == "__main__":
    # ------------------
    # Frustum Parametres
    # ------------------
    r1 = .5
    a = np.pi / 18

    # -----------------------------------------
    # Key values (i.e. generalised "waypoints")
    # -----------------------------------------
    # Time
    ktimes = [0.0, 1.2, 2.6, 3.2, 4.1, 4.8]
    # Target
    cx_t = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    cy_t = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    cz_t = [5.0, 1.0, .5, .5, .5, .5]
    ct = list(zip(cx_t, cy_t, cz_t))
    # Frustum
    cx_f = [0.0] * len(cx_t)
    cy_f = [0.0] * len(cy_t)
    cz_f = [0.0] * len(cz_t)
    cf = list(zip(cx_f, cy_f, cz_f))

    # ----------------------
    # Frustum desired values
    # ----------------------
    # Orientation
    kv = [np.array(vt) - np.array(vf) for vt, vf in zip(ct, cf)]
    kv_norm = [v / np.linalg.norm(v) for v in kv]
    # Height
    norm_kv = [np.linalg.norm(v) for v in kv]

    # ----------------
    # Frustum creation
    # ----------------
    frust = Frustum(r1 = r1, c = cf[0], h = norm_kv[0], a = a)

    # --------------------------------------
    # Create interpolation for target values
    # --------------------------------------
    # Centre coordinates
    times = np.linspace(np.min(ktimes), np.max(ktimes), 50)
    cx_t_interp = sp.interpolate.interp1d(ktimes, cx_t)
    cy_t_interp = sp.interpolate.interp1d(ktimes, cy_t)
    cz_t_interp = sp.interpolate.interp1d(ktimes, cz_t)
    ct_interp = [cx_t_interp, cy_t_interp, cz_t_interp]
    # Frustum heights
    h_interp = sp.interpolate.interp1d(ktimes, norm_kv)
    # Frustum orientations
    kv_norm_x, kv_norm_y, kv_norm_z = zip(*kv_norm)
    kv_norm_x_interp = sp.interpolate.interp1d(ktimes, kv_norm_x)
    kv_norm_y_interp = sp.interpolate.interp1d(ktimes, kv_norm_y)
    kv_norm_z_interp = sp.interpolate.interp1d(ktimes, kv_norm_z)
    kv_norm_interp = [kv_norm_x_interp, kv_norm_y_interp, kv_norm_z_interp]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_aspect('equal')
    ax.set_xlim([-5.0, 5.0])
    ax.set_ylim([-5.0, 5.0])
    ax.set_zlim([-5.0, 5.0])
    ani = animation.FuncAnimation(fig,
                                    animate,
                                    frames = times,
                                    interval = 750,
                                    fargs = (frust, h_interp, kv_norm_interp, ax,),
                                )
    ani.save(f"{__file__.split('.')[0]}_anim.gif", writer = PillowWriter(fps = 15))
    plt.show()