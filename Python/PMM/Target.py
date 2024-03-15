import numpy as np
from Body import Body
import Utils as u

class Target(Body):
    """ Class representing a 'Target' """

    def __init__(self,
                    m: float = 1.0,
                    x0: np.array = np.array([0.0, 0.0, 0.0]),
                    dims: np.array = np.array([1.0, 1.0, 1.0]),
                 ) -> None:
        """ Initiate an object of type 'Target' with a given mass, initial
        position, and dimensions. Alternatively, an object of type 'Target' can
        be constructed by specifying the path to a .kml file containing coordinates

        Parameters
        ----------
        m: <class 'float'> (default: 1.0)
            Mass of the created object
        x0: <class 'numpy.array'> (default: [0.0, 0.0, 0.0])
            Initial position of the created object """
        self._m: float = m
        self._x0: np.array = x0
        self._dims: np.array = dims
        self._x: list = [x0]
        self._v: list = []

    @classmethod
    def pos_from_file(cls, path_kml_file: str = "./Drone_Flight_Path.kml"):
        t = u.get_tree(file = path_kml_file)
        root = u.get_root(tree = t)
        x, y, z = u.get_coordinates(root = root, is_big = False, kw = "coordinates")
        x0 = np.array([x[0], y[0], z[0]])
        target = cls(x0 = x0)
    
        for xx, yy, zz in zip(x[1:], y[1:], z[1:]):
            target._x.append(np.array([xx, yy, zz]))

        return target

    # ==========================================================================
    @property
    def m(self) -> float:
        """ Get or set the mass of the body """
        return self._m

    @m.setter
    def m(self, m: float = 1.0) -> None:
        self._m: float = m
    # ==========================================================================

    # ==========================================================================
    @property
    def x0(self) -> np.array:
        """ Get or set the initial position of the body """
        return self._x0

    @x0.setter
    def x0(self, x0: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._x0: np.array = x0
        self._x[0] = x0
    # ==========================================================================

    # ==========================================================================
    @property
    def dims(self) -> np.array:
        """ Get or set the dimensions of the target """
        return self._dims

    @dims.setter
    def dims(self, dims: np.array = np.array([1.0, 1.0, 1.0])) -> None:
        self._dims = dims
    # ==========================================================================

    # ==========================================================================
    @property
    def x(self) -> list:
        """ Get or set (append) the set of successive body positions """
        return self._x

    @x.setter
    def x(self, x: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._x.append(x)
    # ==========================================================================

    # ==========================================================================
    @property
    def v(self) -> list:
        """ Get or set (append) the set of successive body velocities """
        return self._v

    @v.setter
    def v(self, v: np.array = np.array([0.0, 0.0, 0.0])) -> None:
        self._v.append(v)
    # ==========================================================================



if __name__ == "__main__":
    t = Target()
    t2 = Target.pos_from_file(path_kml_file = "./Drone_Flight_Path.kml")