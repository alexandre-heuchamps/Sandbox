import numpy as np
import scipy as sp
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
        self._x, self._y, self._z = self.create_frustum()

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
    @property
    def x(self) -> np.ndarray:
        return self._x

    @x.setter
    def x(self, x: np.ndarray) -> None:
        self._x = x
    # ==========================================================================

    # ==========================================================================
    @property
    def y(self) -> np.ndarray:
        return self._y

    @y.setter
    def y(self, y: np.ndarray) -> None:
        self._y = y
    # ==========================================================================

    # ==========================================================================
    @property
    def z(self) -> np.ndarray:
        return self._z

    @z.setter
    def z(self, z: np.ndarray) -> None:
        self._z = z
    # ==========================================================================

    # ==========================================================================
    def create_frustum(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Create the base of the frustum
        theta = np.linspace(0.0, 2.0 * np.pi, self.npts)
        self.x = self.c[0] + self.r1 * np.cos(theta)
        self.y = self.c[1] + self.r1 * np.sin(theta)
        self.z = self.c[2] + np.zeros_like(self.x)

        # Calculate the radius of the top of the frustum based on the opening angle
        r2 = self.r1 + self.h * np.tan(self.a)

        # Create the top of the frustum
        x2 = self.c[0] + r2 * np.cos(theta)
        y2 = self.c[1] + r2 * np.sin(theta)
        z2 = self.c[2] + self.h * np.ones_like(x2)

        # Combine the coordinates
        self.x = np.append(self.x, x2)
        self.y = np.append(self.y, y2)
        self.z = np.append(self.z, z2)

        # Reshape the arrays into 2D arrays for plot_surface
        self.x = self.x.reshape((2, self.npts))
        self.y = self.y.reshape((2, self.npts))
        self.z = self.z.reshape((2, self.npts))

        return self.x, self.y, self.z
    # ==========================================================================

    # ==========================================================================
    def orient_frustum(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Normalize the vector
        self.v = np.array(self.v) / np.linalg.norm(self.v)

        # Rotate the points to align with the vector v
        # Calculate the rotation vector and angle
        zaxis = [0.0, 0.0, 1.0]
        rot_vector = np.cross(zaxis, self.v)
        rot_angle = np.arccos(np.dot(zaxis, self.v))
        rotation = sp.spatial.transform.Rotation.from_rotvec(rot_angle * rot_vector)

        self.x = np.ravel(self.x) - self.c[0]
        self.y = np.ravel(self.y) - self.c[1]
        self.z = np.ravel(self.z) - self.c[2]
        points = rotation.apply(np.column_stack((self.x, self.y, self.z)))

        # Split the points back into x, y, z
        self.x = points[:, 0] + self.c[0]
        self.y = points[:, 1] + self.c[1]
        self.z = points[:, 2] + self.c[2]

        # Reshape the arrays into 2D arrays for plot_surface
        self.x = self.x.reshape((2, self.npts))
        self.y = self.y.reshape((2, self.npts))
        self.z = self.z.reshape((2, self.npts))
    # ==========================================================================