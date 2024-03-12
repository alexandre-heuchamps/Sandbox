import numpy as np
import Utils
from World import World
from Projectile import Projectile
from Target import Target

class Simulator():
    """ Class to represent a 'Simulator' (for ballistic propagation) """

    def __init__(self,
                    dt: float = 1e-3,
                    ndt: int = int(1e3),
                    world: World = World(),
                    tol: float = 1e-3,
                 ) -> None:
        """ Initiate an object of type 'Simulator' with given timestep and
        number of timesteps, world in which the simulation takes place, and
        tolerance

        Parameters
        ----------
        dt: <class 'float'> (default: 1e-3)
            Timestep used in the simulation
        ndt: <class 'int'> (default: int(1e3))
            Number of timesteps used in the simulation
        world: <class 'World'> (default: World())
            World in which the simulation takes place
        tol: <class 'float'> (default: 1e-3)
            Tolerance on the error """
        self._dt: float = dt
        self._ndt: int = ndt
        self._world: World = world
        self._tol: float = tol

    # ==========================================================================
    @property
    def dt(self) -> float:
        """ Get or set the current timestep """
        return self._dt

    @dt.setter
    def dt(self, dt: float = 1e-3) -> None:
        self._dt: float = dt
    # ==========================================================================

    # ==========================================================================
    @property
    def ndt(self) -> int:
        """ Get or set the number of timestep """
        return self._ndt

    @ndt.setter
    def ndt(self, ndt: int = int(1e3)) -> None:
        self._ndt: int = ndt
    # ==========================================================================

    # ==========================================================================
    @property
    def world(self) -> World:
        """ Get or set the world in which the simulation takes place """
        return self._world

    @world.setter
    def world(self, world: World = World()) -> None:
        self._world: World = world
    # ==========================================================================

    # ==========================================================================
    @property
    def tol(self) -> float:
        """ Get or set the tolerance on the error  """
        return self._tol

    @tol.setter
    def tol(self, tol: float = 1e-3) -> None:
        self._tol: float = tol
    # ==========================================================================

    # ==========================================================================
    def run(self, target: Target, projectile: Projectile) -> None:
        """ Function performing the ballistic propagation

        Parameters
        ----------
        target: <class 'Target'>
            Target to be neutralised
        projectile: <class 'Projectile'>
            Projectile neutralising the target """
        for n in range(self.ndt):
            print(n)
    # ==========================================================================



if __name__ == "__main__":
    sim = Simulator()