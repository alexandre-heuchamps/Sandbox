import numpy as np

class Body():
    """ Generic class to represent a 'Body'. Can be a projectile or a target """

    def __init__(self,
                    m: float = 1.0,
                    x0: np.array = np.array([0.0, 0.0, 0.0]),
                 ) -> None:
        """ Initiate an object of type 'Body' with a given mass an initial
        position

        Parameters
        ----------
        m: <class 'float'> (default: 1.0)
            Mass of the created object
        x0: <class 'numpy.array'> (default: [0.0, 0.0, 0.0])
            Initial position of the created object """
        self._m: float = m
        self._x0: np.array = x0
        self._x: list = [x0]
        self._v: list = []

    # ==========================================================================
    @property
    def m(self) -> float:
        """ Get or set the mass of the body """
        return self._m

    @m.setter
    def m(self, m: float = 1.0) -> None:
        self._m: float = m
    # ==========================================================================

    # ==========================================================================
    @property
    def x0(self) -> np.array:
        """ Get or set the initial position of the body """
        return self._x0

    @x0.setter
    def x0(self, x0: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._x0: np.array = x0
    # ==========================================================================

    # ==========================================================================
    @property
    def x(self) -> list:
        """ Get or set (append) the set of successive body positions """
        return self._x

    @x.setter
    def x(self, x: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._x.append(x)
    # ==========================================================================

    # ==========================================================================
    @property
    def v(self) -> list:
        """ Get or set (append) the set of successive body velocities """
        return self._v

    @v.setter
    def v(self, v: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._v.append(v)
    # ==========================================================================



if __name__ == "__main__":
    b = Body()