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





if __name__ == "__main__":
    pass