import numpy as np
import scipy as sp

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

    # ==========================================================================
    def is_inside(self, x: list[float]):
        x = np.array(x)
        diff = x - self.c
        result = diff.T @ self.U @ self.Sigma @ self.U.T @ diff
        return result <= 1
    # ==========================================================================

    # ==========================================================================
    def is_on(self, x: list[float]):
        x = np.array(x)
        diff = x - self.c
        result = diff.T @ self.U @ self.Sigma @ self.U.T @ diff
        return result == 1
    # ==========================================================================

    # # ==========================================================================
    # def rotate(self, theta, phi):
    #     # Create a rotation matrix from the angles
    #     r = sp.spatial.transform.Rotation.from_euler('ZYX', [theta, 0, phi])
    #     # Apply the rotation matrix to U
    #     self._U = r.apply(self._U)
    # # ==========================================================================




if __name__ == "__main__":
    c = [0.0, 0.0, 0.0]
    lx = 2.3
    ly = 1.5
    lz = .84
    U = np.eye(3)
    ellipsoid = Ellipsoid(c = c, lx = lx, ly = ly, lz = lz, U = U)

    # # Rotate the ellipsoid
    # ellipsoid.rotate(theta, phi)