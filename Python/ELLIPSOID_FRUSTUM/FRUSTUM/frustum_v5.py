import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Frustum:
    """ A class to represent a conical frustum """

    def __init__(self,
                    r1: float,
                    c: tuple[float, float, float],
                    h: float,
                    a: float,
                    v: tuple[float, float, float] = (1.0, 1.0, 1.0),
                    npts: int = 200,
                ) -> None:
        self._r1: float = r1
        self._c: tuple[float, float, float] = c
        self._h: float = h
        self._a: float = a
        self._v: tuple[float, float, float] = v
        self._npts: int = npts

    # ==========================================================================
    @property
    def r1(self) -> float:
        return self._r1

    @r1.setter
    def r1(self, r1: float) -> None:
        self._r1 = r1
    # ==========================================================================

    # ==========================================================================
    @property
    def c(self) -> tuple[float, float, float]:
        return self._c

    @c.setter
    def c(self, c: tuple[float, float, float]) -> None:
        self._c = c
    # ==========================================================================

    # ==========================================================================
    @property
    def h(self) -> float:
        return self._h

    @h.setter
    def h(self, h: float) -> None:
        self._h = h
    # ==========================================================================

    # ==========================================================================
    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, a: float) -> None:
        self._a = a
    # ==========================================================================

    # ==========================================================================
    @property
    def v(self) -> tuple[float, float, float]:
        return self._v

    @v.setter
    def v(self, v: tuple[float, float, float]) -> None:
        self._v = v
    # ==========================================================================

    # ==========================================================================
    @property
    def npts(self) -> int:
        return self._npts

    @npts.setter
    def npts(self, npts: int) -> None:
        self._npts = npts
    # ==========================================================================

    # ==========================================================================
    def create_frustum(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Create the base of the frustum
        theta = np.linspace(0.0, 2.0 * np.pi, self.npts)
        x = self.c[0] + self.r1 * np.cos(theta)
        y = self.c[1] + self.r1 * np.sin(theta)
        z = self.c[2] + np.zeros_like(x)

        # Calculate the radius of the top of the frustum based on the opening angle
        r2 = self.r1 + self.h * np.tan(self.a)

        # Create the top of the frustum
        x2 = self.c[0] + r2 * np.cos(theta)
        y2 = self.c[1] + r2 * np.sin(theta)
        z2 = self.c[2] + h * np.ones_like(x2)

        # Combine the coordinates
        x = np.append(x, x2)
        y = np.append(y, y2)
        z = np.append(z, z2)

        # Reshape the arrays into 2D arrays for plot_surface
        x = x.reshape((2, self.npts))
        y = y.reshape((2, self.npts))
        z = z.reshape((2, self.npts))

        return x, y, z
    # ==========================================================================

    # ==========================================================================
    def orient_frustum(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        x, y, z = self.create_frustum()

        # Normalize the vector
        self.v = np.array(self.v) / np.linalg.norm(self.v)

        # Rotate the points to align with the vector v
        # Calculate the rotation vector and angle
        zaxis = [0.0, 0.0, 1.0]
        rot_vector = np.cross(zaxis, self.v)
        rot_angle = np.arccos(np.dot(zaxis, self.v))
        rotation = R.from_rotvec(rot_angle * rot_vector)
        x = np.ravel(x) - self.c[0]
        y = np.ravel(y) - self.c[1]
        z = np.ravel(z) - self.c[2]
        points = rotation.apply(np.column_stack((x, y, z)))

        # Split the points back into x, y, z
        x = points[:, 0] + self.c[0]
        y = points[:, 1] + self.c[1]
        z = points[:, 2] + self.c[2]

        # Reshape the arrays into 2D arrays for plot_surface
        x = x.reshape((2, self.npts))
        y = y.reshape((2, self.npts))
        z = z.reshape((2, self.npts))

        return x, y, z
    # ==========================================================================




if __name__ == "__main__":
    cf = (0.0, 1.0, 3.5)
    r1 = .5
    alpha = np.pi / 18
    h = 2.3

    frustum = Frustum(r1 = r1, c = cf, h = h, a = alpha)
    xf, yf, zf = frustum.create_frustum()
    frustum.v = (1.0, 0.0, 0.0)
    xfr, yfr, zfr = frustum.orient_frustum()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    ax.plot_surface(xf, yf, zf, color = 'b', alpha = 0.5)
    ax.plot_surface(xfr, yfr, zfr, color = 'r', alpha = 0.5)
    ax.set_aspect('equal')
    plt.show()