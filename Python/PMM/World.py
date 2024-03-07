import numpy as np

class World():
    """ Class to represent the 'World' containing everything """

    def __init__(self,
                    ndim: int = 3,
                    g: np.array = np.array([0.0, 0.0, -9.81]),
                    targets: list = [],
                    platforms: list = [],
                 ) -> None:
        """ Initiate an object of type 'World' with a given number of
        dimensions, gravity vector, and lists of target(s) and platform(s)

        Parameters
        ----------
        ndim: <class 'int'> (default: 3)
            Dimension of the space in which the simulation takes place
        g: <class 'numpy.array'> (default: [0.0, 0.0, -9.81])
            Gravity of the space in which the simulation takes place
        targets: <class 'list'> (default: [])
            List of targets contained in the world
        platforms: <class 'list'> (default: [])
            List of platforms contained in the world """
        self._ndim: int = ndim
        self._g: np.array = g
        self._targets: list = targets
        self._platforms: list = platforms

    # ==========================================================================
    @property
    def ndim(self) -> int:
        return self._ndim

    @ndim.setter
    def ndim(self, ndim: int = 3) -> None:
        self._ndim: int = ndim
    # ==========================================================================

    # ==========================================================================
    @property
    def g(self) -> np.array:
        return self._g

    @g.setter
    def g(self, g: np.array = np.array([0.0, 0.0, -9.81])) -> None:
        if len(g) != self.ndim:
            print("Wrong input for gravity vector.")
            print("Setting last component to -9.81.")
            self._g: np.array = np.zeros( self.ndim )
            self._g[-1] = -9.81
        else:
            self._g = g
    # ==========================================================================



if __name__ == "__main__":
    world = World()