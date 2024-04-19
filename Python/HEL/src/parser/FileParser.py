import pandas as pd
from typing import Tuple



class FileParser:
    """ Class for parsing input files """

    __req_kw: Tuple[str, ...] = ("--file")

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

    # ==========================================================================
    def get_Excel_file(self) -> list[pd.io.excel._base.ExcelFile]:
        return [pd.ExcelFile(f) for f in self._files]
    # ==========================================================================



if __name__ == "__main__":
    f_parser = FileParser(files = [])