import numpy as np

class Simulator():
    """ Class to represent a 'Simulator' (for ballistic propagation) """

    def __init__(self,
                    ndim: int = 3,
                    g: np.array = np.array([0.0, 0.0, -9.81]),
                    dt: float = 1e-3,
                    ndt: int = int(1e3),
                 ) -> None:
        """ Initiate an object of type 'Simulator' with a given number of
        dimensions, gravity vector, timestep, and number of timestep

        Parameters
        ----------
        ndim: <class 'int'> (default: 3)
            Dimension of the space in which the simulation takes place
        g: <class 'numpy.array'> (default: [0.0, 0.0, -9.81])
            Gravity of the space in which the simulation takes place
        dt: <class 'float'> (default: 1e-3)
            Timestep used in the simulation
        ndt: <class 'int'> (default: int(1e3))
            Number of timesteps used in the simulation """
        self._ndim: int = ndim
        self._g: np.array = g
        self._dt: float = dt
        self._ndt: int = ndt

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

    # ==========================================================================
    @property
    def dt(self) -> float:
        return self._dt

    @dt.setter
    def dt(self, dt: float = 1e-3) -> None:
        self._dt: float = dt
    # ==========================================================================

    # ==========================================================================
    @property
    def ndt(self) -> int:
        return self._ndt

    @ndt.setter
    def ndt(self, ndt: int = int(1e3)) -> None:
        self._ndt: int = ndt
    # ==========================================================================



if __name__ == "__main__":
    sim = Simulator()