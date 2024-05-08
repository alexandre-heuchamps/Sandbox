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

    # ==========================================================================
    @property
    def c(self) -> np.ndarray:
        return self._c

    @c.setter
    def c(self, c: list[float]) -> None:
        self._c = np.array(c)
    # ==========================================================================

    # ==========================================================================
    @property
    def Sigma(self) -> np.ndarray:
        return self._Sigma

    @Sigma.setter
    def Sigma(self, Sigma: list[float]) -> None:
        self._Sigma = np.array(Sigma)
    # ==========================================================================

    # ==========================================================================
    @property
    def U(self) -> np.ndarray:
        return self._U

    @U.setter
    def U(self, U: list[float]) -> None:
        self._U = np.array(U)
    # ==========================================================================