from typing import Tuple
from FileParser import FileParser



class FilePropagParser(FileParser):
    """ Class for parsing input param files """

    __req_kw: Tuple[str, ...] = ("-propag")

    def __init__(self, files: list[str]) -> None:
        self._files: list[str] = files

    # ==========================================================================
    @classmethod
    def get_req_kw(cls) -> Tuple[str, ...]:
        return __class__.__req_kw
    # ==========================================================================

    # ==========================================================================
    @property
    def files(self) -> list[str]:
        return self._files
    # ==========================================================================