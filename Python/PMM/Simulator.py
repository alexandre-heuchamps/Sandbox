import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
        self._world: World = world

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
    def run(self, target: Target, projectile: Projectile) -> None:
        """ Function performing the ballistic propagation

        Parameters
        ----------
        target: <class 'Target'>
            Target to be neutralised
        projectile: <class 'Projectile'>
            Projectile neutralising the target """
        pass
    # ==========================================================================

    # ==========================================================================
    def plot_vals(self, *v: np.array) -> None:
        """ Function plotting vectors against each other

        Parameters
        ----------
        *v: <class 'numpy.array'>
            Vectors to consider

        Returns
        -------
        _: """
        if len(v) == 2:
            plt.figure()
            plt.plot(*v)
            plt.show()
        elif len(v) == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(*v)
            plt.show()
        else:
            print("Invalid number of arguments. Provide only 2 or 3 arguments.")
    # ==========================================================================



if __name__ == "__main__":
    sim = Simulator()