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
                ) -> None:
        self._r1: float = r1
        self._c: tuple[float, float, float] = c
        self._h: float = h
        self._a: float = a
        self._v: tuple[float, float, float] = v

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




if __name__ == "__main__":
    cf = (0.0, 1.0, 3.5)
    r1 = .5
    alpha = np.pi / 18
    h = 2.3

    frustum = Frustum(r1 = r1, c = cf, h = h, a = alpha)