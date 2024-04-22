from src.body.World import World
from src.body.HEL import HEL
from src.body.Drone import Drone



class ConsistencyCheckerWorld:
    """ A class to check if drones and HEL are within the specified world """

    def __init__(self,
                    world: World,
                    HELs: list[HEL],
                    drones: list[Drone],
                ) -> None:
        self._world: World = world
        self._HELs: list[HEL] = HELs
        self._drones: list[Drone] = drones

    # ==========================================================================
    @property
    def world(self) -> World:
        """ Function returning the world in which consistency is checked """
        return self._world
    # ==========================================================================

    # ==========================================================================
    @property
    def HELs(self) -> list[HEL]:
        """ Function returning the list of HELs for which consistency is checked """
        return self._HELs
    # ==========================================================================

    # ==========================================================================
    @property
    def drones(self) -> list[Drone]:
        """ Function returning the list of drones for which consistency is checked """
        return self._drones
    # ==========================================================================

    # ==========================================================================
    def HEL_in_world_t0(self, HEL: HEL) -> bool:
        """ Function checking if a given HEL is within the world bounding box """
        w_xmin: tuple[float, float, float] = self.world.xmin
        w_xmax: tuple[float, float, float] = self.world.xmax
        all_min_ok: bool = all(h0 >= wmin for h0, wmin in zip(HEL.x0, w_xmin))
        all_max_ok: bool = all(h0 <= wmax for h0, wmax in zip(HEL.x0, w_xmax))
        return True if (all_min_ok and all_max_ok) else False
    # ==========================================================================

    # ==========================================================================
    def HELs_in_world_t0(self) -> list[bool]:
        """ Function checking if each HEL is within the world bounding box """
        w_xmin: tuple[float, float, float] = self.world.xmin
        w_xmax: tuple[float, float, float] = self.world.xmax
        is_inside = []
        for hel in self.HELs:
            hel_x0 = hel.x0
            all_min_ok: bool = all(h0 >= wmin for h0, wmin in zip(hel_x0, w_xmin))
            all_max_ok: bool = all(h0 <= wmax for h0, wmax in zip(hel_x0, w_xmax))
            is_inside.append(True if (all_min_ok and all_max_ok) else False)
        return is_inside
    # ==========================================================================

    # ==========================================================================
    def are_all_in_t0(self) -> bool:
        """ Function checking if all HELs are within the world bounding box """
        return all(self.HELs_in_world_t0())
    # ==========================================================================



if __name__ == "__main__":
    w = World()
    hel1 = HEL()
    hel2 = HEL()
    d = Drone()
    c_check = ConsistencyCheckerWorld(world = w, HELs = [hel1, hel2], drones = [d])
    print(f"World limits: {w.xmin} -> {w.xmax}")
    print(f"HEL1 initial position: {hel1.x0}")
    print(f"HEL2 initial position: {hel2.x0}")
    print(f"HEL1 in world initially? {c_check.HEL_in_world_t0(HEL = hel1)}")
    print(f"HEL2 in world initially? {c_check.HEL_in_world_t0(HEL = hel2)}")
    hel1.x0 = (1.0, 0.12, 3.12)
    print(f"HEL1 initial position: {hel1.x0}")
    print(f"HEL2 initial position: {hel2.x0}")
    print(f"HEL1 in world initially? {c_check.HEL_in_world_t0(HEL = hel1)}")
    print(f"HEL2 in world initially? {c_check.HEL_in_world_t0(HEL = hel2)}")
    print(f"HELs in world initially? {c_check.HELs_in_world_t0()}")
    print(f"All HELs in world initially? {c_check.are_all_in_t0()}")