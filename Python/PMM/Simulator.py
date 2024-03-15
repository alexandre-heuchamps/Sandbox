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
    def get_point_to_hit(self, pt: np.array = [0.0, 0.0, 0.0]) -> np.array:
        for coords in self.world.targets[0].x:
            if np.array_equal(pt, coords):
                return pt

        # Alternative version:
        # if the arrays are 1D and have the same shape, the efficiency could be
        # improved by converting the list of arrays and the target array into
        # sets of tuples, then checking for membership.
        # This method works because sets in Python are implemented as hash tables
        # and membership checks in a set are generally faster than in a list.
        # However, this only works for 1D arrays of the same shape, and assumes
        # the order of elements matters (i.e., [0.0, 1.0] is not the same as
        # [1.0, 0.0]). If the arrays are not 1D or have different shapes, 
        # stick with the previous method.
        # The conversion to tuples and the creation of the set have a
        # computational cost, so this method will be more efficient only if
        # membership check happens many times.
        # For single check, previous method is better
        # coords = set(tuple(arr) for arr in self.world.targets[0].x)
        # if tuple(pt) in coords:
        #     return pt
        # else:
        #     pass
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