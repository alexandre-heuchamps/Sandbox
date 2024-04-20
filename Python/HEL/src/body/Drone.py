import numpy as np
from typing import List, Tuple

class Drone:
    """ A class representing a drone """

    __cnt: int = 0

    def __init__(self,
                    ax1_angs0: Tuple[float, float] = (0.0, 0.0),
                    ax2_angs0: Tuple[float, float] = (0.0, 0.0),
                    ax3_angs0: Tuple[float, float] = (0.0, 0.0),
                    x0: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                    v0: float = 12.0,
                    v0_angs: Tuple[float, float] = (0.5 * np.pi, 0.0),
                    dam_fluence: float = 10.0,
                    dims: Tuple[float, float, float] = (.5, .15, 1.5),
                    id: int = 0,
                    priority: int = 0,
                    is_alive: bool = True,
                ) -> None:
        __class__.__cnt += 1
        self._ax1_angs0: Tuple[float, float] = ax1_angs0
        self._ax2_angs0: Tuple[float, float] = ax2_angs0
        self._ax3_angs0: Tuple[float, float] = ax3_angs0
        self._ax1_angs: List[Tuple[float, float]] = [self._ax1_angs0]
        self._ax2_angs: List[Tuple[float, float]] = [self._ax2_angs0]
        self._ax3_angs: List[Tuple[float, float]] = [self._ax3_angs0]
        self._x0: Tuple[float, float, float] = x0
        self._x: List[Tuple[float, float, float]] = [self._x0]
        self._v0: float = v0
        self._v0_angs: Tuple[float, float] = v0_angs
        self._v: List[Tuple[float, float, float]] = [(self._v0 * np.cos(self._v0_angs[0]) * np.cos(self._v0_angs[1]), self._v0 * np.sin(self._v0_angs[0]) * np.cos(self._v0_angs[1]), self._v0 * np.sin(self._v0_angs[1]))]
        self._v_angs: List[Tuple[float, float]] = [self._v0_angs]
        self._dam_fluence: float = dam_fluence
        self._dims: Tuple[float, float, float] = dims
        self._id: int = id
        self_priority: int = priority
        self._is_alive: bool = is_alive

    # ==========================================================================
    def __del__(self) -> None:
        __class__.__cnt -= 1
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def get_cnt(cls) -> int:
        return cls.__cnt
    # ==========================================================================

    # ==========================================================================
    @property
    def ax1_angs0(self) -> Tuple[float, float]:
        return self._ax1_angs0

    @ax1_angs0.setter
    def ax1_angs0(self, ax1_angs0: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax1_angs0 = ax1_angs0
        self._ax1_angs[0] = ax1_angs0
    # ==========================================================================

    # ==========================================================================
    @property
    def ax2_angs0(self) -> Tuple[float, float]:
        return self._ax2_angs0

    @ax2_angs0.setter
    def ax2_angs0(self, ax2_angs0: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax2_angs0 = ax2_angs0
        self._ax2_angs[0] = ax2_angs0
    # ==========================================================================

    # ==========================================================================
    @property
    def ax3_angs0(self) -> Tuple[float, float]:
        return self._ax3_angs0

    @ax3_angs0.setter
    def ax3_angs0(self, ax3_angs0: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax3_angs0 = ax3_angs0
        self._ax3_angs[0] = ax3_angs0
    # ==========================================================================

    # ==========================================================================
    @property
    def ax1_angs(self) -> List[Tuple[float, float]]:
        return self._ax1_angs

    @ax1_angs.setter
    def ax1_angs(self, ax1_angs: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax1_angs.append(ax1_angs)
    # ==========================================================================

    # ==========================================================================
    @property
    def ax2_angs(self) -> List[Tuple[float, float]]:
        return self._ax2_angs

    @ax2_angs.setter
    def ax2_angs(self, ax2_angs: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax2_angs.append(ax2_angs)
    # ==========================================================================

    # ==========================================================================
    @property
    def ax3_angs(self) -> List[Tuple[float, float]]:
        return self._ax3_angs

    @ax3_angs.setter
    def ax3_angs(self, ax3_angs: Tuple[float, float] = (.5 * np.pi, 0.0)) -> None:
        self._ax3_angs.append(ax3_angs)
    # ==========================================================================

    # ==========================================================================
    @property
    def x0(self) -> Tuple[float, float, float]:
        return self._x0

    @x0.setter
    def x0(self, x0: Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:
        self._x0 = x0
        self._x[0] = x0
    # ==========================================================================

    # ==========================================================================
    @property
    def x(self) -> List[Tuple[float, float, float]]:
        return self._x

    @x.setter
    def x(self, x: Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:
        self._x.append(x)
    # ==========================================================================

    # ==========================================================================
    @property
    def v0(self) -> float:
        return self._v0

    @v0.setter
    def v0(self, v0: float = 0.0) -> None:
        if v0 < 0.0:
            raise ValueError("Speed cannot be negative")
        self._v0 = v0
        self._v[0] = (v0 * np.cos(self._v0_angs[0]) * np.cos(self._v0_angs[1]),
                        v0 * np.sin(self._v0_angs[0]) * np.cos(self._v0_angs[1]),
                        v0 * np.sin(self._v0_angs[1]))
    # ==========================================================================

    # ==========================================================================
    @property
    def v0_angs(self) -> Tuple[float]:
        return self._v0_angs

    @v0_angs.setter
    def v0_angs(self, v0_angs: Tuple[float, float] = 0.0) -> None:
        self._v0_angs = v0_angs
        self._v_angs[0] = v0_angs
    # ==========================================================================

    # ==========================================================================
    @property
    def v(self) -> List[Tuple[float, float, float]]:
        return self._v
 
    @v.setter
    def v(self, v: Tuple[float, float, float] = (0.0, 1.0, 2.0)) -> None:
        self._v.append(v)
    # ==========================================================================

    # ==========================================================================
    @property
    def v_angs(self) -> List[Tuple[float, float]]:
        return self._v_angs

    @v_angs.setter
    def v_angs(self, v_angs: Tuple[float, float] = (0.0, 1.0)) -> None:
        self._v_angs.append(v_angs)
    # ==========================================================================

    # ==========================================================================
    @property
    def dam_fluence(self) -> float:
        return self._dam_fluence

    @dam_fluence.setter
    def dam_fluence(self, dam_fluence: float = 12.37) -> None:
        if dam_fluence <= 0.0:
            raise ValueError("Fluence damage threshold cannot be negative or zero")
        self._dam_fluence = dam_fluence
    # ==========================================================================

    # ==========================================================================
    @property
    def dims(self) -> Tuple[float, float, float]:
        return self._dims

    @dims.setter
    def dims(self, dims: Tuple[float, float, float] = (2.35, 8.47, 8.8)) -> None:
        if any(dim <= 0 for dim in dims):
            raise ValueError("Dimensions cannot be negative or zero")
        self._dims = dims
    # ==========================================================================

    # ==========================================================================
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int = 1) -> None:
        if id < 0:
            raise ValueError("Drone ID cannot be negative")
        self._id = id
    # ==========================================================================

    # ==========================================================================
    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, priority: int = 1) -> None:
        if priority < 0:
            raise ValueError("Drone priority cannot be negative")
        self._priority = priority
    # ==========================================================================

    # ==========================================================================
    @property
    def is_alive(self) -> bool:
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool = True) -> None:
        self._is_alive = is_alive
    # ==========================================================================




if __name__ == "__main__":
    d = Drone()
    print(d.__dict__)