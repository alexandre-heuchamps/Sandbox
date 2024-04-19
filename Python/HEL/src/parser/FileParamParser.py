from typing import Tuple
from .FileParser import FileParser



class FileParamParser(FileParser):
    """ Class for parsing input param files """

    __req_kw: Tuple[str, ...] = ("-param")

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