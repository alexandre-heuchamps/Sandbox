from typing import Tuple



class FileParser:
    """ Class for parsing input files """

    __req_kw: Tuple[str, ...] = ("--file")

    def __init__(self, file: str) -> None:
        self._file: str = file

    # ==========================================================================
    @classmethod
    def get_req_kw(cls) -> Tuple[str, ...]:
        return __class__.__req_kw
    # ==========================================================================

    # ==========================================================================
    @property
    def file(self) -> str:
        return self._file
    # ==========================================================================