from typing import List, Tuple
from CLParser import CLParser
from HELParser import HELParser
from DroneParser import DroneParser
from HEL import HEL
from Drone import Drone

class Simulator:
    def __init__(self,
                    cl_parser: CLParser,
                    dt: float = 1e-3,
                    t_max: float = 1e3,
                ) -> None:
        self._cl_parser: CLParser = cl_parser
        self._dt: float = dt
        self._t_max: float = t_max
        self._HELs: List[HEL] = []
        self._Drones: List[Drone] = []

        if self.cl_parser.has_files():
            self.initialisation_with_file()
        else:
            self.initialisation_without_file()

    # ==========================================================================
    @property
    def cl_parser(self) -> CLParser:
        return self._cl_parser
    # ==========================================================================

    # ==========================================================================
    @property
    def dt(self) -> float:
        return self._dt
    # ==========================================================================

    # ==========================================================================
    @dt.setter
    def dt(self, dt: float = 1e-3) -> None:
        self._dt = dt
    # ==========================================================================

    # ==========================================================================
    @property
    def t_max(self) -> float:
        return self._t_max
    # ==========================================================================

    # ==========================================================================
    @t_max.setter
    def t_max(self, t_max: float = 1e3) -> None:
        self._t_max = t_max
    # ==========================================================================

    # ==========================================================================
    @property
    def HELs(self) -> List[HEL]:
        return self._HELs
    # ==========================================================================

    # ==========================================================================
    @property
    def Drones(self) -> List[Drone]:
        return self._Drones
    # ==========================================================================

    # ==========================================================================
    def initialisation_without_file(self) -> None:
        raise NotImplementedError("Simulation initialisation without input file under construction. Stay tuned!")
    # ==========================================================================

    # ==========================================================================
    def initialisation_with_file(self) -> None:
        HEL_param_file = self._cl_parser.get_HEL_param_files()
        Drone_param_file = self._cl_parser.get_Drone_param_files()
        HEL_parser = HELParser(HEL_file = HEL_param_file[-1])
        nHEL = HEL_parser.get_nHEL(cl_parser = self._cl_parser)[0, 0]
        drone_parser_params = DroneParser(drone_file = Drone_param_file[-1])
        nDrone = drone_parser_params.get_sheet_number()

        HEL_names = HEL_parser.get_HEL_names()
        HEL_init_pos = HEL_parser.get_HEL_init_pos()
        HEL_lambdas = HEL_parser.get_HEL_wavelengths()
        HEL_Ps = HEL_parser.get_HEL_Ps()
        HEL_M2s = HEL_parser.get_HEL_M2s()
        HEL_Js = HEL_parser.get_HEL_jitters()
        HEL_w0s = HEL_parser.get_HEL_w0s()
        HEL_modes = HEL_parser.get_HEL_modes()
        for i in range(nHEL):
            self._HELs.append(
                                HEL(name = HEL_names[i],
                                    wavelength = HEL_lambdas[i],
                                    P = HEL_Ps[i],
                                    M2 = HEL_M2s[i],
                                    J = HEL_Js[i],
                                    w0 = HEL_w0s[i],
                                    mode = HEL_modes[i],
                                    x0 = HEL_init_pos[i],
                                )
                            )

        for i in range(nDrone):
            self._Drones.append(Drone())
    # ==========================================================================

    # ==========================================================================
    def run(self) -> None:
        print(self._HELs)
        print(self._Drones)
    # ==========================================================================




if __name__ == "__main__":
    cl_parser = CLParser()
    sim = Simulator(cl_parser = cl_parser)
    sim.run()