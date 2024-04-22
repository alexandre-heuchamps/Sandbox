from ..checker.ConsistencyCheckerWorld import ConsistencyCheckerWorld as cworld
from ..checker.ConsistencyCheckerNames import ConsistencyCheckerNames as cnames
from ..parser.CLParser import CLParser
from ..parser.DroneParamParser import DroneParamParser
from ..parser.DronePropagParser import DronePropagParser
from ..parser.HELParamParser import HELParamParser
from .HEL import HEL
from .Drone import Drone
from .World import World

class Simulator:
    def __init__(self,
                    cl_parser: CLParser,
                    world: World,
                    dt: float = 1e-3,
                    t_max: float = 1e3,
                ) -> None:
        self._cl_parser: CLParser = cl_parser
        self._world: World = world
        self._dt: float = dt
        self._t_max: float = t_max
        self._HELs: list[HEL] = []
        self._Drones: list[Drone] = []

        if self.cl_parser.get_nopt_files():
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
    def HELs(self) -> list[HEL]:
        return self._HELs
    # ==========================================================================

    # ==========================================================================
    @property
    def Drones(self) -> list[Drone]:
        return self._Drones
    # ==========================================================================

    # ==========================================================================
    def initialisation_without_file(self) -> None:
        raise NotImplementedError("Simulation initialisation without input file under construction. Stay tuned!")
    # ==========================================================================

    # ==========================================================================
    def initialisation_with_file(self) -> None:
        nHEL = self._cl_parser.get_nHEL()
        HEL_params = HELParamParser(files = self._cl_parser.get_HEL_param_files())
        HEL_params_names = HEL_params.get_names_in_files()

        ndrone = self._cl_parser.get_nDrone()
        drone_params = DroneParamParser(file = self._cl_parser.get_drone_param_files())
        drone_params_names = drone_params.get_names_in_files()
        drone_propag = DronePropagParser(file = self._cl_parser.get_drone_propag_files())
        drone_propag_sheets = drone_propag.get_sheet_names()

        cnames(names_sheets = drone_propag_sheets, names_col = drone_params_names)

        print("Hey!")
    # ==========================================================================

    # ==========================================================================
    def run(self) -> None:
        raise NotImplementedError("Simulation run under construction. Stay tuned!")
    # ==========================================================================




if __name__ == "__main__":
    """ Note:
    Run the line
    python -m src.body.Simulator -nHEL 2 -nDrone 3 --file-param-HEL data\Effectors.xlsx --file-param-drone data\Drones_Params.xlsx --file-propag-drone data\Drones_Propagation.xlsx
    from HEL/ """
    cl_parser = CLParser()
    world = World()
    sim = Simulator(cl_parser = cl_parser, world = world)