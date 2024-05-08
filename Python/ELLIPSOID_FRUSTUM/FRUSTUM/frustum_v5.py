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
                ) -> None:
        self._r1: float = r1
        self._c: tuple[float, float, float] = c
        self._h: float = h
        self._a: float = a

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




if __name__ == "__main__":
    pass