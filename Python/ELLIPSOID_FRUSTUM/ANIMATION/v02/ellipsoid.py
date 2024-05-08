import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Ellipsoid:
    """ A class to represent an ellipsoid """

    def __init__(self,
                    c: tuple[float, float, float],
                    lx: float,
                    ly: float,
                    lz: float,
                    U: np.ndarray,
                    npts_theta: int = 100,
                    npts_phi: int = 100,
                ) -> None:
        self._c: np.ndarray = np.array(c)
        self._lx: float = lx
        self._ly: float = ly
        self._lz: float = lz
        self._Sigma: np.ndarray = np.diag([(1/self._lx)**2, (1/self._ly)**2, (1/self._lz)**2])
        self._U: np.ndarray = np.array(U)

        # Precompute the mesh for a unit sphere
        # -------------------------------------
        self._npts_theta: int = npts_theta
        self._npts_phi: int = npts_phi
        u = np.linspace(0, 2 * np.pi, self._npts_theta)
        v = np.linspace(0, np.pi, self._npts_phi)
        self._x_mesh = np.outer(np.cos(u), np.sin(v))
        self._y_mesh = np.outer(np.sin(u), np.sin(v))
        self._z_mesh = np.outer(np.ones(np.size(u)), np.cos(v))





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
    def lx(self) -> float:
        return self._lx

    @lx.setter
    def lx(self, lx: float) -> None:
        self._lx = lx
    # ==========================================================================

    # ==========================================================================
    @property
    def ly(self) -> float:
        return self._ly

    @ly.setter
    def ly(self, ly: float) -> None:
        self._ly = ly
    # ==========================================================================

    # ==========================================================================
    @property
    def lz(self) -> float:
        return self._lz

    @lz.setter
    def lz(self, lz: float) -> None:
        self._lz = lz
    # ==========================================================================





    # ==========================================================================
    @property
    def Sigma(self) -> np.ndarray:
        return self._Sigma
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
    @property
    def npts_theta(self) -> int:
        return self._npts_theta

    @npts_theta.setter
    def npts_theta(self, npts_theta: int) -> None:
        self._npts_theta = npts_theta
    # ==========================================================================

    # ==========================================================================
    @property
    def npts_phi(self) -> int:
        return self._npts_phi

    @npts_phi.setter
    def npts_phi(self, npts_phi: int) -> None:
        self._npts_phi = npts_phi
    # ==========================================================================





    # ==========================================================================
    def is_inside(self, x: list[float]) -> bool:
        x = np.array(x)
        diff = x - self.c
        result = diff.T @ self.U @ self.Sigma @ self.U.T @ diff
        return result <= 1
    # ==========================================================================

    # ==========================================================================
    def is_on(self, x: list[float]) -> bool:
        x = np.array(x)
        diff = x - self.c
        result = diff.T @ self.U @ self.Sigma @ self.U.T @ diff
        return result == 1
    # ==========================================================================





    # ==========================================================================
    def rotate(self, theta, phi) -> None:
        # Create a rotation matrix from the angles
        r = sp.spatial.transform.Rotation.from_euler('ZYX', [theta, 0, phi])
        # Apply the rotation matrix to U
        self._U = r.apply(self._U)
    # ==========================================================================





    # ==========================================================================
    def get_mesh(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        x = self._c[0] + self._lx * self._x_mesh
        y = self._c[1] + self._ly * self._y_mesh
        z = self._c[2] + self._lz * self._z_mesh
        return x, y, z
    # ==========================================================================

    # ==========================================================================
    def get_rotated_mesh(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        # Get the original mesh
        x, y, z = self.get_mesh()

        # Reshape the mesh arrays into 2D arrays
        x_flat = np.ravel(x) - self.c[0]
        y_flat = np.ravel(y) - self.c[1]
        z_flat = np.ravel(z) - self.c[2]
        mesh_flat = np.array([x_flat, y_flat, z_flat])

        # Apply the rotation to each point in the mesh
        rotated_mesh_flat = np.dot(self._U, mesh_flat)

        # Reshape the rotated mesh arrays back to the original shape
        x_rot = rotated_mesh_flat[0].reshape(x.shape) + self.c[0]
        y_rot = rotated_mesh_flat[1].reshape(y.shape) + self.c[1]
        z_rot = rotated_mesh_flat[2].reshape(z.shape) + self.c[2]

        return x_rot, y_rot, z_rot
    # ==========================================================================





if __name__ == "__main__":
    c = [0.0, 0.0, 0.0]
    lx = 2.3
    ly = 1.5
    lz = .84
    U = np.eye(3)
    ellipsoid = Ellipsoid(c = c, lx = lx, ly = ly, lz = lz, U = U)
    xmesh, ymesh, zmesh = ellipsoid.get_mesh()
    ellipsoid.rotate(np.pi / 6.0, 0.0)
    ellipsoid.c = [0.0, 0.0, 5.0]
    xmesh_rot, ymesh_rot, zmesh_rot = ellipsoid.get_rotated_mesh()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(xmesh, ymesh, zmesh, color = 'b', alpha = 0.5)
    ax.plot_surface(xmesh_rot, ymesh_rot, zmesh_rot, color = 'r', alpha = 0.5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_aspect('equal')
    plt.show()