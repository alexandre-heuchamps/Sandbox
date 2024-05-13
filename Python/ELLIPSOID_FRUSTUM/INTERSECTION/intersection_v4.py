import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_ellispoid(c: tuple[float, float, float],
                    l: tuple[float, float, float],
                    Theta: np.ndarray,
                    Phi: np.ndarray,
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X_ell = c[0] + l[0] * np.outer(np.sin(Phi), np.cos(Theta))
    Y_ell = c[1] + l[1] * np.outer(np.sin(Phi), np.sin(Theta))
    Z_ell = c[2] + l[2] * np.outer(np.cos(Phi), np.ones_like(Theta))
    return X_ell, Y_ell, Z_ell

def is_on_ell_surf(x: tuple[float, float, float],
                    c: tuple[float, float, float],
                    l: tuple[float, float, float],
                ) -> bool:
    return (
                (
                    ((x[0] - c[0]) / l[0])**2
                    + ((x[1] - c[1]) / l[1])**2
                    + ((x[2] - c[2]) / l[2])**2
                )
                ==
                1
            )

def get_con_frust(c: tuple[float, float, float],
                        theta: np.ndarray,
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

def is_inside_fru(x: tuple[float, float, float],
                    c: tuple[float, float, float],
                    r1: float,
                    z: float,
                    alpha: float,
                ) -> bool:
    r_squared = (x[0] - c[0])**2 + (x[1] - c[1])**2

    def r(z: float) -> float:
        return r1 + (z - c[2]) * np.tan(alpha)

    return (r_squared <= r(x[2]) and c[2] <= x[2] <= c[2] + z)





def is_inside_fru_vectorized(x, c, r1, z, alpha):
    r_squared = (x[0] - c[0])**2 + (x[1] - c[1])**2
    def r(z):
        return r1 + (z - c[2]) * np.tan(alpha)
    return (r_squared <= r(x[2])) & (c[2] <= x[2]) & (x[2] <= c[2] + z)


if __name__ == "__main__":
    # Create mesh points
    ntheta = 50
    nphi = 50
    theta = np.linspace(0, 2 * np.pi, ntheta)
    phi = np.linspace(0, np.pi, nphi)
    Theta, Phi = np.meshgrid(theta, phi)

    # Ellipsoid
    ce = [0.0, 0.0, 5.0]
    l = [2.0, 1.25, 0.5]
    Xe, Ye, Ze = get_ellispoid(ce, l, Theta, Phi)

    # Conical frustum
    cf = [0.0, 0.0, 0.0]
    h = np.linalg.norm(np.array(cf) - np.array(ce))
    r1 = .5
    nz = 200
    z = np.linspace(cf[-1], h, nz)
    alpha = np.pi / 45
    Xf, Yf, Zf = get_con_frust(cf, theta, r1, alpha, z)

    Xe_flat, Ye_flat, Ze_flat = np.ravel(Xe), np.ravel(Ye), np.ravel(Ze)
    inside_fru = is_inside_fru_vectorized((Xe_flat, Ye_flat, Ze_flat), cf, r1, h, alpha)
    pts = np.vstack((Xe_flat[inside_fru], Ye_flat[inside_fru], Ze_flat[inside_fru])).T
    pts = np.unique(pts, axis = 0)

    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(Xe, Ye, Ze, color = 'r', alpha = 0.005)
    ax.plot_surface(Xf, Yf, Zf, color = 'b', alpha = 0.35)
    ax.scatter(*pts.T, s = 1.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()