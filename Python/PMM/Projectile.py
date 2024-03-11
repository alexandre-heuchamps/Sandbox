import numpy as np
from Body import Body

class Projectile(Body):
    """ Class to represent a 'Projectile' """

    def __init__(self,
                    m: float = 1.0,
                    x0: np.array = np.array([0.0, 0.0, 0.0]),
                    cd0: float = 1.0,
                    k: float = 3.27,
                    n: float = 0.5,
                 ) -> None:
        """ Initiate an object of type 'Projectile' with given mass, initial
        position, subsonic drag coefficient, peak drag coefficient value, and
        exponent of drag decrease

        Parameters
        ----------
        m: <class 'float'> (default: 1.0)
            Mass of the created projectile
        x0: <class 'numpy.array'> (default: [0.0, 0.0, 0.0])
            Initial position of the created projectile
        cd0: <class 'float'> (default: 1.0)
            Subsonic (constant) drag coefficient of the created projectile
        k: <class 'float'> (default: 3.27)
            Peak drag coeficient in transonic regime for the created projectile
        n: <class 'float'> (default: 0.5)
            Exponent in supersonic drag coefficient of the created projectile """
        super().__init__(m = m, x0 = x0)
        self._cd0: float = cd0
        self._k: float = k
        self._n: float = n

    # ==========================================================================
    @property
    def cd0(self) -> float:
        """ Get or set the projectile subsonic (constant) drag coefficient """
        return self._cd0

    @cd0.setter
    def cd0(self, cd0: float = 1.0) -> None:
        self._cd0: float = cd0
    # ==========================================================================

    # ==========================================================================
    @property
    def k(self) -> float:
        """ Get or set the projectile peak drag coefficient """
        return self._k

    @k.setter
    def k(self, k: float = 1.0) -> None:
        self._k: float = k
    # ==========================================================================

    # ==========================================================================
    @property
    def n(self) -> float:
        """ Get or set the exponent for projectile drag decrease """
        return self._n

    @n.setter
    def n(self, n: float = 1.0) -> None:
        self._n: float = n
    # ==========================================================================



if __name__ == "__main__":
    proj = Projectile()