import numpy as np

class Body():
    """ Generic class to represent a 'body'. Can be a projectile or a target """

    def __init__(self,
                    m: float = 1.0,
                    x0: np.ndarray = np.array([0.0, 0.0, 0.0]),
                 ) -> None:
        """ Initiate an object of type 'Body' with a given mass an initial position

        Parameters
        ----------
        m: <class 'float'> (default: 1.0)
            Mass of the created object
        x0: <class 'numpy.ndarray'> (default: [0.0, 0.0, 0.0])
            Initial position of the created object """
        self._m = m
        self._x0 = x0



if __name__ == "__main__":
    b = Body()