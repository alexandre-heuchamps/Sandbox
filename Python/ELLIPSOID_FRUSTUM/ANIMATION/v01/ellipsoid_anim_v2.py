import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter





def get_ellispoid(c: tuple[float, float, float],
                    l: tuple[float, float, float],
                    Theta: np.ndarray,
                    Phi: np.ndarray,
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X = c[0] + l[0] * np.outer(np.sin(Phi), np.cos(Theta))
    Y = c[1] + l[1] * np.outer(np.sin(Phi), np.sin(Theta))
    Z = c[2] + l[2] * np.outer(np.cos(Phi), np.ones_like(Theta))
    return X, Y, Z





def get_con_frust(c: tuple[float, float, float],
                    theta: np.ndarray,
                    r1: float,
                    alpha: float,
                    zmax: float,
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    nz = 200
    z = np.linspace(c[2], zmax, nz)
    Theta, Z = np.meshgrid(theta, z)
    R = r1 + Z * np.tan(alpha)
    X = c[0] + R * np.cos(Theta)
    Y = c[1] + R * np.sin(Theta)
    Z = c[2] + Z
    return X, Y, Z





def rotate_ellipsoid(t: np.float64,
                        slerp: sp.spatial.transform._rotation.Rotation,
                        c_interp: np.ndarray,
                        l: list[float]
                    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x_e, y_e, z_e = get_ellispoid(
                    [c_interp[0](t), c_interp[1](t), c_interp[2](t)],
                    l,
                    Theta,
                    Phi,
                )
    rotation_e = slerp(t)
    rotated_e = rotation_e.apply(
                    np.column_stack(
                        [np.ravel(x_e), np.ravel(y_e), np.ravel(z_e)]
                    )
                )
    x_e = rotated_e[:, 0].reshape(x_e.shape)
    y_e = rotated_e[:, 1].reshape(y_e.shape)
    z_e = rotated_e[:, 2].reshape(z_e.shape)
    return x_e, y_e, z_e





def rotate_con_frust(t: np.float64,
                        slerp: sp.spatial.transform._rotation.Rotation,
                        c_interp: np.ndarray,
                        theta: np.ndarray,
                        r1: float,
                        alpha: float,
                        zmax: float,
                    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x_f, y_f, z_f = get_con_frust(
                    [c_interp[0](t), c_interp[1](t), c_interp[2](t)],
                    theta,
                    r1,
                    alpha,
                    zmax
                )
    rotation_f = slerp(t)
    rotated_f = rotation_f.apply(
                    np.column_stack(
                        [np.ravel(x_f), np.ravel(y_f), np.ravel(z_f)]
                    )
                )
    x_f = rotated_f[:, 0].reshape(x_f.shape)
    y_f = rotated_f[:, 1].reshape(y_f.shape)
    z_f = rotated_f[:, 2].reshape(z_f.shape)
    return x_f, y_f, z_f





def animate_objs(t: np.float64,
                    slerp_e: sp.spatial.transform._rotation.Rotation,
                    ce_interp: np.ndarray,
                    l: list[float],
                    slerp_f: sp.spatial.transform._rotation.Rotation,
                    cf_interp: np.ndarray,
                    theta: np.ndarray,
                    r1: float,
                    alpha: float,
                    ax,
                ) -> None:
    x_e, y_e, z_e = rotate_ellipsoid(t, slerp_e, ce_interp, l)
    zmax = ce_interp[2](t) - cf_interp[2](t)
    x_f, y_f, z_f = rotate_con_frust(t, slerp_f, cf_interp, theta, r1, alpha, zmax)
    print(f"Frustum centre basis: ({cf_interp[0](t)}, {cf_interp[1](t)}, {cf_interp[2](t)})")
    ax.cla()
    ax.plot_surface(x_e, y_e, z_e, color = 'r', alpha = .005)
    ax.plot_surface(x_f, y_f, z_f, color = 'b', alpha = .75)
    del x_e, y_e, z_e, x_f, y_f, z_f
    ax.set_xlim([-5.0, 5.0])
    ax.set_ylim([-5.0, 5.0])
    ax.set_zlim([-11.0, 11.0])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')





def get_quaternion(theta, phi):
    # Convert spherical coordinates to quaternion
    w = np.cos(phi / 2) * np.cos(theta / 2)
    x = -np.cos(phi / 2) * np.sin(theta / 2)
    y = -np.sin(phi / 2) * np.sin(theta / 2)
    z = -np.sin(phi / 2) * np.cos(theta / 2)
    return [w, x, y, z]





if __name__ == "__main__":
    # -------------------
    # Create angular mesh
    # -------------------
    ntheta = 50
    nphi = 50
    theta = np.linspace(0, 2 * np.pi, ntheta)
    phi = np.linspace(0, np.pi, nphi)
    Theta, Phi = np.meshgrid(theta, phi)

    # --------------------
    # Ellipsoid parameters
    # --------------------
    lx = 2.5
    ly = 1.5
    lz = .5
    dims = [lx, ly, lz]

    # --------------------------
    # Conical frustum parametres
    # --------------------------
    r1 = .5
    alpha = np.pi / 30

    # -----------------------------------------
    # Key values (i.e. generalised "waypoints")
    # -----------------------------------------
    # Time
    ktimes = [0.0, 1.2, 2.6, 3.2, 4.1, 4.8]
    #Ellipsoid
    cx_e = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    cy_e = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    cz_e = [5.0, 1.0, .5, .5, .5, .5]
    ce = zip(cx_e, cy_e, cz_e)
    kt_e = np.radians([0.0, 23.5, 48.79, 67.2, 80.0, 90.0])
    kp_e = np.radians([0.0, 0.0, 0.0, 10.0, 17.5, 17.5])
    # Conical frustum
    cx_f = [0.0] * len(ktimes)
    cy_f = [0.0] * len(ktimes)
    cz_f = [-2.5] * len(ktimes)
    cf = zip(cx_f, cy_f, cz_f)

    # ---------------------------------------------
    # Relative positions and orientation of centres
    # ---------------------------------------------
    # Position
    kv = [np.array(ve) - np.array(vf) for ve, vf in zip(ce, cf)]
    kv_norm = [v / np.linalg.norm(v) for v in kv]
    # Orientation
    ktp = [np.array([np.arctan2(v[1], v[0]), np.arcsin(v[2])]) for v in kv_norm]

    # ------------------------------------------------------
    # Convert spherical coordinates to Cartesian coordinates
    # ------------------------------------------------------
    # Ellipsoid rotations
    krot_e = sp.spatial.transform.Rotation.from_euler('zyz',
                    np.column_stack(
                        [
                            kt_e,
                            -kp_e,
                            np.zeros_like(kt_e)
                        ]
                    )
                )
    # Conical frustum rotations
    krot_f = [sp.spatial.transform.Rotation.from_rotvec(np.arccos(np.dot([0, 0, 1], v/np.linalg.norm(v))) * np.cross([0, 0, 1], v)) for v in kv_norm]
    # Concatenate the rotations into a single Rotation instance
    krot_e = sp.spatial.transform.Rotation.concatenate(krot_e)
    krot_f = sp.spatial.transform.Rotation.concatenate(krot_f)

    # ------------------------------
    # Create rotation interpolations
    # ------------------------------
    # Ellipsoid
    slerp_e = sp.spatial.transform.Slerp(ktimes, krot_e)
    # Conical frustum
    slerp_f = sp.spatial.transform.Slerp(ktimes, krot_f)

    # -------------------------------------------
    # Create interpolation for centre coordinates
    # -------------------------------------------
    times = np.linspace(np.min(ktimes), np.max(ktimes), 50)
    # Ellipsoid
    cxe_interp = sp.interpolate.interp1d(ktimes, cx_e)
    cye_interp = sp.interpolate.interp1d(ktimes, cy_e)
    cze_interp = sp.interpolate.interp1d(ktimes, cz_e)
    ce_interp = [cxe_interp, cye_interp, cze_interp]
    # Conical frustum
    cxf_interp = sp.interpolate.interp1d(ktimes, cx_f)
    cyf_interp = sp.interpolate.interp1d(ktimes, cy_f)
    czf_interp = sp.interpolate.interp1d(ktimes, cz_f)
    cf_interp = [cxf_interp, cyf_interp, czf_interp]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ani = animation.FuncAnimation(fig, animate_objs, frames=times, fargs=(slerp_e, ce_interp, dims, slerp_f, cf_interp, theta, r1, alpha, ax,))
    ani.save(f"{__file__.split('.')[0]}.gif", writer = PillowWriter(fps = 30))
    plt.show()