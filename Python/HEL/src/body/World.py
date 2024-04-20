from typing import Tuple

class World:
    """ Class representing the worldboundary in which a simulation is run """

    def __init__(self,
                    xmin: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                    xmax: Tuple[float, float, float] = (1.0, 1.0, 1.0),
                ) -> None:
        self._xmin: Tuple[float, float, float] = xmin
        self._xmax: Tuple[float, float, float] = xmax
        self._Lx: float = self._xmax[0] - self._xmin[0]
        self._Ly: float = self._xmax[1] - self._xmin[1]
        self._Lz: float = self._xmax[2] - self._xmin[2]

    # ==========================================================================
    @property
    def xmin(self) -> Tuple[float, float, float]:
        return self._xmin

    @xmin.setter
    def xmin(self, xmin: Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:
        self._xmin: Tuple[float, float, float] = xmin
    # ==========================================================================

    # ==========================================================================
    @property
    def xmax(self) -> Tuple[float, float, float]:
        return self._xmax

    @xmax.setter
    def xmax(self, xmax: Tuple[float, float, float] = (1.0, 1.0, 1.0)) -> None:
        self._xmax: Tuple[float, float, float] = xmax
    # ==========================================================================

    # ==========================================================================
    @property
    def Lx(self) -> float:
        return (self._xmax[0] - self._xmin[0])
    # ==========================================================================

    # ==========================================================================
    @property
    def Ly(self) -> float:
        return (self._xmax[1] - self._xmin[1])
    # ==========================================================================

    # ==========================================================================
    @property
    def Lz(self) -> float:
        return (self._xmax[2] - self._xmin[2])
    # ==========================================================================




if __name__ == "__main__":
    w = World()
    print(f"xmin: {w.xmin}, xmax: {w.xmax}, Lx: {w.Lx}, Ly: {w.Ly}, Lz: {w.Lz}")
    w.xmax = (2.36, 5.6, 9.84)
    print(f"xmin: {w.xmin}, xmax: {w.xmax}, Lx: {w.Lx}, Ly: {w.Ly}, Lz: {w.Lz}")