import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from frustum import Frustum
from ellipsoid import Ellipsoid





def animate(t, ell, slerp_e, ce_interp, frustum, h_f, vec_f, ax):
    ax.cla()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_aspect('equal')
    ax.set_xlim([-5.0, 5.0])
    ax.set_ylim([-5.0, 5.0])
    ax.set_zlim([-5.0, 5.0])
    ell.c = [ce_interp[0](t), ce_interp[1](t), ce_interp[2](t)]
    rotation_e = slerp_e(t)
    theta, phi = rotation_e.as_euler('ZYX')[0], rotation_e.as_euler('ZYX')[2]
    ell.rotate(-theta, phi)
    xmesh_e, ymesh_e, zmesh_e = ell.get_rotated_mesh()
    surf_e = ax.plot_surface(xmesh_e, ymesh_e, zmesh_e, color = 'b', alpha = .5)

    frustum.h = h_f(t)
    frustum.v = [vec_f[0](t), vec_f[1](t), vec_f[2](t)]
    frustum.orient_frustum()
    surf_f = ax.plot_surface(frustum.x, frustum.y, frustum.z, color = 'r', alpha = .5)





if __name__ == "__main__":
    # --------------------
    # Ellipsoid Parametres
    # --------------------
    lx = 2.5
    ly = 1.75
    lz = 1.0
    l = [lx, ly, lz]

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
    # Ellipsoid
    # cx_e = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    cx_e = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    cy_e = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    cz_e = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
    ce = list(zip(cx_e, cy_e, cz_e))
    # ktheta_e = np.linspace(0.0, 8.0 * np.pi, num = len(ktimes))
    ktheta_e = np.radians([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # kphi_e = np.radians([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    kphi_e = np.radians([0.0, 23.5, 48.79, 67.2, 80.0, 90.0])
    # kphi_e = np.linspace(0.0, 8.0 * np.pi, num = len(ktimes))
    kquat_e = np.column_stack([
        np.cos(ktheta_e / 2) * np.cos(kphi_e / 2),
        - np.sin(ktheta_e / 2) * np.cos(kphi_e / 2),
        np.sin(ktheta_e / 2) * np.sin(kphi_e / 2),
        - np.cos(ktheta_e / 2) * np.sin(kphi_e / 2)
    ])
    # Frustum
    cx_f = [0.0] * len(cx_e)
    cy_f = [0.0] * len(cy_e)
    cz_f = [0.0] * len(cz_e)
    cf = list(zip(cx_f, cy_f, cz_f))

    # ----------------------
    # Frustum desired values
    # ----------------------
    # Orientation
    kv = [np.array(vt) - np.array(vf) for vt, vf in zip(ce, cf)]
    kv_norm = [v / np.linalg.norm(v) for v in kv]
    # Height
    norm_kv = [np.linalg.norm(v) for v in kv]

    # ---------------
    # Bodies creation
    # ---------------
    # Ellipsoid
    ell = Ellipsoid(c = ce[0], lx = lx, ly = ly, lz = lz, U = np.eye(3))
    ell.rotate(ktheta_e[0], kphi_e[0])
    # Frustum
    frust = Frustum(r1 = r1, c = cf[0], h = norm_kv[0], a = a)

    # ------------------------------------------------------
    # Convert spherical coordinates to Cartesian coordinates
    # ------------------------------------------------------
    # Ellipsoid rotations
    krot_e = sp.spatial.transform.Rotation.from_quat(kquat_e)
    krot_e = sp.spatial.transform.Rotation.concatenate(krot_e)

    # ------------------------------
    # Create rotation interpolations
    # ------------------------------
    # Ellipsoid
    slerp_e = sp.spatial.transform.Slerp(ktimes, krot_e)

    # --------------------------------------
    # Create interpolation for target values
    # --------------------------------------
    # Centre coordinates
    times = np.linspace(np.min(ktimes), np.max(ktimes), 50)
    cx_e_interp = sp.interpolate.interp1d(ktimes, cx_e)
    cy_e_interp = sp.interpolate.interp1d(ktimes, cy_e)
    cz_e_interp = sp.interpolate.interp1d(ktimes, cz_e)
    ce_interp = [cx_e_interp, cy_e_interp, cz_e_interp]
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
    ani = animation.FuncAnimation(fig,
                                    animate,
                                    frames = times,
                                    interval = 200,
                                    fargs = (ell, slerp_e, ce_interp, frust, h_interp, kv_norm_interp, ax,),
                                )
    # ani.save(f"{__file__.split('.')[0]}_anim_phi.gif", writer = PillowWriter(fps = 10))
    plt.show()