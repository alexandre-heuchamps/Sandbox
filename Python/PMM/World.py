import numpy as np
from Body import Body

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
        """ Get or set the current space dimension. Setting the space dimension
        to a new value different from 2 or 3 will result in that dimension being
        set to 3 by default. """
        return self._ndim

    @ndim.setter
    def ndim(self, ndim: int = 3) -> None:
        ndim_chosen: int = self.check_ndim(ndim)
        self._ndim: int = ndim_chosen
        self._g: np.array = np.zeros( ndim_chosen )
        self._g[-1] = -9.81

    def check_ndim(self, ndim: int) -> int:
        """ Function checking if the input space dimension is valid. If not,
        output correct space dimension, set to 3 by default

        Parameters
        ----------
        ndim: <class 'int'>
            Space dimension

        Return
        ------
        ndim: <class 'int'> (default: 3)
            Valid space dimension """
        if ((ndim != 2) or (ndim != 3)):
            ndim_default = 3
            print(f"World only of dimension 2 or 3.")
            print(f"Entered {ndim}.")
            print(f"Changing to {ndim_default}")
            return ndim_default
        else:
            return ndim
    # ==========================================================================

    # ==========================================================================
    @property
    def g(self) -> np.array:
        """ Get or set the current gravity vector. Setting the gravity vector to
        something having a wrong dimension (i.e., different from the space
        dimension) will result in a default gravity vector of the right length
        with -9.81 as last component """
        return self._g

    @g.setter
    def g(self, g: np.array = np.array([0.0, 0.0, -9.81])) -> None:
        self._g = self.check_g(g)

    def check_g(self, g: np.array) -> np.array:
        """ Function checking if the input gravity vector is valid. If not,
        outputs an array of correct length with -9.81 as last component

        Parameters
        ----------
        g: <class 'np.array'>
            Gravity vector

        Return
        ------
        g: <class 'np.array'> (default: [0.0, 0.0, ..., 0.0, -9.81])
            Valid gravity vector """
        if len(g) != self.ndim:
            print("Wrong input for gravity vector.")
            print("Setting last component to -9.81.")
            g_default: np.array = np.zeros( self.ndim )
            g_default[-1] = -9.81
            return g_default
        else:
            return g
    # ==========================================================================

    # ==========================================================================
    @property
    def targets(self) -> list:
        """ Get or set the list of targets """
        return self._targets

    @targets.setter
    def targets(self, target: Body = Body()) -> None:
        print(target)
        self._targets.append(target)
    # ==========================================================================

    # ==========================================================================
    @property
    def platforms(self) -> list:
        """ Get or set the list of platforms """
        return self._platforms

    @platforms.setter
    def platforms(self, platform: Body = Body()) -> None:
        self._platforms.append(platform)
    # ==========================================================================



if __name__ == "__main__":
    w = World()
    print(f"Out1: {w.ndim}, {w.g}")
    w.ndim = 5
    print(f"Out2: {w.ndim}, {w.g}")
    w.g = [2.3, 6.4]
    print(f"Out3: {w.ndim}, {w.g}")
    w.g = [2.3, 6.4, 5.6]
    print(f"Out4: {w.ndim}, {w.g}")
    help(w)
    print(w.targets)