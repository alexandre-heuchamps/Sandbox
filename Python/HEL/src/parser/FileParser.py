import pandas as pd



class FileParser:
    """ Class for parsing input files """

    _req_kw: str = "--file"

    def __init__(self, files: list[str]) -> None:
        self._files: list[str] = files

    # ==========================================================================
    @classmethod
    def get_req_kw(cls) -> str:
        """ Function returning the required keyword(s) to be a file parser """
        return cls._req_kw
    # ==========================================================================

    # ==========================================================================
    @property
    def files(self) -> list[str]:
        """ Function returning all the files to be parsed """
        return self._files
    # ==========================================================================

    # ==========================================================================
    def get_Excel_files(self) -> list[pd.io.excel._base.ExcelFile]:
        """ Function returning the files as Excel format for inner processing """
        return [pd.ExcelFile(f) for f in self._files]
    # ==========================================================================

    # ==========================================================================
    def get_Excel_file(self, file: str) -> pd.io.excel._base.ExcelFile:
        """ Function returning the file as Excel format for inner processing """
        return pd.ExcelFile(file)
    # ==========================================================================

    # ==========================================================================
    def get_dfs(self) -> list[list[pd.core.frame.DataFrame]]:
        """ Function returning the dataframes corresponding to all the files """
        dfs = []
        for f in self._files:
            f_xlsx = self.get_Excel_file(file = f)
            dfs.append([f_xlsx.parse(s_name) for s_name in f_xlsx.sheet_names])
            f_xlsx.close()
        return dfs
    # ==========================================================================

    # ==========================================================================
    def get_sheet_names(self) -> list[list[str]]:
        """ Function returning a list of lists with each sheet name """
        names = []
        for f in self._files:
            f_xlsx = self.get_Excel_file(file = f)
            names.append([s_name for s_name in f_xlsx.sheet_names])
            f_xlsx.close()
        return names
    # ==========================================================================