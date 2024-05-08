import numpy as np

class Ellipsoid:
    """ A class to represent an ellipsoid """

    def __init__(self,
                    c: tuple[float, float, float],
                    lx: float,
                    ly: float,
                    lz: float,
                    U: np.ndarray,
                ) -> None:
        self._c: np.ndarray = np.array(c)
        self._Sigma: np.ndarray = np.diag([1/lx**2, 1/ly**2, 1/lz**2])
        self._U: np.ndarray = np.array(U)