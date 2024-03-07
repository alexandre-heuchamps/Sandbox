import numpy as np

class Simulator():
    """ Class to represent a 'Simulator' (for ballistic propagation) """

    def __init__(self,
                    dt: float = 1e-3,
                    ndt: int = int(1e3),
                 ) -> None:
        """ Initiate an object of type 'Simulator' with given timestep
        and number of timesteps

        Parameters
        ----------
        dt: <class 'float'> (default: 1e-3)
            Timestep used in the simulation
        ndt: <class 'int'> (default: int(1e3))
            Number of timesteps used in the simulation """
        self._dt: float = dt
        self._ndt: int = ndt

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