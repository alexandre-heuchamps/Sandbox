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
        """ Function returning the HELs for which consistency is checked """
        return self._HELs
    # ==========================================================================

    # ==========================================================================
    @property
    def drones(self) -> list[Drone]:
        """ Function returning the drones for which consistency is checked """
        return self._drones
    # ==========================================================================

    # ==========================================================================
    def HEL_in_world_t0(self, HEL: HEL) -> bool:
        """ Function checking if a HEL is within the world bounding box initially """
        w_xmin: tuple[float, float, float] = self.world.xmin
        w_xmax: tuple[float, float, float] = self.world.xmax
        all_min_ok: bool = all(h0 >= wmin for h0, wmin in zip(HEL.x0, w_xmin))
        all_max_ok: bool = all(h0 <= wmax for h0, wmax in zip(HEL.x0, w_xmax))
        return True if (all_min_ok and all_max_ok) else False
    # ==========================================================================

    # ==========================================================================
    def HELs_in_world_t0(self) -> list[bool]:
        """ Function checking if each HEL is within the world bounding box initially """
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
    def are_all_HELs_in_t0(self) -> bool:
        """ Function checking if all HELs are within the world bounding box initially """
        return all(self.HELs_in_world_t0())
    # ==========================================================================

    # ==========================================================================
    def drone_in_world_t0(self, drone: Drone) -> bool:
        """ Function checking if a given drone is within the world bounding box initially """
        w_xmin: tuple[float, float, float] = self.world.xmin
        w_xmax: tuple[float, float, float] = self.world.xmax
        all_min_ok: bool = all(d0 >= wmin for d0, wmin in zip(drone.x0, w_xmin))
        all_max_ok: bool = all(d0 <= wmax for d0, wmax in zip(drone.x0, w_xmax))
        return True if (all_min_ok and all_max_ok) else False
    # ==========================================================================

    # ==========================================================================
    def drones_in_world_t0(self) -> list[bool]:
        """ Function checking if each drone is within the world bounding box initially """
        w_xmin: tuple[float, float, float] = self.world.xmin
        w_xmax: tuple[float, float, float] = self.world.xmax
        is_inside = []
        for d in self.drones:
            d_x0 = d.x0
            all_min_ok: bool = all(d0 >= wmin for d0, wmin in zip(d_x0, w_xmin))
            all_max_ok: bool = all(d0 <= wmax for d0, wmax in zip(d_x0, w_xmax))
            is_inside.append(True if (all_min_ok and all_max_ok) else False)
        return is_inside
    # ==========================================================================

    # ==========================================================================
    def are_all_drones_in_t0(self) -> bool:
        """ Function checking if all HELs are within the world bounding box initially """
        return all(self.drones_in_world_t0())
    # ==========================================================================

    # ==========================================================================
    def HEL_in_world_n(self, HEL: HEL, n: int) -> bool:
        """ Function checking if a HEL is within the world bounding box at iteration n """
        if n == 0:
            return self.HEL_in_world_t0(HEL = HEL)
        else:
            raise NotImplementedError("HEL_in_world_n not implemented for time n")
    # ==========================================================================

    # ==========================================================================
    def HELs_in_world_n(self, n: int) -> list[bool]:
        """ Function checking if each HEL is within the world bounding box at iteration n """
        if n == 0:
            return self.HELs_in_world_t0()
        else:
            raise NotImplementedError("HELs_in_world_n not implemented for time n")
    # ==========================================================================

    # ==========================================================================
    def are_all_HELs_in_n(self, n: int) -> bool:
        """ Function checking if all HELs are within the world bounding box at iteration n """
        if n == 0:
            return self.are_all_HELs_in_t0()
        else:
            raise NotImplementedError("are_all_HELs_in_n not implemented for time n")
    # ==========================================================================

    # ==========================================================================
    def drone_in_world_n(self, drone: Drone, n: int) -> bool:
        """ Function checking if a drone is within the world bounding box at iteration n """
        if n == 0:
            return self.drone_in_world_t0(drone = drone)
        else:
            raise NotImplementedError("drone_in_world_n not implemented for time n")
    # ==========================================================================

    # ==========================================================================
    def drones_in_world_n(self, n: int) -> list[bool]:
        """ Function checking if each drone is within the world bounding box at iteration n """
        if n == 0:
            return self.drones_in_world_t0()
        else:
            raise NotImplementedError("drones_in_world_n not implemented for time n")
    # ==========================================================================

    # ==========================================================================
    def are_all_drones_in_n(self, n: int) -> bool:
        """ Function checking if all HELs are within the world bounding box at iteration n """
        if n == 0:
            return self.are_all_drones_in_t0()
        else:
            raise NotImplementedError("are_all_drones_in_n not implemented for time n")
    # ==========================================================================







if __name__ == "__main__":
    w = World()
    hel1 = HEL()
    hel2 = HEL()
    d = Drone()
    c_check = ConsistencyCheckerWorld(world = w, HELs = [hel1, hel2], drones = [d])