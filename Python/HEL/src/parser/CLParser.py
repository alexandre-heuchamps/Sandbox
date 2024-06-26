import sys
from typing import Tuple
from .FileParser import FileParser
from .FileParamParser import FileParamParser
from .FilePropagParser import FilePropagParser



class CLParser:
    """ Class for parsing command line """

    _req_kw: Tuple[str, ...] = ('-nHEL', '-nDrone')

    def __init__(self) -> None:
        self._argv: list[str] = sys.argv
        self._argc: int = self.argc

    # ==========================================================================
    @classmethod
    def get_req_kw(cls) -> Tuple[str, ...]:
        """ Function returning a tuple containing the mandatory keywords to be
        found in the command line """
        return cls._req_kw
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def are_req_kw_in_CL(cls) -> bool:
        """ Function checking if command line contains required keywords """
        cl = [kw for kw in sys.argv if kw in cls._req_kw]
        return True if len(cl) == len(cls._req_kw) else False
    # ==========================================================================

    # ==========================================================================
    @classmethod
    def get_min_argc(cls) -> int:
        """ Function returning the minimal length required for a valid command
        line input. That length is computed as 2 times the number of required
        keywords (as each of those need a value), plus the name of the file to
        run """
        return 2 * len(cls._req_kw) + 1
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
        if ((argc >= CLParser.get_min_argc()) and CLParser.are_req_kw_in_CL()):
            return argc
        elif ((argc >= CLParser.get_min_argc()) and not CLParser.are_req_kw_in_CL()):
            raise ValueError(f"Wrong CL input. Missing required keyword(s)")
        else:
            raise ValueError(f"Wrong CL input: at least {CLParser.get_min_argc() - argc} inputs missing")
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
    def get_opt_argv(self) -> list[str]:
        """ Function returning all the optional inputs """
        pattern = FileParser.get_req_kw()
        idx = [i for i, v in enumerate(self._argv) if pattern in v]
        s = [self._argv[i] for i in idx]
        f = [self._argv[i + 1] for i in idx]
        return [item for tup in list(zip(s, f)) for item in tup]
    # ==========================================================================

    # ==========================================================================
    def get_opt_files(self) -> list[str]:
        """ Function returning all the optional files """
        pattern = FileParser.get_req_kw()
        opt_argv = self.get_opt_argv()
        idx = [i for i, s in enumerate(opt_argv) if pattern in s]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_nopt_files(self) -> int:
        """ function returning the number of optional arguments """
        return len(self.get_opt_files())
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
    def get_nparam_files(self) -> int:
        """ Function returning the number of param files """
        return len(self.get_param_files())
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
    def get_npropag_files(self) -> int:
        """ Function returning the number of propagation files """
        return len(self.get_propag_files())
    # ==========================================================================

    # ==========================================================================
    def get_HEL_files(self) -> list[str]:
        """ Function returning all the optional HEL files """
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if "HEL" in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_nHEL_files(self) -> int:
        """ Function returning the number of HEL-related files """
        return len(self.get_HEL_files())
    # ==========================================================================

    # ==========================================================================
    def get_HEL_param_files(self) -> list[str]:
        """ Function returning all the optional param HEL files """
        opt_argv = self.get_opt_argv()
        pattern = FileParser.get_req_kw() + FileParamParser.get_req_kw() + "-HEL"
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_nHEL_param_files(self) -> list[str]:
        """ Function returning the number of HEL param files """
        return len(self.get_HEL_param_files())
    # ==========================================================================

    # ==========================================================================
    def get_HEL_propag_files(self) -> list[str]:
        """ Function returning all the optional HEL propagation files """
        opt_argv = self.get_opt_argv()
        pattern = FileParser.get_req_kw() + FilePropagParser.get_req_kw() + "-HEL"
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_nHEL_propag_files(self) -> list[str]:
        """ Function returning the number of HEL propagation files """
        return len(self.get_HEL_propag_files())
    # ==========================================================================

    # ==========================================================================
    def get_drone_files(self) -> list[str]:
        """ Function returning all the optional drone files """
        opt_argv = self.get_opt_argv()
        idx = [i for i, v in enumerate(opt_argv) if "drone" in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_ndrone_files(self) -> int:
        """ Function returning the number of drone-related files """
        return len(self.get_drone_files())
    # ==========================================================================

    # ==========================================================================
    def get_drone_param_files(self) -> list[str]:
        """ Function returning all the optional param drone files """
        opt_argv = self.get_opt_argv()
        pattern = FileParser.get_req_kw() + FileParamParser.get_req_kw() + "-drone"
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_ndrone_param_files(self) -> list[str]:
        """ Function returning the number of drone param files """
        return len(self.get_drone_param_files())
    # ==========================================================================

    # ==========================================================================
    def get_drone_propag_files(self) -> list[str]:
        """ Function returning all the optional drone propagation files """
        opt_argv = self.get_opt_argv()
        pattern = FileParser.get_req_kw() + FilePropagParser.get_req_kw() + "-drone"
        idx = [i for i, v in enumerate(opt_argv) if pattern in v]
        return [opt_argv[i + 1] for i in idx]
    # ==========================================================================

    # ==========================================================================
    def get_ndrone_propag_files(self) -> list[str]:
        """ Function returning the number of drone propagation files """
        return len(self.get_drone_propag_files())
    # ==========================================================================



if __name__ == "__main__":
    cl_parser = CLParser()
    f_parser = FileParser(files = cl_parser.get_opt_files())
    fparam_parser = FileParamParser(files = cl_parser.get_param_files())
    fpropag_parser = FilePropagParser(files = cl_parser.get_propag_files())