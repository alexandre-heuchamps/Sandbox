import sys
from typing import Tuple



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



if __name__ == "__main__":
    cl_parser = CLParser()