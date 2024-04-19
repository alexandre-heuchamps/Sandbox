import sys
from typing import Tuple
from FileParser import FileParser
from FileParamParser import FileParamParser
from FilePropagParser import FilePropagParser
from HELParamParser import HELParamParser
from HELPropagParser import HELPropagParser
from DroneParamParser import DroneParamParser
from DronePropagParser import DronePropagParser



class CLParser:
    """ Class for parsing command line """

    __req_kw: Tuple[str, ...] = ('-nHEL', '-nDrone')

    def __init__(self) -> None:
        self._argv: list[str] = sys.argv
        self._argc: int = self.argc

    # ==========================================================================
    @classmethod
    def get_req_kw(cls) -> Tuple[str, ...]:
        """ Function returning a tuple containing the mandatory keywords to be
        found in the command line """
        return __class__.__req_kw
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def are_req_kw_in_CL(cls) -> bool:
        """ Function checking if command line contains required keywords """
        cl = [kw for kw in sys.argv if kw in cls.__req_kw]
        return True if len(cl) == len(cls.__req_kw) else False
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def get_min_argc(cls) -> int:
        """ Function returning the minimal length required for a valid command
        line input. That length is computed as 2 times the number of required
        keywords (as each of those need a value), plus the name of the file to
        run """
        return 2 * len(__class__.__req_kw) + 1
    # ==========================================================================

    # ==========================================================================
    @property
    def argv(self) -> list[str]:
        return self._argv
    # ==========================================================================

    # ==========================================================================
    @property
    def argc(self) -> int:
        """ Function returning the number of inputs on the command line """
        argc = len(self._argv)
        if ((argc >= __class__.get_min_argc()) and __class__.are_req_kw_in_CL()):
            return argc
        elif ((argc >= __class__.get_min_argc()) and not __class__.are_req_kw_in_CL()):
            raise ValueError(f"Wrong CL input. Missing required keyword(s)")
        else:
            raise ValueError(f"Wrong CL input: at least {__class__.get_min_argc() - argc} inputs missing")
    # ==========================================================================

    # ==========================================================================
    def get_opt_argv(self) -> list[str]:
        """ Function returning all the optional inputs """
        pattern = FileParser.get_req_kw()
        idx = [i for i, v in enumerate(self._argv) if pattern in v]
        s = [self._argv[i] for i in idx]
        f = [self._argv[i + 1] for i in idx]
        return [item for tup in list(zip(s, f)) for item in tup]
    # ==========================================================================

    # ==========================================================================
    def get_nHEL(self) -> int:
        """ Extract the number of requested HEL(s) from the command line """
        idx_nHEL = self._argv.index("-nHEL")
        return int(self._argv[idx_nHEL + 1])
    # ==========================================================================

    # ==========================================================================
    def get_nDrone(self) -> int:
        """ Extract the number of requested drone(s) from the command line """
        idx_nDrone = self._argv.index("-nDrone")
        return int(self._argv[idx_nDrone + 1])
    # ==========================================================================

    # ==========================================================================
    def get_param_files(self) -> list[str]:
        """ Function returning all the optional param files """
        pattern = FileParser.get_req_kw() + FileParamParser.get_req_kw()
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_propag_files(self) -> list[str]:
        """ Function returning all the optional propag files """
        pattern = FileParser.get_req_kw() + FilePropagParser.get_req_kw()
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_HEL_files(self) -> list[str]:
        """ Function returning all the optional HEL files """
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if "HEL" in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_drone_files(self) -> list[str]:
        """ Function returning all the optional drone files """
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if "drone" in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================



if __name__ == "__main__":
    cl_parser = CLParser()
    argv = cl_parser.argv
    print(f"Optional arguments {cl_parser.get_opt_argv()}")
    print(f"Optional parameter file(s) {cl_parser.get_param_files()}")
    print(f"Optional propagation file(s) {cl_parser.get_propag_files()}")
    print(f"Optional HEL file(s) {cl_parser.get_HEL_files()}")
    print(f"Optional drone file(s) {cl_parser.get_drone_files()}")